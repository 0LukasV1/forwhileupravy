
x=input("Zadaj mi číslo")
for i in range(1,int(x)+1):
    if int(i)%3==0:
        print("číslo",i,"je delitelné 3")
    else:
        print("číslo nie je delitelné 3")
l = 1

for u in range(1,100):

    if u % 8 == 0:

     k = l * (u + 1) // 8

print(k, end=' ')