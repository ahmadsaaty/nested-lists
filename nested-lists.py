lists= []
listn= []
for _ in range(3):
    name = input("enter name: ")
    score = float(input("enter grade: "))
    listn = [name, score]
    
    print(listn)
    lists.append(listn)
print(lists)