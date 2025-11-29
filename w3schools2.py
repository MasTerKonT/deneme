import sys

def somefunc(yas):  
    if yas < 0:
        return "Invalid age"
    elif yas < 18:
        return "Minor"
    elif yas > 150:
        return "No one can live that long"
    else:
        return "Adult"

def main():
    try:
        yas = float(sys.argv[1])
        print(somefunc(int(yas)))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()