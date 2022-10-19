x=input("Zadaj mi číslo: ")
x=int(x)
výsledok=0
for i in range(1,x+1):
    if i % 8 == 0:
        výsledok+=1
print("Počet čísel delitelných 8 v intervale je",výsledok)