lists= []
listn= []
for _ in range(int(input("enter number of students: "))):
    name = input("enter name: ")
    score = float(input("enter grade: "))
    listn = [name, score]
    
    print(listn)
    lists.append(listn)
print(lists)