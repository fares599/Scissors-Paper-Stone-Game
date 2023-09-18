import random
from rich.console import Console
from rich.table import Table
import pyfiglet as pf
import time
from rich import print
import termcolor 

figleted_text=pf.figlet_format(text="Fares  Software")

print()
print(figleted_text)
print()
s='''hello there how are you we are
so happy to be with us in
our simple game rock paper and scissers
the rules are so simple 
*you choose a number between (1,3)
	- if you choose 1 it refer to rock (Rock=1)
	- if you choose 2 it refer to paper (Paper=2)
	- if you choose 3 it refer to rock (scissors=3)
*press enter or write x to end your game

Warrning :=> please if you do any thing else like :
	
	-pressing any other thing the game will end
Have fun ^___^
'''.title()

for letter in s:
	print(letter,end="",flush=True)
	time.sleep(0.02) 



accomulative_user_result=[0]
accomulative_computer_result=[0]
while True :
	try:	
		time.sleep(0.5)
		l="-"*76
		for i in l:
			print(i,end="",flush=True)
			time.sleep(0.02)
			time.sleep(0.01)

		print("")
		print("[green]To Exit The Game   ( Exit =  [yellow]x[/yellow]  Or  [yellow]Enter[/yellow])[/green]  ")
		print("Rock =[cyan] 1[/cyan]\nPaper =[cyan]2[/cyan]\nScissors = [cyan]3[/cyan] \n")
		user__choice=input("Your Choice : ")
		if user__choice == "x" or user__choice == "":
			print()
			print(pf.figlet_format(text="Game  Over"))
			input("press Enter")
			break

		user_choice = int(user__choice)


		assert any([user_choice==1,user_choice==2,user_choice==3])

	except AssertionError:
		print(f"[red]You Entered An Inapropriate Value Out Of Range Choose 1 or 2 or 3[/red] ")
		break
	

		


	computer_choice = random.randint(1,3)


	choice=["Rock" ,"Paper"," Scissors"]


	# Draw

	computer_score=1
	user_score=1

	if user_choice == computer_choice:
		# computer_score=computer_score
		# user_score=user_score

		result="Draw"

	# user win 
	elif any([ user_choice==1 and  computer_choice==3, user_choice==3 and  computer_choice==2, user_choice==2 and  computer_choice==1]):

		
		accomulative_user_result.append(user_score)

		result=  "You Win"


	#computer win
	else:
		
		accomulative_computer_result.append(computer_score)

		result= "Computer Win"


	game_graphics = [

	'''           _______
	---'   ____)
	      (_____)
	      (_____)
	      (____)
	---.__(___)'''
	,
	
	'''       _________
	---'     ____)____
	           ______)
	          _______)
	         _______)
	---.__________)'''
	,
	'''     _____
	---'  ____)_______
	          _________)
	       _____________)
	      (____)
	---.__(___)'''
	]



	header=Table(title="The Game ")
	footer=Table()

	header.add_column("            Your Choice           ",justify="center",style="cyan")
	header.add_column("          Computer Choice         ",justify="center",style="cyan")
	

	header.add_row(f"You Choose {choice[user_choice-1]}",f"Computer Choose {choice[computer_choice-1]}")
	header.add_row(game_graphics[user_choice-1] ,game_graphics[computer_choice-1])
	

	footer.add_column("Your Score",justify="center",style="green")
	footer.add_column("Computer score",justify="center",style="cyan")
	footer.add_column("Who Win",justify="center",style="cyan")
	footer.add_row(f"{sum(accomulative_user_result)} ",f"{sum(accomulative_computer_result)} " , f"{result:^{len(result)+6}s}")

	console=Console()


	console.print(header)
	console.print(footer)
	











