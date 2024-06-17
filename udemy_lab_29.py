from decimal import Decimal, ROUND_DOWN

# Program description: Program obliczający pole koła i obwód koła
WartośćPi= Decimal('3.14')
print(WartośćPi)
PromienOkregu = Decimal('5')
print ('w tym zadaniu liczymy pole koła')
PoleKola = WartośćPi * PromienOkregu ** 2
PoleKola = PoleKola.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(PoleKola)


print('w tym zadaniu liczymy obwód koła')
ObwódOkregu =  Decimal(2) * WartośćPi * PromienOkregu
ObwódOkregu = ObwódOkregu.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(ObwódOkregu)

print('w tym zadaniu liczymy pole prostokąta')
PoleProstokata = 2 * 3
print(PoleProstokata)