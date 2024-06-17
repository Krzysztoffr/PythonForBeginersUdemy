# 1. Zadeklaruj zmienną name i przypisz do niej swoje imie
name = 'Peter'
# 2. Zadeklaruj zmienną age i przypisz do niej wiek
age = 25
# 3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365
daysInYear = 365
# 4. Zadeklaruj zmienną message i przypisz jej wartość jak poniżej. 
# Uwaga w miejscu ??? należy umieścić znaczniki pozwalające na wyświetlenie kolejno napisu i dwóch liczb
print('4')
message = '%s is %d years old, so is about %d days old'
print(message % (name, age, age * daysInYear))
# '??? is ??? years old, so is about ??? days old' 

# 5. Wyświetl informację jak poniżej (wykorzystaj funkcje formatowania napisów)j:
print('5')
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, age * daysInYear))

# Jan is 26 years old, so is about 9490 days old 
name = 'Jan'
age = 26
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))
# 6. Zmień imie i wiek w zmiennych name i age i jeszcze raz wyświetl komunikat korzystając z tej samej instrukcj co poprzednio
print('6')
name = 'Anna'
age = 30
print(message.format(name, age, age * daysInYear))
# 7. Zmień wartość zmiennej message na:
print('7')
# message = '{???} is {???} years old, so is about {???} days old' 
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
# Ponownie w miejscu ??? należy umieścić odpowiednie napisy formatujące pozwalające wyświetlić napis i 2 liczby
print(message.format(name,age,age*daysInYear))


# 8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:
# Chris is 17 years old, so is about 6205 days old
print('8')
name = 'Chris'
age = 17
daysInYear = 365
message8 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message8.format(name,age,age*daysInYear))

# 9. Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:
# Wynik powinien wyglądać tak:
# 1234567890 divided by 12345 is  100005 and the rest is 6165
print('9')
print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)