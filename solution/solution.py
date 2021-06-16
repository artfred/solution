import random #-----------> import a random number generator

f_g = [] #----------> first group
s_g = [] #----------> second group
t_g = [] #----------> third group

len_fg = len(f_g) #----------> to get the lenght of the  first group
len_sg = len(s_g) #----------> to get the lenght of the  second group
len_tg = len(t_g) #----------> to get the lenght of the  third group

board_row = len_fg + len_sg + len_tg #----------> to see if the board is already filled  with letters

x_win = "" #----------> to know if the x win
o_win = "" #----------> to know if the o win
x_win_list = 0 #----------> to hold the number of x wins
o_win_list = 0 #----------> to hold the number of o wins

for i in range(10): #----------> to run the game for 10 times
    while board_row < 9: #----------> if the board is not yet filled with letters it keep on picking numbers and the will be use to get a letter from the letters collection
        try:
            len_fg = len(f_g) #----------> again it checks the letters in the first group
            len_sg = len(s_g) #----------> again it checks the letters in the second group
            len_tg = len(t_g) #----------> again it checks the letters in the third group

            board_row = len_fg + len_sg + len_tg #----------> again to see if the board is already filled  with letters

            letters = [] # this is the variable or basket to hold the collection of letters, it only accept letter "x" or "o"

            for i in range(300):  # this is the source of letters, THIS IS HOW IT LOOKS LIKE. THE WORK BELOW IS THE OUTPUT OF THIS line of code.
                                  #  i simply generate a random number and picked a letter from this list of characters
                # ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O',
                #  'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', '
                #  X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', '
                #  X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O',
                #   'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #   'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #   'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #   'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O',
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 
                #    'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', '
                #    X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
                for i in 'XO':
                    letters.append(i)


            total_num = len(letters) # to get the length of the letters that was generated
            picked_number = random.randint(0,total_num) # i picked a  number, the limit of the choices is based to the length of the letters collection "letters = []"
            print('picked number'+str(picked_number)) #i simply display the picked number, to see that the random number is working and its not picking the same number
            picked_letter = letters[picked_number]  # i picked a  letter
            print('picked letter '+picked_letter) #i simply display the picked letter, to see that the picked letter is not the same from previous picked.

            if picked_number < 100: # if the picked number is less than 100, if just put the picked letter to the first group
                if len_fg == 3: # if the first group is already filled with letters it will not accept adding a letters
                    pass
                else:
                    f_g.append(picked_letter)
            elif picked_number > 100: # if the picked number is greater than 100, if just put the picked letter to the second group
                if len_sg == 3: # if the second group is already filled with letters it will not accept adding a letters
                    pass
                else:
                    s_g.append(picked_letter)
            else: # if the picked number is not less than 100 and not greater than 200, if simply added the picked letter to third group
                if len_tg == 3: # if the third group is already filled with letters it will not accept adding a letters
                    pass
                else:
                    t_g.append(picked_letter)

            fg_1 = f_g[0] #this block of codes simply to see who wins in a first group
            fg_2 = f_g[1]
            fg_3 = f_g[2]
            if fg_1 == fg_2:
                if fg_2 == fg_3:
                    if fg_3 == "X":
                        x_win = "yes"
                    else:
                        o_win = "yes"
            else:
                pass


  
            tg_1 = t_g[0] #this block of codes simply to see who wins in a second group
            tg_2 = t_g[1]
            tg_3 = t_g[2]
            if tg_1 == tg_2:
                if tg_2 == tg_3:
                    if tg_3 == "X":
                        x_win = "yes"
                    else:
                        o_win = "yes"
            else:
                pass


            fg_1 = f_g[0] #this block of codes simply to see who wins in a first group
            fg_2 = f_g[1]
            fg_3 = f_g[2]
            if fg_1 == fg_2:
                if fg_2 == fg_3:
                    if fg_3 == "X":
                        x_win = "yes"
                    else:
                        o_win = "yes"
            else:
                pass





                
        except:
            pass

    print(f_g)
    print(s_g)
    print(t_g)
    print('-----------------------------------'+str(i))
    if x_win == "yes":
        x_win_list += 1
        print('--------------------X win------')
    elif o_win == "yes":
        print('--------------------O win------')
        o_win_list += 1
    else:
        pass
    print('')


print("X wins "+str(x_win_list)+" out of 10")
print("O wins "+str(o_win_list)+" out of 10")




val = input("Enter any keys and press enter to exit: ") 

print('test')