def gradestat(students,scores):

    grades={}

    for i in range(len(students)):
        grades[students[i]] = scores[i]
    print("Grades are:", grades)


    sum=0
    for i in grades.values():
        sum +=i
    average_score=sum/len(grades.values())
    print("Average score:", average_score)

    below_70=[]
    for i in grades.keys():
        if grades[i]<70:
            below_70.append(i)
            below_70.sort
    print("Students below 70:", below_70)

    return(grades,average_score,below_70)

def main():
    students=["Alice","Moka","Bob","Charlie","Dora"]
    scores=[85,55,72,91,60]
    gradestat(students,scores)

if __name__=="__main__":
    main()


