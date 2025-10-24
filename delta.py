import sys

def main():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    delta = float(b * b - 4 * a * c)

    if delta<0:
        print("There are no solutions")
    elif delta==0:
        print("There is one solution")
        print((-b+delta**1/2)/(2*a))
    elif delta>0:
        print("There are two solutions")
        print((-b-delta**1/2)/(2*a))
        print((-b+delta**1/2)/(2*a))

if __name__ == "__main__":
    main()