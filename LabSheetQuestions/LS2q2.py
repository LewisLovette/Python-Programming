# The 121COM grading scheme is as follows:
# Total grade is 30% from exam and 70% from coursework.
# Must have >40% overall and >35% in each component to pass

# The rough degree boundaries are:
# 3rd = 40-49%
# 2:2 = 50-59%
# 2:1 = 60-69%
# 1st = 70% and above

# The following script takes a users grades and lets them know what degree level that is equivalent to. 

cwMark = int( input("What is the coursework mark? "))
exMark = int( input("What is the exam mark? "))
totMark = (30*exMark + 70*cwMark)/100


if cwMark<35 or exMark<35:
    grade="FAIL"
    print("Component failed - no grade")
else:
    if totMark < 40:
        grade = "FAIL"
        print("Very bad")    
    elif totMark < 50:
        grade = "3rd"
        print("Below Average")
    elif totMark < 60:
        grade = "2:2"
        print("Average")
    elif totMark < 70:
        grade = "2:1"
        print("Good")
    elif totMark >= 70:   #added = so that a mark of 70 is covered
        grade = "1st"
        print("Great!")
        if totMark == 100:
            print("In fact its perfect!")
    print("On track for a: " + grade)
print(totMark)
