import getpass
import string
import os

# creatinga lists of users, their PINs and bank statements

users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

# while loop checks existance of the enterd username

while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('INVALID USERNAME')

# comparing pin

while count < 3:
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	
	if pin.isdigit():
	# For User1	
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
	# For User2
		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
	# For user3			
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
	else:
		print('PIN CONSISTS OF 4 DIGITS')
		count += 1
	
# in case of a valid pin- continuing, or exiting

if count == 3:
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	exit()

print()
print('LOGIN SUCCESFUL, CONTINUE')
print()
print(str.capitalize(users[n]), 'Welcome To Pochinki')
print('----------ATM SYSTEM-----------')

# Main menu

while True:
	
	#os.system('clear')
	print()
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()

	valid_responses = ['s', 'w', 'l', 'p', 'q']
	
	response = response.lower()
	
	#(FOR STATEMENT)
	
	if response == 's':
		print(str.capitalize(users[n]), 'YOU HAVE :', amounts[n],',RUPEE ON YOUR ACCOUNT.')
	
	#(FOR WITHDRAW)
	
	elif response == 'w':
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		
		if cash_out%100 != 0:
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 RUPEE NOTES')
		
		elif cash_out > amounts[n]:
			print('YOU HAVE INSUFFICIENT BALANCE')
		
		else:
			amounts[n] = amounts[n] - cash_out
			print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEE')
	
	#(FOR LODGEMENT)
	
	elif response == 'l':
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print()
		
		if cash_in%100 != 0:
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 100 RUPEE NOTES')		

		else:
			amounts[n] = amounts[n] + cash_in
			print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEE')
	
	#(FOR CHANGING PIN)
	elif response == 'p':
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			
			if new_ppin != new_pin:
				print('PIN MISMATCH')
				print()
			
			else:
				pins[n] = new_pin
				print()
				print('NEW PIN SAVED')
				
		else:
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
	
	#(FOR EXITING)
	elif response == 'q':
		print("$$ THANKS FOR CHOOSING OUR BANK $$")
		exit()	
		

	else:
		print('RESPONSE NOT VALID')		

