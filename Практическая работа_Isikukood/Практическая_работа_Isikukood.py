from math import *
from random import *
from OmaModul import *
# 03/02/23
arvud=[]
isikukoodid=[]

while True:
    ik=input("Anna isikukood: ") #str
    if len(ik)!=11:
        print("Liiga palju või liiga vähe sümboleid. Sisesta veel kord: ")
        arvud.append(ik)
    else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) # "1" ->1
    if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige")
    else:
            print("Esimene sümbol on õige")
            spaev=Sunnipaev(ik_list)
            if spaev=="Viga":
                arvud.append(ik)
            else:

            
             print(f"Sünnipäev on {spaev}")
            print("Viimane number: {ik_list[-1]}")
            hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
         #
            haigla=Sunnikoht(hhh)
         #
            sugu=Sugu(ik_list)

            print(f"See on {sugu},sünnipäev{spaev}. Ta on sündinud {haigla}")
            isikukoodid.append(ik)
                    
    a1=int(ik[0])*1
    b1=int(ik[1])*2
    b2=int(ik[2])*3
    b3=int(ik[3])*4
    b4=int(ik[4])*5
    b5=int(ik[5])*6
    b6=int(ik[6])*7
    b7=int(ik[7])*8
    b8=int(ik[8])*9
    b9=int(ik[9])*1

    s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
    print(s11)
    isikukoodid.append(ik)
print(isikukoodid)
isikukoodid=naised_mehed(isikukoodid)
print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)

    
    

        
        



