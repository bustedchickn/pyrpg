# Use the hashtag button to make a comment
escape = ""


'''
Comments help you see what is happening in the code
This is a multiline comment in python
'''

# Main game loop
while(escape != "yes"):
    print("This is the location you are in.")
    choice = input("Do you want to go right or left?")
    if(choice== "right"):
        print("You see a green goblin.")
        choice = "left"
    else:
        print("You see a lighthouse.")



    escape = input("Do you want to quit?")
