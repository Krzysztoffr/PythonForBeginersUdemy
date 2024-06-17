# Zadeklaruj zmienną helloMessage i wpisz do niej tekst: "Hello %s!"

helloMessage = 'Hello %s!'
print(helloMessage % ('Kate i Chris'))

#Zmień zawartość zmiennej helloMessage na "Hello {0:s}!"
print('''
      helloMessage4
    ''')
helloMessage4 = 'Hello {0:s}!'
helloMessage4.format('Kate i Chis 4')
print(helloMessage4.format('Kate i Chis 4'))

#Zmień zawartość zmiennej helloMessage na  "%s has %d %s"
print('''
      helloMessage5
    ''')
helloMessage5 = '%s has %d %s'
print(helloMessage5 % ('Kate', 1, 'animal'))
print(helloMessage5 % ('Chris', 100000, '$'))
print('''
      helloMessage6
    ''')
helloMessage6 = "{0:s} has {1:d} {2:s}"
print(helloMessage6.format('Kate', 1, 'animal'))
print(helloMessage6.format('Chris', 100000, '$'))
print('''
      helloMessage9
    ''')
line = "{0:20s} costs {1:6d} €"

print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))

line = '{0:s} {1:d}'
 
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))