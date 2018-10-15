from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_types_linkedList = LinkedList()
for food in types:
  food_types_linkedList.insert_beginning(food)


#Write code to insert restaurant data into a data structure here. The data is in data.py
restaurants_linkedList = LinkedList()
for food in types:
  new_linkedList = LinkedList()
  for restaurant in restaurant_data:
    if restaurant[0] == food:
      new_linkedList.insert_beginning(restaurant)
  restaurants_linkedList.insert_beginning(new_linkedList)


#Write code for user interaction here
while True:
  user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()

    #Search for user_input in food types data structure here

  food_types_matched_linkedList = LinkedList()
  currentNode = food_types_linkedList.get_head_node()
  food_type = currentNode.get_value()

  if food_type.startswith(user_input):
    food_types_matched_linkedList.insert_beginning(food_type)

  while currentNode.get_next_node().get_value() != None:
    currentNode = currentNode.get_next_node()
    food_type = currentNode.get_value()
    if food_type.startswith(user_input):
      food_types_matched_linkedList.insert_beginning(food_type)

  if food_types_matched_linkedList.get_head_node().value == None:
    print("\nSorry, there is no such food here.")

  elif (food_types_matched_linkedList.get_head_node().value != None) and (food_types_matched_linkedList.get_head_node().get_next_node().value == None):
    print("\nYour only option is: \n" + food_types_matched_linkedList.stringify_list())
    user_input_2 = str(input("Do you want to look at " +  food_types_matched_linkedList.stringify_list().title() + "restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()

    while user_input_2 not in ['n', 'y']:
      user_input_2 = str(input("Do you want to look at " +  food_types_matched_linkedList.stringify_list() + "restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()
    if user_input_2 == 'n':
      continue
    elif user_input_2 == 'y':

      current_restaurants_Node = restaurants_linkedList.get_head_node()
      chosen_food_type = food_types_matched_linkedList.get_head_node().get_value()

      while current_restaurants_Node.get_next_node():

        current_one_food_type_restaurant_Node = current_restaurants_Node.get_value().get_head_node()
        restaurant_type = current_one_food_type_restaurant_Node.get_value()[0]

        if restaurant_type == chosen_food_type:

          print("\nThe {0} Restaurants in SoHo are...".format(restaurant_type.title()))

          while current_one_food_type_restaurant_Node.get_next_node():

          	availableRestaurants = current_one_food_type_restaurant_Node.get_value()
          	print("\n--------------------------\n\nName: {0} \nPrice: {1}/5 \nRating: {2}/5 \nAdress: {3}".format(availableRestaurants[1], availableRestaurants[2], availableRestaurants[3], availableRestaurants[4]))
          	current_one_food_type_restaurant_Node = current_one_food_type_restaurant_Node.get_next_node()

        current_restaurants_Node = current_restaurants_Node.get_next_node()

      user_input_3 = str(input("\nDo you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()
      while user_input_3 not in ['n', 'y']:
      	user_input_3 = str(input("\nDo you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()
      if user_input_3 == 'n':
      	break
      else:
      	continue

  else:
    print("\nYour options are: \n"  + food_types_matched_linkedList.stringify_list())
