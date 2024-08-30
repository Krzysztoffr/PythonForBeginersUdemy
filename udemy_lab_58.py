# 1. W tym zadaniu możesz się spodziewać ciekawego wyniku.
# (jeżeli chcesz sprawdzić jego działanie w innym roku niż 2017 to zmień liczbę 1017, np dla roku bieżącego 2019 należy użyć 1019):
# >>> Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50. Całość pomnóż przez 20, a następnie dodaj 1017.
# Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.<<<

shoesize = 44
number = (shoesize*5 +50)*20+1024 -1979
print(number)
print('shoe size is:',number //100)
print('birth date is:',number %100)


# 2. Kolejne działanie z tego samego cyklu:
# >>>Pomyśl liczbę nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę. Powinno wyjść 5 - zawsze. <<<

number2 = 5
calc = ((number2*2) //2) - number2
print(calc)
# 3. Ile to jest - najpierw policz sam, a potem sprawdź rozwiązanie pythona
# 2+2*2 = ?
# 7+7/7+7*7-7 = ?


# 4. Wykładowca mówi studentom.
# Zaliczysz semestr jeżeli masz obecność co najmniej 80% i średnią >= 3.0
# lub zaliczyłeś pracę semestralną.
# Zbuduj wyrażenie w Python które stwierdzi czy student, który ma obecność 0.85, średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.

obecnosc = 0.85
srednia = 3.5
zaliczenie_ex4 = False
zaliczyłes_prace_semestralna = False

zaliczenie_ex4 = (
    (obecnosc >= 0.8 and srednia >= 3.0)
                or
                (zaliczyłes_prace_semestralna)
                )

print(f"Dla obecnosc {obecnosc}, srednia {srednia}, zaliczyłes_prace_semestralna {zaliczyłes_prace_semestralna}, "
      f"wynik zaliczenie_ex4 {zaliczenie_ex4}, {'Semestr zaliczony' if zaliczenie_ex4 else 'Semestr niezaliczony'}")

# F-stringi (formatowane stringi) w Pythonie to sposób na wstawianie wartości zmiennych bezpośrednio do ciągu znaków. Są one dostępne od Pythona 3.6
# i pozwalają na bardziej czytelne i zwięzłe formatowanie tekstu. F-stringi są oznaczane literą `f` przed cudzysłowem otwierającym ciąg znaków.
# Oto kilka kluczowych punktów dotyczących f-stringów:

# Podstawowa składnia:
# F-stringi są oznaczane literą f przed cudzysłowem otwierającym ciąg znaków.
# Wartości zmiennych są wstawiane do ciągu znaków za pomocą nawiasów klamrowych {}.

# 5. Wykładowca zmienił zdanie. Aby zaliczyć semest trzeba: mieć obecność co najmniej 80%, średnią >=3.0 i zaliczoną pracę. Czy teraz student zda?

obecnosc = 0.85
srednia = 3.5
zaliczenie = False
zaliczyłes_prace_semestralna = False

zaliczenie_ex5 = (
    (obecnosc >= 0.8 and srednia >= 3.0)
               and
                zaliczyłes_prace_semestralna
                )
print(f"Dla obecnosc {obecnosc}, srednia {srednia}, zaliczyłes_prace_semestralna {zaliczyłes_prace_semestralna}, "
      f"wynik zaliczenie_ex5 {zaliczenie_ex5}, {'Semestr zaliczony' if zaliczenie_ex5 else 'Semestr niezaliczony'}")


# 6. Zmieniamy dane studenta. Teraz ma obecność 40%. średnią 2.5 ale zaliczył pracę semestralną. Sprawdź wg którego z kryterów student zaliczy semestr.

obecnosc = 0.40
srednia = 2.5
zaliczenie = False
zaliczyłes_prace_semestralna = True

zaliczenie_ex5 = (
    (obecnosc >= 0.8 and srednia >= 3.0)
               and
                zaliczyłes_prace_semestralna
                )
print(f"Dla obecnosc {obecnosc}, srednia {srednia}, zaliczyłes_prace_semestralna {zaliczyłes_prace_semestralna}, "
      f"wynik zaliczenie_ex5 {zaliczenie_ex5}, {'Semestr zaliczony' if zaliczenie_ex5 else 'Semestr niezaliczony'}")

print('------------------')
#------------------
#Rozwiązanie ze zdefiniowaną funkcją
print('EX.4')
def check_passing(attendance, average, passed_semestral_work):
    return (attendance >= 0.8 and average >= 3.0) or passed_semestral_work

attendance = 0.85
average = 3.5
passed_semestral_work = False

passing_ex4 = check_passing(attendance, average, passed_semestral_work)
print(f"For attendance {attendance}, average {average}, passed semestral work {passed_semestral_work}, "
      f"result passing_ex4 {passing_ex4}, {'Semester passed' if passing_ex4 else 'Semester not passed'}")

print('EX.5')
def check_passing_with_work(attendance, average, passed_semestral_work):
    return (attendance >= 0.8 and average >= 3.0) and passed_semestral_work

attendance = 0.85
average = 3.5
passed_semestral_work = False

passing_ex5 = check_passing_with_work(attendance, average, passed_semestral_work)
print(f"For attendance {attendance}, average {average}, passed semestral work {passed_semestral_work}, "
      f"result passing_ex5 {passing_ex5}, {'Semester passed' if passing_ex5 else 'Semester not passed'}")

print('EX.6')
attendance = 0.40
average = 2.5
passed_semestral_work = True

passing_ex6 = check_passing_with_work(attendance, average, passed_semestral_work)
print(f"For attendance {attendance}, average {average}, passed semestral work {passed_semestral_work}, "
      f"result passing_ex6 {passing_ex6}, {'Semester passed' if passing_ex6 else 'Semester not passed'}")