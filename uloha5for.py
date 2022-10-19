x=input("Zadaj mi číslo: ")
x=int(x)
výsledok=0
for i in range(1,x+1):
    if i % 2 == 0:
        výsledok+=1
print("Počet čísel deliteľných 2 v intervale je",výsledok)