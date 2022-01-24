x = int(input("zadaj km pre prvý deň:"))
y = int(input("zadaj cieľové kilometre:"))

den = 1

while x < y:
    den += 1
    x += x * 0.1

print(f"na {den} den prebehne {x:2f} km") #neviem aký iný príkaz na desatiné čísla ked nejde 2f
