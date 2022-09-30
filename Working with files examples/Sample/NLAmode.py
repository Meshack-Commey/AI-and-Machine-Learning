
def option():
	print('5/90')
	print('--')
	print('\b 1. Direct-1 \n 2. 2-Sure \n 3. Direct-3 \n 4. Direct-4 \n 5. Direct-5 \n 6. Perm-2 \n 7. Perm-3 \n 8. Banker')
	print('--')
	print('0. Back \n')
	
	y = int(input(' '))
	
	if y == 1:
		print('5/90')
		print('Number Position - First \n Select 1 number between 1 - 90 : ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
	
		
	elif y == 2:
		print('5/90')
		print('Select ', y,' numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	elif y == 3:
		print('5/90')
		print('Select ', y,' numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	elif y == 4:
		print('5/90')
		print('Select ', y,' numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	elif y == 5:
		print('5/90')
		print('Select ', y,' numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
	
	elif y == 6:
		print('5/90')
		print('Select 3 or more numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	elif y == 7:
		print('5/90')
		print('Select 4 or more numbers between 1 - 90 and separate each number with a space: ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	elif y == 8:
		print('5/90')
		print('Select banker number between 1 - 90 : ')
		print('--')
		print('0. Back \n ')
		x = int(input(' '))
		
	else:
		print('Invalid option!')
	
	
	






print(' Welcome to NLA 5/90')
print('--')
print('Select a game: ')
print('\b 1. Monday Special \n 2. Lucky Tuesday \n 3. Midweek \n 4. Fortune Thursday \n 5. Friday Bonza \n 6. National ')
print('--')
print('\b 9. Terms and Conditions \n \b Last draw result -')
print('\b 0. Contact us \n ')

y = int(input(' '))
if y == 1:
	Special = option()
	print(Special)
elif y == 2:
	Lucky = option()
	print(Lucky)
elif y == 3:
	Midweek = option()
	print(Midweek)
elif y == 4:
	Fortune = option()
	print(Fortune)
elif y == 5:
	Bonza = option()
	print(Bonza)
elif y == 6:
	National = option()
	print(National)
else:
	print('Invalid option!')



