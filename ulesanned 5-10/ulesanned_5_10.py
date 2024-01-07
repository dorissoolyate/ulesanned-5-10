
#ulesanne 5
import math
N=float(input("Sisesta ristküliku pikkus (N meetrides) : "))
M =float(input("Sisesta ristküliku laius (M meetrites): "))
diagonaal=math.sqrt(N**2 + M**2)
print(f"Ristkülikukujulise maatüki diagonaal on {diagonaal:.2f} meetrit.")

#ulesanne 6
viga oli kiiruse arvutamisega
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#ulesanne 7
arvud=[]
for i in range(5):
    arv=int(input(f"Sisesta {i+1}. arv: "))
    arvud.append(arv)
keskmine=sum(arvud)/len(arvud)
print(f"Aritmeetiline keskmine on: :{keskmine}")

#ulesanne 8
print("    @..@")
print("   (----)")
print("  ( \\__/ )")
print("  ^^ \"\" ^^")

#ulesanne 9
a=int(input("Sisesta esimese külje pikkus a: "))
b=int(input("Sisesta teise külje pikkus b: "))
c=int(input("Sisesta kolmanda külje pikkus c: "))
ümbermõõt=a+b+c
print(f"Kolmnurga ümbermõõt on {ümbermõõt}")

#ulesanne 10
pitsa_hind=12.9
jootraha_prots=10
jootraha=(jootraha_prots/100)*pitsa_hind
kogusumma=pitsa_hind+jootraha
igauks_maksab=kogusumma/2
print(f"igauks maksab {igauks_maksab:.2f} eur")
