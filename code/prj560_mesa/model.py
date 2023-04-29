from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from enum import Enum
import math
import random
from mesa.datacollection import DataCollector




def count_survivors(model):
    return sum([1 for agent in model.schedule.agents if isinstance(agent, Civilian) and agent.found])
def count_dead(model):
    return sum([1 for agent in model.schedule.agents if isinstance(agent, Civilian) and agent.dead])

class Zone(Agent):
    def __init__(self, unique_id, model, zone_type):
        super().__init__(unique_id, model)
        self.zone_type = zone_type

    def step(self):
        pass

class ZoneCell(Agent):
    def __init__(self, unique_id, model, zone_type):
        super().__init__(unique_id, model)
        self.zone_type = zone_type

    def step(self):
        pass
def generate_zone_cells(model, zone, size):
    zone_cells = []
    for dx in range(-size, size + 1):
        for dy in range(-size, size + 1):
            x, y = (zone.pos[0] + dx) % model.grid.width, (zone.pos[1] + dy) % model.grid.height
            zone_cell = ZoneCell((zone.unique_id * 100) + len(zone_cells), model, zone.zone_type)
            zone_cells.append((zone_cell, (x, y)))
    return zone_cells





class SAR(Agent):
    def __init__(self, unique_id, model, is_robot_equipped=False):
        super().__init__(unique_id, model)
        self.supplies = 5
        self.is_robot_equipped = is_robot_equipped

    def tag_civilian(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        civilian = [obj for obj in cellmates if isinstance(obj, Civilian)]
        return civilian[0] if civilian else None

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        civilian = self.tag_civilian()
        if civilian and self.supplies > 0:
            civilian.tagged = True
            self.supplies -= 1
            if self.is_robot_equipped:
                civilian.found = True
        self.move()



class Civilian(Agent):
    def __init__(self, unique_id, model, wounded):
        super().__init__(unique_id, model)
        self.dead = False
        self.wounded = wounded
        self.timeToDie = random.randint(9,20) # implement an ever dwindling hit point
        self.found = False
        self.speed = 1 if not wounded else 0

    def move(self):
        if not self.dead and not self.wounded:
            if not self.found:
                possible_steps = self.model.grid.get_neighborhood(
                    self.pos, moore=True, include_center=False)
                new_position = self.random.choice(possible_steps)
                self.model.grid.move_agent(self, new_position)
            else:
                self.move_to_target()
        else:
            pass

    def move_to_target(self):
        # Civilian moves towards the nearest medical facility or evacuation zone
        pass

    def step(self):
        if self.wounded: # if hit point goes 0, civ dies
            self.timeToDie = self.timeToDie - 1
            if self.timeToDie <= 0:
                self.wounded = False
                self.dead = True
        self.move()

class Drone(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def rearm_sar(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        sar_agent = [obj for obj in cellmates if isinstance(obj, SAR)]
        return sar_agent[0] if sar_agent else None

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        sar_agent = self.rearm_sar()
        if sar_agent:
            sar_agent.supplies = 5
        self.move()

class UAV(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def detect_civilians(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        civilians = [obj for obj in cellmates if isinstance(obj, Civilian)]
        for civ in civilians:
            if random.random() < 0.5:  # Detection probability
                civ.found = True

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.detect_civilians()
        self.move()

# this stuff is main function
class SearchAndRescueModel(Model):
    def __init__(self, width, height):
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, False) # false for preventing torusing
        self.datacollector = DataCollector(
            model_reporters={"Survivors": count_survivors, "Dead": count_dead}
        )

        # hard code zone areas
        fob_center = (18, 10)
        fob_radius = 1
        med_center = (18, 15)
        med_radius = 1
        eva_center = (18, 5)
        eva_radius = 1
        dis_center = (10, 10)
        dis_radius = 5

        # Create agents
        for i in range(5):
            sar_agent = SAR(i, self, is_robot_equipped=(i % 2 == 0))
            self.schedule.add(sar_agent)
            # self.grid.place_agent(sar_agent, self.grid.find_empty())
            self.grid.place_agent(sar_agent, RandPlaceInArea(fob_center,fob_radius))

        for i in range(10):
            civilian = Civilian(i + 5, self, wounded=(i % 3 == 0))
            self.schedule.add(civilian)
            # self.grid.place_agent(civilian, self.grid.find_empty())            
            self.grid.place_agent(civilian, RandPlaceInArea(dis_center,dis_radius))

        for i in range(3):
            drone = Drone(i + 15, self)
            self.schedule.add(drone)
            # self.grid.place_agent(drone, self.grid.find_empty())
            self.grid.place_agent(drone, RandPlaceInArea(fob_center,fob_radius))

        uav = UAV(18, self)
        self.schedule.add(uav)
        self.grid.place_agent(uav, (0, 0))
        
        # create Zones
        zone_types = ["medical", "evacuation", "fob", "disaster"]
        # zone_types = [ "disaster", "medical", "evacuation", "fob"]
        for i, zone_type in enumerate(zone_types):
            zone = Zone(i + 19, self, zone_type)
            self.schedule.add(zone)
            # randomly places zones
            # self.grid.place_agent(zone, self.grid.find_empty()) 
            if zone_type == "disaster":
                self.grid.place_agent(zone, dis_center)
                zone_size = dis_radius
            elif zone_type == "medical": 
                self.grid.place_agent(zone,  med_center)
                zone_size = med_radius
            elif zone_type == "fob": 
                self.grid.place_agent(zone, fob_center)
                zone_size = fob_radius
            else : # corresponds to evacuatıon
                self.grid.place_agent(zone, eva_center)
                zone_size = eva_radius

            # Create ZoneCell instances
            # zone_size = 1
            # if zone_type == "disaster":
            #     zone_size = dis_radius
            zone_cells = generate_zone_cells(self, zone, zone_size)
            for zone_cell, pos in zone_cells:
                self.schedule.add(zone_cell)
                self.grid.place_agent(zone_cell, pos)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)


def RandPlaceInArea(pos,rad):
    out = (random.randint(pos[0]-rad,pos[0]+rad),
           random.randint(pos[1]-rad,pos[1]+rad))
    return out

