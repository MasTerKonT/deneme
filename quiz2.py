'''
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
'''
import sys
def cross(c):
    boşluksayısı=0
    ortaboşluksayısı=c-2
    while ortaboşluksayısı>=1:
        print(boşluksayısı*" "+"*"+" "*ortaboşluksayısı+"*"+boşluksayısı*" ")
        ortaboşluksayısı-=2
        boşluksayısı+=1
    ortaboşluksayısı+=1
    print(boşluksayısı*" "+"*"+" "*ortaboşluksayısı+boşluksayısı*" ")
    boşluksayısı-=1
    ortaboşluksayısı+=1
    while ortaboşluksayısı<=c-2:
        print(boşluksayısı*" "+"*"+" "*ortaboşluksayısı+"*"+boşluksayısı*" ")
        ortaboşluksayısı += 2
        boşluksayısı -=1
def main():
    cross(int(sys.argv[1]))

if __name__ == "__main__":
    main()

