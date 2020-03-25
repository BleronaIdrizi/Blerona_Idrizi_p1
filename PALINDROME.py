def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
 
    rev = reverse(s) 
   
    if (s == rev): 
        return True
    return False

palindrome=input("Shkruani nje fjali per ta pare nese eshte palindrome,apo jo:")
ans = isPalindrome(palindrome) 
  
if ans == 1: 
    print("Fjalia e dhene eshte palindrome.") 
else: 
    print("Fjalia e dhene nuk eshte palindrome.")
