# Elise Harper

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

print('Hello Friend!')
# Greets user in English
print('Please choose a language by typing a number')
print('1. Spanish')
print('2. Italian')
print('3. French')
# I put the print commands on separate lines for formatting purposes. 
myLanguage = input()
# I assigned whatever the user types in to myLanguage 
if myLanguage == '1':
        print('Hola! Como estas?')
#This message is displayed in Spanish if the user entered 1
elif myLanguage == '2':
        print('Ciao, come stai')
#This message is displayed in Italian if the user entered 2
elif myLanguage == '3':
        print('Salut comment allez-vous')
#This message is displayed in French if the user entered 3

else:
        print('Have a nice day!')
#If the user puts something other than 1, 2 or 3 then it will write this
exit()
#exits the program



