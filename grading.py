import sys

def calculatescore(midterm,final,attendance):
    return midterm*0.3+final*0.6+attendance*0.1

def calculategrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'

def main():
    midterm = int(sys.argv[1])
    final = int(sys.argv[2])
    attendance = int(sys.argv[3])

    score = calculatescore(midterm, final, attendance)
    grade = calculategrade(score)
    print(score)
    print(grade)

if __name__ == '__main__':
    main()