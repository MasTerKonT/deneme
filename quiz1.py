'''
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321
'''
import sys

def generate_numberpyramid(p):
    boşluksayısı=p-1
    for p in range(1,p+1):
        print(boşluksayısı*" ",end="")
        for i in range(1,p+1):
            print(i,end="")
        for i in range(p-1,0,-1):
            print(i,end="")
        boşluksayısı -= 1
        print(" ")


def main():
    generate_numberpyramid(int(sys.argv[1]))


if __name__ == "__main__":
    main()