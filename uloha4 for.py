x=input("Zadaj mi číslo: ")
x=int(x)
výsledok=0
for i in range(1,x+1):
    výsledok+=i
print("Hodnota súčtu všetkých čísel v intervale od 1 po",x,"je",výsledok)