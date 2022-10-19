x=input("Zadaj mi číslo")
for i in range(1,int(x)+1):
    if int(i)%3==0:
        print("číslo",i,"je delitelné 3")
    else:
        print("číslo nie je delitelné 3")