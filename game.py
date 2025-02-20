import random
# Use the hashtag button to make a comment
escape = ""


'''
Comments help you see what is happening in the code
This is a multiline comment in python
'''


class Location():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def set_connections(self, connections):
        self.connections = connections
        


'''
This is for a bunch of variables
'''

forest = Location("forest","A scary, evil forest.")
cave = Location("cave","A dark, damp cave.")
castle = Location("castle","A regal castle.")
city = Location("city","A busy city.")

print(forest.name)

#We are going to use a dictionary
locations = {"forest" : Location("forest","A scary, evil forest."),
"cave" : Location("cave","A dark, damp cave."),
"castle" : Location("castle","A regal castle."),
"city" : Location("city","A busy city.")}



forest.set_connections([castle,city,cave])
castle.set_connections([forest,city])
city.set_connections([forest,castle])
cave.set_connections([forest])

for connection in forest.connections:
    print(connection.description)













class Dice():
    def __init__(self, sides):
        self.number_of_sides = sides
    def roll(self):
        print(random.randint(1,self.number_of_sides))


D20 = Dice(20)
D20.roll()

D6 = Dice(6)
D6.roll()
    


locations = [forest,castle]

for location in locations:
    input(location.description)

dice_list = []
for i in range(4,20):
    die = Dice(i)
    # die.roll()
die.roll()




# Main game loop
# while(escape != "yes"):
#     print("This is the location you are in.")
#     choice = input("Do you want to go right or left?")
#     if(choice== "right"):
#         print("You see a green goblin.")
#         choice = "left"
#     else:
#         print("You see a lighthouse.")



#     escape = input("Do you want to quit?")
