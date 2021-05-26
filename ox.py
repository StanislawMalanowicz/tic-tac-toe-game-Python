from random import randint

winning_patterns = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6],
]

def show_main_msg():
	print('***********************************************\n')
	print('Witaj w ostatecznym turnieju w Kółko i Krzyżyk!\n')
	print('Nasza plansza wygląda nastepująco:')
	print("""
		0 | 1 | 2
		_________
		3 | 4 | 5
		_________
		6 | 7 | 8
		""")

def choose_figure():
	choice = input('Chcesz grać kółkiem (O) czy krzyżykiem (X)?')
	while choice not in ['X', 'O']:
		print('Zdecyduj się!')
		choice = input('Kołko (O) czy krzyżyk (X)?')
	return choice

def choose_comp_figure(human):
	if human == 'X':
		comp = 'O'
	else:
		comp = 'X'
	return comp

def who_is_first():
	first = randint(0,1)
	if first == 0:
		print('Ty zaczynasz')
	elif first == 1:
		print('Komputer zaczyna')
	return first

def show_current_table(table):
	print(f"""
		{table[0] or 0} | {table[1] or 1} | {table[2] or 2}
		_________
		{table[3] or 3} | {table[4] or 4} | {table[5] or 5}
		_________
		{table[6] or 6} | {table[7] or 7} | {table[8] or 8}
		""")

def move_is_legal(table, value):
	if table[value] == "X" or table[value] ==  "O":
		print(value, " it's unlegal")
		return False
	else:
		# print(value, " it's legal")
		return True

def human_plays(table, human):
	value = int(input('Gdziesz chcesz?'))
	legal = move_is_legal(table, value)
	while not legal:
		value = int(input('Ruch nieprawidlowy, Gdziesz chcesz?'))
		legal = move_is_legal(table, value)
	table[value] = human
	return table

def comp_plays(table, comp):
	# print("comp: ", table)
	center = 4
	bestChoose =[0,2,6,8]
	if table[center] == None:
		table[center] = comp
		return table
	
	for nr in bestChoose:
		if table[nr] == None:
			table[nr] = comp
			return table

	value = randint(0,8)
	legal = move_is_legal(table, value)
	# print("table before check: ", table)
	while not legal:
		value = randint(0,8)
		legal = move_is_legal(table, value)
	table[value] = comp
	# print("table after check: ", table)
	return table

def pick_winner(table):
	# print("pick a winner works")
	X_list = []
	O_list = []
	for i,el in enumerate(table):
		if el == 'X':
			X_list.append(i)
		elif el == "O":
			O_list.append(i)
			
	whoWin = ""
	for patern in winning_patterns:
		if(all(item in X_list for item in patern)):
			print(" X win")
			whoWin = "X"
			break
		elif(all(item in O_list for item in patern)):
			print(" o win")
			whoWin = "O"
			break
		else:
			whoWin = None
	print("who win? ", whoWin)
	return whoWin


def display_final_msg(winner, comp, human):
	if human == winner:
		print(f"Wygrales grajac: {human}")
	if comp == winner:
		print(f"Przegrales, komp gral: {comp}")
	


def play():
	show_main_msg()
	human = choose_figure()
	comp = choose_comp_figure(human)
	print(f'Zatem grasz {human}, a ja gram {comp}')
	next_player = who_is_first()
	table = [None, None, None, None, None, None, None, None, None]
	winner = None
	while not winner:
		show_current_table(table)
		if next_player == 0:
			table = human_plays(table, human)
			next_player = 1
		elif next_player == 1:
			table = comp_plays(table, comp)
			next_player = 0
		winner = pick_winner(table)
		# print("winner is: ", winner)
	display_final_msg(winner, comp, human)


play()


