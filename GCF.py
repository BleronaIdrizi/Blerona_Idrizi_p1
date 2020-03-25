a=int(input("Shkrusni numerin e pare:"))
b=int(input("Shkrusni numerin e dyte:"))

def GCF(a,b): 
    if(b==0): 
       return a 
    else: 
       return int(GCF(b,a%b)) 
 
   
print ("GCF e numerit: "+ str(a) +" dhe numerit: "+ str(b) + " eshte: " + str(GCF(a,b))) 

