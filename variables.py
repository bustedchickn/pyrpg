my_list = [0,1,2,3,4]
my_set = {"bob","talmage","james"}
my_int = 21
my_dictionary = {"Hyrum": 20,"Talmage": my_int}
my_string = ""
my_float = 1.2


# print(my_list)
# print(my_list[3])
# print(my_dictionary["Talmage"])

# print(f"{type(my_int)} is the data type of my_int")



class player():
    def __init__(self, name):
        self.name = name
        self.health = 3

    def attack(self):
        #do the attack stuff here
        print(f"{self.name} attacks")

def my_function():
    #put the code to run here
    pass

player1 = player("Bob")
print(f"the first player is {player1.name}")
player1.attack()