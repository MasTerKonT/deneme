val = True
x = input("Enter your full name: ").capitalize()
y = input("Enter your student number: ")
z = input("Enter your birth date as DD/MM/YYYY: ")

if x != "Bilgehan soybaş":
    print("Your full name is invalid.")
    val = False
if y != "2250356046":
    print("Your student number is invalid.")
    val = False
if z != "14/07/2007":
    print("Your birth date is invalid.")
    val = False
if  val:
    print("Welcome, Bilgehan!")
