#reference Zybooks 8.24 LAB: Program: Soccer team roster (Dictionaries)

# This program will store roster and rating information for a soccer team. 
# Coaches rate players during tryouts to ensure a balanced team.
# (1) Prompt the user to input five pairs of numbers: 
#     A player's jersey number (0 - 99) and the player's rating (1 - 9). 
#     Store the jersey numbers and the ratings in a dictionary. 
#     Output the dictionary's elements with the jersey numbers in ascending order 
#     (i.e., output the roster from smallest to largest jersey number).
#      Hint: Dictionary keys can be stored in a sorted list. 
#(2) Implement a menu of options for a user to modify the roster. 
#    Each option is represented by a single character. 
#    The program initially outputs the menu, and outputs the menu after a user chooses an option.
#    The program ends when the user chooses the option to Quit.
#     For this step, the other options do nothing
#(3) Implement the "Output roster" menu option.
#(4) Implement the "Add player" menu option. Prompt the user for a new player's jersey number and rating.
#    Append the values to the two vectors.
#(5) Implement the "Delete player" menu option. 
#    Prompt the user for a player's jersey number. 
#    Remove the player from the roster (delete the jersey number and rating).
#(6) Implement the "Update player rating" menu option. Prompt the user for a player's jersey number. 
#    Prompt again for a new rating for the player, and then change that player's rating
#(7) Implement the "Output players above a rating" menu option. Prompt the user for a rating.
#    Print the jersey number and rating for all players with ratings above the entered value.

soccer_team = {}
menu_op = ''

for i in range(1, 6):
   jersey_num = int(input('Enter player {}\'s jersey number:\n'.format(i)))
   rating_num = int(input('Enter player {}\'s rating:\n'.format(i)))
   soccer_team[jersey_num] = rating_num
   print('')

list_of_jersey_nums = sorted(list(soccer_team.keys()))

print('ROSTER')
for i in list_of_jersey_nums:
   print('Jersey number: {}, Rating: {}'.format(i, soccer_team[i]))

while menu_op != 'q':
   print('\nMENU')
   print('a - Add player')
   print('d - Remove player')
   print('u - Update player rating')
   print('r - Output players above a rating')
   print('o - Output roster')
   print('q - Quit\n')
   
   menu_op = input('Choose an option:\n')
   
   if menu_op == 'a':
      jersey_num = int(input('Enter a new player\'s jersey number: \n'))
      rating_num = int(input('Enter the player\'s rating: \n'))
      soccer_team[jersey_num] = rating_num
   
   elif menu_op == 'd':
      jersey_num = int(input('Enter a jersey number: \n'))
      del soccer_team[jersey_num]
      
   elif menu_op == 'u':
      jersey_num = int(input('Enter a jersey number: \n'))
      rating_num = int(input('Enter a new rating for player: \n'))
      soccer_team[jersey_num] = rating_num
   
   elif menu_op == 'r':
      rating_num = int(input('Enter a rating: \n'))
      list_of_jersey_nums = sorted(list(soccer_team.keys()))
      
      print('ABOVE', rating_num)
      for i in list_of_jersey_nums:
         if soccer_team[i] > rating_num:
            print('Jersey number: {}, Rating: {}'.format(i, soccer_team[i]))
      
   elif menu_op == 'o':
      list_of_jersey_nums = sorted(list(soccer_team.keys()))
      print('ROSTER')
      for i in list_of_jersey_nums:
         print('Jersey number: {}, Rating: {}'.format(i, soccer_team[i]))


