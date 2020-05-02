filename = input('Ukajite fail: ') #Ukazat text.txt ili kakoy u vas txt fail 
file = open(filename, 'r')
print('V dannom file ' + str(len(file.read())) + ' simvolov')
file = open(filename, 'r')
strok = 0
words = 0
letters = 0

for item in file:
    strok += 1
    letters += len(item)
    words += len(item.split())


print('Strok: ', strok)
print('Slov: ', words)
print('Bukv: ', letters)


file.close()
