x=input("Zadaj mi číslo: ")
x=int(x)
výsledok=0
for i in range(1,x+1):
    if i%2==0:
        výsledok=výsledok+i
print("Súčet párnych čísel v intervale je",výsledok)
