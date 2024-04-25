month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

expense = input("enter expense amount") 
expense = int(expense)
found = False

for i in range(len(expense_list)):

    if expense == expense_list[i]:
        print("month:", month_list[i], "expenses:", expense_list[i])
        found = True
        break


if found == False:
     print("XXXX")

for i in range(1, 6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)