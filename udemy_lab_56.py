#1.  Anagram to słowa, które składają sie z tych samych liter,
# ale mające różne znaczenia np. "arbuz" >> "burza", "alergia" >> "galeria".
# Tu pobawimy się trochę anagramami.

def are_anagrams(word1, word2):
    # Remove any spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the sorted characters of both words are the same
    return sorted(word1) == sorted(word2)


# Example usage
word1 = "arbuz"
word2 = "burza"
result1 = are_anagrams(word1, word2)

word3 = "alergia"
word4 = "galeria"
result2 = are_anagrams(word3, word4)

word5 = "example"
word6 = "samples"
result3 = are_anagrams(word5, word6)

# Print the results
print(f"{word1}, {word2}, {result1}")  # arbuz, burza, True
print(f"{word3}, {word4}, {result2}")  # alergia, galeria, True
print(f"{word5}, {word6}, {result3}")  # example, samples, False

# 2. Tutaj każdą literkę wyodrębnisz i wykorzystasz oddzielnie.
# Do zmiennej q zapisz tekst "THE EYES".
# Wyświetl napis zbudowany z liter zmiennej q w kolejności: 0,1,2,5,3,7,4,6.
# Wyświetlając literki skorzystaj z print lub dodaj do siebie literki budując napis.

q="THE EYES"
new_string = q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6]
print(new_string)

#3. Tutaj użyjesz notacji, która pozwoli wyodrębnić fragment napisu rozpoczynając od określonej pozycji do końca.
# Do zmiennej q zapisz  "a gentleman" a potem wyświetl litery w kolejności 3,6,7,2,0,4,5,1,8 - do końca

a = "a gentleman"
# Reverse the string
b = a[::-1]

# Print the reversed string
print(b)

#or Using __reversed__():
# Assign the text "a gentleman" to the variable q
q = "a gentleman"
# Reverse the string using __reversed__() and join
reversed_q = ''.join(reversed(q))
# Print the reversed string
print(reversed_q)

print(b[3]+b[6]+b[7]+b[2]+b[0]+b[4]+b[5]+b[1]+b[8])

# 4. Wiesz jak z napisu  "THE MORSE CODE" zrobić tekst "HERE COME DOTS"? Gdzie się da korzystaj z notacji "od-do"
q = "THE MORSE CODE"

#HERE COME DOTS

print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])

print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])
# 5. Zostajesz zatrudniony w firmie, która wykonuje analizę oglądalności poszczególnych programów TV. Na bardzo początkowym etapie, Twój program musi przeczytać dane z pliku tekstowego z zapisanym harmonogramem poszczególnych programów. Plik zawiera linie zbudowane tak, że tytuł programu znajduje się w cudzysłowie, a kończy się napisem o:, po którym następuje godzina, np tak:
#
# 'Program "Kropka nad i" nadamy o: 22:00'
# Musisz wyodrębnić tytuł programu i godzinę o której zostanie nadany. W tym celu:
# Do zmiennej line wpisz tekst "'Program "Kropka nad i" nadamy o: 22:00'"
# Do zmiennej time wyodrębnij samą tylko godzinę (musisz poszukać znaku dwukropek i pobrać wszystkie dalsze znaki)
# Wyświetl napis time
# Do zmiennej tmp wyodrębnij fragment tekstu ze zmiennej line rozpoczynający się za znakiem cudzysłów do końca
line = 'Program "Kropka nad i" nadamy o: 22:00'

time = line[ line.find(':')+2 : ]

print(time)

tmp = line[ line.find('"')+1: ]

title = tmp [ : tmp.find('"')]
# a = line[line.find('nad')+1:]
#print (a)
print(title, time)

# Do zmiennej title wyodrębnij z tmp fragment tekstu od początku do znaku cudzysłów
# Wyświetl title i time
# To samo wykonaj dla linii
# 'Program "Pytanie na śniadanie" nadamy o: 6:00'

line = 'Program "Pytanie na śniadanie" nadamy o: 6:00'



time = line[ line.find(':')+2 : ]

print(time)



tmp = line[ line.find('"')+1: ]

title = tmp [ : tmp.find('"')]

print(title, time)