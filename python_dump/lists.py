num = [1, 2, 3]
print(num)
print(num[2])
print(num + [4, 5, 6])
num[0] = 0
print(num)
num.append(7) # sowie stringbuilder
num.append(4 * 2)
print(num)

letters = ['a', 'b', 'c', 'd' , 'e', 'f']
print(letters)
print('Length: ', len(letters))
letters[0:3] = ['A', 'B', 'C'] # von 0 - 2 werte ersetzt
print(letters)
letters[3:5] = [] # werte gelöscht
print(letters)
print('Length: ', len(letters))
letters[:] = [7] # ganze liste wurde durch 7 eingetauscht
print(letters)
print('Length: ', len(letters))

numlist = [1, 2, 3, 4, 5]
letlist = ['a', 'b']
list = [numlist, letlist]
print(list)
print(list[1]) # gibt die buchstaben zurück
print(list[0][2]) # gibt von der ersten menge den wert an psoition 2 zurück
print(len(list)) # = 2. weil nur 2 elemente!