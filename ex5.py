name = 'Zed A. Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

metric_height = height * 2.54
metric_weight = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches or {metric_height} cms tall")
print(f"He's {weight} pounds or {metric_weight} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usualy {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
