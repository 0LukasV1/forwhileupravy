x=input("Zadaj mi číslo: ")
x=int(x)
výsledok=0
for i in range(1,x+1):
    if i%4==0 or i%7==0:
        výsledok=výsledok+1
print("Počet čísel delitelnými buď 4 alebo 7 je",výsledok)