string=input("Enter string:")
zanoretCount=0
bashktinglloretCount=0
for i in string.strip().replace(" ",""):
    if string != None:
        if(i.isalpha()):
              if(i=='a' or i=='e' or i=='ë' or i=='i' or i=='o' or i=='u' or i=='y' or i=='A'
                or i=='E' or i=='Ë' or i=='I' or i=='O' or i=='U' or i=='Y'):
                  zanoretCount +=1  
              else:
                  bashktinglloretCount +=1
        else:
            pass
    else:
        print("Ju nuk keni jepun asnje karakter!!!")
print("Nr. i zanoreve:"+ str(zanoretCount) +" nr i bashtinglloreve eshte:"+str(bashktinglloretCount))

