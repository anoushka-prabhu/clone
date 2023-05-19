# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         ANOUSHKA PRABHU
# Section:      213
# Assignment:   leet speak
# Date:         11 October 2022
#

text = input("Enter some kind of text:")
words = text.split()
keys = {'a' : '4', 'e' : '3', 'o' : '0', 's' : '5', 't' : '7'}
leetlist = []
#loop for conversions
for i in words:
    for j in i :
        if j in keys :
            leetlist.append(keys.get(j))
        else:
            leetlist.append(j)
leet = ''.join(leetlist)

print('In leet speak,"' , text, '" is:', leet)
            
            
        