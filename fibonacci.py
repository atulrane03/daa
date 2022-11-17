#Recursive Method - 
# def Fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return (Fibonacci(n-1) + Fibonacci(n-2))

# n_terms = int(input("Enter number of terms you want: "))

# if n_terms<=0:
#     print("Invalid Integer")
# else:
#     print("Sequence is as follows: ")
#     for i in range(n_terms):
#         print(Fibonacci(i))

# Non recursive method - 

n_terms = int(input("Enter the no. of terms you want: "))
n1,n2 = 0,1
count=0
if n_terms<=0:
    print("Invalid input")
elif n_terms == 1:
    print("Fibonacci Sequence: ")
    print(n1)
else:
    print("Fibonacci Sequence: ")
    while count<n_terms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2 = nth
        count+=1




        #time complextity of recursive = o 2^n
       # time complextity of non-recursive = o(n)