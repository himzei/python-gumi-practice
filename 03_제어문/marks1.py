marks = [90, 25, 67, 45, 80]

number = 0 

for mark in marks:
    number = number + 1 # number 학생번호  1, 2, 3, 4, 5

    if mark >= 60: 
        print(f"{number}번 학생은 합격입니다.")
    else: 
        print(f"{number}번 학생은 불합격입니다.")
