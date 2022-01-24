from random import choice


mena = ("Mačka", "Pes", "Programátor", "učiteľ", "žiak", "osoba")
prid_mena = ("pekný", "šialený", "obyčajný", "milá")
vec = ("stôl", "obraz", "televízor")
slovesa = ("prať", "žehliť", "usmievať sa")

for _ in range(int(input("Enter integer value:"))):
    print(list(map(choice, [mena, slovesa, prid_mena, vec])))