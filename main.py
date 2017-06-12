# Code Names 
# Board Set Up
import random
import getpass

# Colors
W  = '\033[0m'  # white
R  = '\033[31m' # red (Team)
G  = '\033[32m' # green
O  = '\033[33m' # orange (Bystander)
B  = '\033[34m' # blue (Team)
P  = '\033[35m' # purple (Kill)

r_cnt, b_cnt, x_cnt, y_cnt = 0, 0, 0, 0
row1,row2,row3,row4,row5 = [],[],[],[],[]
matrix = [row1, row2, row3, row4, row5]

nouns = []
game_over = False

def noun_setup(dic_raw):
	with open(dic_raw) as inputfile:
		maxlen = 0
		for line in inputfile:
			nouns.append(line.strip().split('\n')[0])
			if len(line.strip().split('\n')[0]) > maxlen: # Determine longest str
				maxlen = len(line.strip().split('\n')[0])
		return maxlen

def noun_standardize(nouns, maxlen): # Make all nouns save str length
	counter = 0
	for item in nouns:
		white = 0
		if len(item) < maxlen: # If item is less than largest string
			white = maxlen-len(item)
			nouns[counter] = item+(" "*white) # Filling in additional whitespace
		counter += 1

def print_matrix(m):
	print "="*max_len_noun*6 # Arbitary, as long as it covers the whole board
	for row in m:
		print
		print('\t'.join([str(x) for x in row]))
		print
	print "="*max_len_noun*6

# Import Dictionary and Standardize Words
max_len_noun = noun_setup('dictionary') # Open file
noun_standardize(nouns, max_len_noun) # Add white space for uniform board

# Game Board Randomizer Set Up
for row in matrix:
	for i in range(0,5):
		rand = random.randint(0, len(nouns)-1)
		row.append(nouns[rand])
		nouns.pop(rand) # Prevents Repeat letters

print "Code Master study this!"
print_matrix(matrix)

print "Legend:"
print (R+"\tR = Red Word "+W), "8 (or 9) occurances, depending on who is first"
print (B+"\tB = Blue Word"+W), "8 (or 9) occurances, depending on who is first"
print (P+"\tX = Kill Word"+W), "1 occurance"
print (O+"\tY = Bystander"+W), "7 occurances"

print "Enter in this format. Case Insensitive. Example:"
print "\t1:\tYYYBR"
print "\t2:\tBYBYR"
print "\t3:\tBYXRB"
print "\t4:\tBBYBR"
print "\t5:\tRBRRR"

print "There is only 5 letters per row"
print "Code Master: Enter Row Key"

key_matrix = []
key_dict = {}

valid = False
while (valid != True):
	row_ctr = 1

	#'''	
	for row in matrix:
		rawdata = getpass.getpass(str(row_ctr)+": ")

		while rawdata.isalpha() == False:
			print "Invalid Input, must only be alphas R, B, X, and Y"
			rawdata = getpass.getpass(str(row_ctr)+": ")
		rawdata = rawdata.upper()

		while len(rawdata) != 5:
			print "Invalid Row Length (Needs to be 5)"
			rawdata = getpass.getpass(str(row_ctr)+": ")

		invalid = True
		while invalid:
			for letter in rawdata:
				if letter == 'R':
					r_cnt += 1
				elif letter == 'B':
					b_cnt += 1
				elif letter == 'X':
					x_cnt += 1
				elif letter == 'Y':
					y_cnt += 1
				else:
					rawdata = getpass.getpass(str(row_ctr)+": ")
			invalid = False # Break

		key_matrix.append(list(rawdata))
		print "Row Accepted"
		#print key_matrix
		row_ctr += 1
	'''
	################## BEGIN DELETE AFTER TESTING ##################
	key_matrix = [['Y', 'Y', 'Y', 'B', 'R'], 
				  ['B', 'Y', 'B', 'Y', 'R'], 
				  ['B', 'Y', 'X', 'R', 'B'], 
				  ['B', 'B', 'Y', 'B', 'R'], 
				  ['R', 'B', 'R', 'R', 'R']]
	r_cnt = 8
	b_cnt = 9
	x_cnt = 1
	y_cnt = 7
	################### END DELETE AFTER TESTING ###################
	'''
	if ((r_cnt == 8 and b_cnt == 9) or (r_cnt == 9 and b_cnt == 8)) and x_cnt == 1 and y_cnt == 7:
		print G+"Successful and valid board!"+W
		print "\n" + "*"*max_len_noun*6

		for row in range(0,5):
			for col in range(0,5):
				spaceless_key = matrix[row][col]
				if " " in matrix[row][col]:
					spaceless_key = matrix[row][col].replace(" ", "")

				key_dict[spaceless_key] = key_matrix[row][col]
				# All nouns are labeled with corresponding roles
		valid = True

	else:
		print "Invalid Board, Try again."
		print "\tR", r_cnt, "\t 8 or 9"
		print "\tB", b_cnt, "\t 8 or 9"
		print "\tX", x_cnt, "\t 1"
		print "\tY", y_cnt, "\t 7"

# Set up complete #
#################################################################################
#print "!!!!! THIS IS THE KILL WORD: ", key_dict.keys()[key_dict.values().index('X')], "!!!!!"

turn = ""

if b_cnt == 9:
	print (B+"Blue Team Begins First"+W)
	turn = "blue"

elif r_cnt == 9:
	print (R+"Red Team Begins First"+W)
	turn = "red"
print 

user_entries = set()

