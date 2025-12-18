def hypotenuse(a,b):
    return (a*a+b*b)**(1/2)

def test_hypotenuse():
    try:
        assert hypotenuse(3,4)==5
        assert hypotenuse(5,12)==13

    except AssertionError:
        print("At least one test failed.")
    else:
        print("Tests are passed.")

def main():
    test_hypotenuse()

if __name__=="__main__":
    main()


#Toprak: 91 -> 97
#Altuğ: 80 -> 75
#Erdem: 89
#Bilgehan: 75 -> 70