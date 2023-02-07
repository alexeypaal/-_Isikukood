from hashlib import sha1


def Sugu(ik_list:list)->str:
    """Esimese tahe jargi m��rame sugu
    :param list list_ik:J�rjend isikukoodi numbridest
    :rtype: str
    """
    if int(ik_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu
def Sunnikoht(a:int)->str:
    """Tagastab sunnikohta
    """
          a=int(ik_list[8]+ik_list[9]+ik_list[10])
         if 1<=a<=10:
             haigla="kuresaare Haigla"
         elif 11<=a<=19:
             haigla="Tartu �likooli Naistekliinik, Tartumaa, Tartu"
         elif 21<=a=220:
             haigla="Ida-Viru Keskhaigla (Kohtla-J�rve, endine J�hvi)"
         elif 271<=a<=370:
             haigla="Maarjam�isa Kliinikum (Tartu), J�geva Haigla"
         elif 371<=a<=420:
             haigla="Narva Haigla"
         elif 421<=a<=470:
             haigla="P�rnu Haigla "
         elif 471<=a<=480:
             haigla="Pelgulinna S�nnitusmaja (Tallinn), Haapsalu haigla"
         elif 491<=a<=520:
             haigla="J�rvamaa Haigla (Paide)"
         elif 521<=a<=570:
             haigla="Rakvere, Tapa haigla"
         elif 571<=a<=600:
             haigla="Valga Haigla "
         elif 601<=a<=650:
             haigla="Viljandi Haigla"
         elif 651<=a<=700:
             haigla=" L�una-Eesti Haigla (V�ru), P�lva Haigla "
         else:
             haigla="___"
            return haigla
def

def Sunnipaev(d: int,m: int,y: int)->str:
    """
    """
    s1=int(ik_list[0])
    y=(ik_list[1]+ik_list[2])      #aasta
            m=(ik_list[3]+ik_list[4])   #kuu
            d=int(ik_list[5]+ik_list[6])   #p�ev
    if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                spaev="Viga"
                #arvud.append(ik)
    else:
         if s1==1 or s1==2:
                    yy="18"
         elif s1==3 or s1==4:
                    yy="19"
         else:
                    yy="20"
         spaev=str(d)+"."+str(m)+"."+yy+(y)    #ei ole 18..,29..,20..
         return spaev
def naised_mehed(isikoodid:list):
    """
    :rtype: list,list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        ik_list=list(kood)
        sugu=Sugu(ik_list)
        if sugu=="naine":
            naised.append(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(mehed)
    return ikoodid
