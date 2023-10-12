# Define a list of values
values = ["Hello", "World"]

hello_values = []
world_values = []

for value in values:
    if "Hello" in value:
        hello_values.append(value)
    elif "World" in value:
        world_values.append(value)

print("Hello Values:", hello_values)
print("World Values:", world_values)


