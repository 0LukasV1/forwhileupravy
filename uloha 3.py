x=input("Zadaj mi meno: ")
while x != "koniec":
    x = input("Zadaj mi meno: ")
print("Zadaj si reťazec koniec")
l=[]

for u in range(1, 100):

    if (u%7==0) and (u%4==0):

        l.append(str(u))

print (','.join(l))