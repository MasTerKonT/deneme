x=float(input('Enter a number: '))
if int(x+0.5)==int(x):
    print(int(x))
elif int(x + 0.5) == int(x + 1): # We can just code only "else" here.
    print(int(x+1))