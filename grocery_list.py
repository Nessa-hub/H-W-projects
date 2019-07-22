#Write a python program that will capture and display a person's grocery list.
#Day 6

def user_grocery_list():
    print("Welcome to Nessa's grocery list aid")

    #input_list = []
    #while input_list != "x":
    #      input_list = input("Please enter your grocery item:" )
    #print(input_list)
    while True:
          input_string = input("Please enter your grocery item:" )
          if input_string == "x":
             break
          grocery_list = input_string.split(",")
          for item in grocery_list:
              print(item)


user_grocery_list()
