# a = input('vedite slovo: ')
# filename = input('viberite ofice google: ')
# file = open(filename, 'a+')
# file.write(input('vedite jalobu: '))
# file.close()

#2sposob with open
a = input('vedite slovo: ')
filename = input('viberite ofice google: ')
with open(filename, 'a+') as file:
    file.write(input('vedite jalobu: '))


