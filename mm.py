n=int(input("Enter a number"))
a=0
t=n
while t !=0:
    digit=t%10
    a=a+digit**3
    t= t//10
print(a)
if(n==a):
    print("It's an Armstrong number")
else:
    print("It's not an armstrong number")