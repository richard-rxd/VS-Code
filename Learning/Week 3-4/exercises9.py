result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads=0
n=0

for items in result:
    if result[n]=="heads":
        heads=heads+1
    n=n+1

print(f"Total Heads: {heads}")

for k in range (1,11):
    if k%2!=0:
        print(k*k)

expense_list = [2340, 2500, 2100, 3100, 2980]
months = ["jan","feb","mar","apr", "may"]
notfound = True

exp=int(input("Enter Expense Amount: "))

for i in expense_list:
    if exp==i:
        month=expense_list.index(i)
        print(f"Expense occured in: {months[month]}")
        notfound = False
        break

if notfound == True:
    print(f"Expense {exp} not found")

km=1
for m in range(1,5):
    response=input("Are you tired?")
    if response == "yes":
        print("you didn't finish the race")
        break
    km=km+1

if km==5:
    print("congratulation")

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)