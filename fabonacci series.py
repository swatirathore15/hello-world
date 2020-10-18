#  I made a function for nth Fibonacci number 
  
def Fibo(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibo(n-1)+Fibo(n-2) 
  
# Driver Program 
  
print(Fibo(9)) 
  
#This code is contributed to learn pull reqeust.please don't reject my pull request. you can leave as it is.
