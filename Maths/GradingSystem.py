def gradingStudents(grades):
    result=[]
    for grade in grades:
        if grade>=38 and grade % 5>=3:
            grade+=(5-grade%5)
        result.append(grade)
    return result 