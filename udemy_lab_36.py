quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quote.upper()
# lub
print(quote.upper())

quote.lower()
#lub
print(quote.lower())

quote.endswith('street')
#lub
print(quote.endswith('street'))



quote.isupper()
#lub
print('quote.isupper:') 
print(quote.isupper())



quote.upper().isupper()
#lub
print(quote.upper().isupper())



quote.find('one')
#lub
print(quote.find('one'))



quote.replace('one', '1')
#lub
print(quote.replace('one','1'))

      


quote.replace('one', '1').replace('both','2')
#lub
print(quote.replace('one','1').replace('both','2'))



quote.split(' ')
#lub
print(quote.split(' '))


quote.isdigit()
quote.isdecimal()
quote.isalpha()
quote.isalnum()
#lub
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())