def round(team, clue_num, of_clues, round_num, clue_name):
	#Print team and round number
	#print clue number
	#get input
	#color the matrix
	#reduce cnt's

	global r_cnt
	global b_cnt
	global x_cnt
	global y_cnt

	if team == "blue":
		print(B+"Blue Team's Turn"+W)
	elif team == "red":
		print(R+"Red Team's Turn"+W)
	print "Round #", round_num
	print "Clue", clue_num, "of", of_clues, "("+clue_name.title()+")"


	print "Current Board"
	print_matrix(matrix)

	rawdata = raw_input("Code Word: ")
	while rawdata.isalpha() == False:
		print "Input is not a valid string."
		rawdata = raw_input("Code Word: ")

	while rawdata.title() not in key_dict.keys():
		print "Input is not one of the provided code words."
		rawdata = raw_input("Code Word: ")

	while rawdata.title() in user_entries:
		print "Input has been revealed already. Pick a new code word."
		rawdata = raw_input("Code Word: ")

	rawdata = rawdata.title()
	early_eject = False
	game_over = False
	end_turn = False
	for row in range(0,5):
		for col in range(0,5):
			white_space = matrix[row][col].count(" ")
			spaceless = matrix[row][col].replace(" ", "")
			if rawdata == spaceless:
				allegiance = key_dict[spaceless]

				if allegiance == 'R':
					color = R
					r_cnt -= 1
					if team == "red":
						end_turn = False	# Red Team Guessed Correctly
					else:
						end_turn = True		# Blue Team chose Red Card
				elif allegiance == 'B':
					color = B
					b_cnt -= 1
					if team == "blue":
						end_turn = False	# Blue Team Guessed Correctly
					else:
						end_turn = True		# Blue Team chose Red Card
				elif allegiance == 'X':		# KILL WORD
					color = P
					game_over = True
					x_cnt = 0
				elif allegiance == 'Y':
					color = O
					y_cnt -= 1
					end_turn = True			# Team chose incorrectly

				matrix[row][col] = (color+rawdata+W)+(" "*white_space)
				#print (color+rawdata+W)
				#print_matrix(matrix)
				user_entries.add(rawdata)
				early_eject = True
				break

		if early_eject:
			print_matrix(matrix)
			break
	return (game_over, end_turn)

word_count = 1
loss_type = ""
win = True
while word_count <= 25 or b_cnt != 0 or r_cnt != 0 or x_cnt != 0 or game_over == False:

	if turn == "blue":
		user_inp_clue = raw_input(B+"Blue Team\nProvide a Clue: "+W)
		while user_inp_clue.title() in key_dict.keys() or " " in user_inp_clue or "-" in user_inp_clue:
			if " " in user_inp_clue or "-" in user_inp_clue:
				print "A clue must be only one word"
			else:
				print "The clue you provided is a word on the board. No cheating!"
			user_inp_clue = raw_input(B+"Blue Team\nProvide a Clue: "+W)
		num_clues = raw_input(B+"Clue Number: "+W)

	elif turn == "red":
		user_inp_clue = raw_input(R+"Red Team\nProvide a Clue: "+W)
		while user_inp_clue.title() in key_dict.keys() or " " in user_inp_clue or "-" in user_inp_clue:
			if " " in user_inp_clue or "-" in user_inp_clue:
				print "A clue must be only one word"
			else:
				print "The clue you provided is a word on the board. No cheating!"
			user_inp_clue = raw_input(R+"Red Team\nProvide a Clue: "+W)
		num_clues = raw_input(R+"Clue Number: "+W)


	while num_clues.isdigit() == False or "." in num_clues or int(num_clues) < 1 or int(num_clues) > 9:
		if num_clues.isdigit() == False or "." in num_clues:
			print "Entry is not a pure integer. Do not enter alphas or floats."
			num_clues = raw_input("Clue Number: ")
		elif int(num_clues) < 1 or int(num_clues) > 9:
			print "Number of clues must be in the range 1 through 9, inclusive"
			num_clues = raw_input("Clue Number: ")

	num_clues = int(num_clues)

	print "-"*max_len_noun*6
	round_result_GO = False
	round_result_ET = False

	# For loop will allow a certain # of guesses.
	for clue in range(1,int(num_clues)+1):
		# Team, Clue #, total clues, Round #
		round_result_GO, round_result_ET = round(turn, clue, num_clues, word_count, user_inp_clue)
		print "Blue Code Words Left", b_cnt
		print "Red Code Words Left", r_cnt
		if round_result_ET:
			print "Sorry! Wrong choice. Wait for the next round!"
		if word_count >= 25 or round_result_GO == True or round_result_ET == True or b_cnt == 0 or r_cnt == 0:
			break
		print 
		word_count += 1

	if word_count >= 25:
		loss_type = R+"Game Over, Exhausted all words!"+W
		print loss_type
		print P+turn.title()+" Team Loses"+W
		win = False
		break
	elif round_result_GO == True:
		loss_type = R+"Game Over, Kill Word Activated!"+W
		print loss_type
		print P+turn.title()+" Team Loses"+W
		win = False
		break
	elif b_cnt == 0:
		print R+"Red Team Loses!"+W
		loss_type = "***** Blue Team Wins! *****"
		print B+loss_type+W
		break
	elif r_cnt == 0:
		print B+"Blue Team Loses!"+W
		loss_type = "Red Team Wins!"
		print R+loss_type+W
		break
	print "-"*max_len_noun*6

	# Toggle Turns
	if turn == "blue":
		turn = "red"
	elif turn == "red":
		turn = "blue"