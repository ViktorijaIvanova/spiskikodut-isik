ikoodid=[] 
arvud=[]
while True:
 isik=input("sisetage isikukood:") #str
 if len(isik)!=11:
     print("liiga palju või liiga vähe sümboleid.Sisesta veel kord:")
 else:
     print("isiskukood kontroll")
     isik_list=list(isik)
     s1=int(isik_list[0])
     if s1 not in [1,2,3,4,5,6]:
         print("esimene sümbol ei ole õige!")
     else:
         print("esimene sümbol on õige!")
         y=isik_list[1]+isik_list[2]
         m=isik_list[3]+isik_list[4]
         d=int(isik_list[5]+isik_list[6])
         if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
             print("sünnipäev ei saa luua")
         else:
             if s1==1 or s1==2:
                 yy="18"
             elif s1==3 or s1==4:
                 yy="19"
             else:
                 yy="20"
             späev=str(d)+"."+str(m)+"."+str(y)
             print(f"sünnipäev on {späev}")
             print(f"viimane number: {isik_list[-1]}")
         if isik in True:
             ikoodid.append(isik)
             print(ikoodid)
         else:
             arvud.append(isik)
             print(ikoodid)
         if arvud:
             isik.sort()
             isik>=100000000000
            

