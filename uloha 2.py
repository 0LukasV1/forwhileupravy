
x=0
výsledok=0
y=0
while výsledok <= 100:
    x+=1
    výsledok+=x
    y+=1
print("Počet čísel bol",y,"celkový súčet čísel bol",výsledok)

l = 0

for u in range(1,100):

    if u % 2 == 0:

        l = l + u

print('sucet =', l)