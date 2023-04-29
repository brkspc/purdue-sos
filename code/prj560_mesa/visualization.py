from model import SearchAndRescueModel, SAR, Civilian, Drone, UAV, ZoneCell, Zone


from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    if isinstance(agent, SAR):
        portrayal = {"Shape": "circle",
                     "Color": "blue",
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5}
    elif isinstance(agent, Civilian):
        if agent.dead:
            color = "black"
        elif agent.wounded:
            color = "red"
        else:
            color = "green"

        portrayal = {"Shape": "circle",
                     "Color": color,
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5}
    elif isinstance(agent, Drone):
        portrayal = {"Shape": "circle",
                     "Color": "orange",
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5}
    elif isinstance(agent, UAV):
        portrayal = {"Shape": "circle",
                     "Color": "purple",
                     "Filled": "true",
                     "Layer": 1,
                     "r": 0.5}
    elif isinstance(agent, ZoneCell):
        if agent.zone_type == "medical":
            color = "pink"
        elif agent.zone_type == "evacuation":
            color = "yellow"
        elif agent.zone_type == "fob":
            color = "cyan"
        elif agent.zone_type == "disaster":
            color = "grey"
            
        portrayal = {"Shape": "rect",
                     "Color": color,
                     "Filled": "true",
                     "Layer": 0,
                     "w": 1,
                     "h": 1,
                     "Alpha": 0.5}

    elif isinstance(agent, Zone):
        if agent.zone_type == "medical":
            color = "pink"
        elif agent.zone_type == "evacuation":
            color = "yellow"
        elif agent.zone_type == "fob":
            color = "cyan"
        elif agent.zone_type == "disaster":
            color = "grey"

        portrayal = {"Shape": "rect",
                     "Color": color,
                     "Filled": "true",
                     "Layer": 3,
                     "w": 1,
                     "h": 1,
                     "text": agent.zone_type.upper()+" zone",
                     "text_color": "black",
                     "text_size": 5,
                     "LineWidth": 3,
                     "OutlineColor": "black"}
    return portrayal

# make the area definition parametric
areaWidth = 30
areaHeight = 20


grid = CanvasGrid(agent_portrayal, areaWidth, areaHeight, areaWidth*25, 
                  areaHeight*25)

chart = ChartModule([{"Label": "Survivors",
                      "Color": "green"}],
                    data_collector_name='datacollector')
chart_dead = ChartModule([{"Label": "Dead",
                           "Color": "black"}],
                         data_collector_name='datacollector')
server = ModularServer(SearchAndRescueModel,
                       [grid, chart,chart_dead],
                       "Search and Rescue Model",
                       {"width": areaWidth, "height": areaHeight})

server.launch()
