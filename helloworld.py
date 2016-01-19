# Elise Harper

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

print('Hello Friend!')
print('Please choose a language')
print('1. Spanish')
print('2. Italian')
print('3. French')
# I put the print commands on separate lines for formatting purposes. Not sure if there's an easier way to do that.
myLanguage = input()
# I assigned whatever the user types in to myLanguage with the 3 different outcomes
if myLanguage == 'Spanish':
        print('Hola! Como estas?')
if myLanguage == 'Italian':
        print('Ciao, come stai')
if myLanguage == 'French':
        print('Salut comment allez-vous')
        

