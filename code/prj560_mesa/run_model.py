from model import SearchAndRescueModel

model = SearchAndRescueModel(width=10, height=10)

for i in range(10):  # Run the model for 10 steps
    model.step()
