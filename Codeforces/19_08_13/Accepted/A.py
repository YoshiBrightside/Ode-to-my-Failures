# 1203A
# Circle of Students

queries = int(raw_input())
for _ in range(queries):
    _ = raw_input()
    students = list(map(int,raw_input().split()))
    if len(students) <= 2:
        print('YES')
    else:
        failed = False
        for i in range(len(students)-1):
            if abs(students[i]-students[i+1])>1 and not((students[i]==len(students) and students[i+1]==1) or (students[i]==1 and students[i+1]==len(students))):
                print('NO')
                failed = True
                break
        if not failed:
            print('YES')