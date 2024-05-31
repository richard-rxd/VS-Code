# Task 1

expenses = {"JAN": 2200, "Feb": 2350, "MAR": 2600, "APR": 2130, "MAY": 2190}

extraspent = expenses["Feb"] - expenses["JAN"]
print(f"FEB extra spent: {extraspent}")

quarter1 = expenses["Feb"] + expenses["JAN"] + expenses["MAR"]
print(f"Quarter 1 spent: {quarter1}")

k2months = 0
for i in expenses:
    if expenses[i] == 2000:
        print(f"2000 USD spent in: {expenses[i]}")
        k2months += 1
    
if k2months == 0:
    print("No months with 2k spent")

expenses["JUN"] = 1980

expenses["APR"] = expenses["APR"] - 200

print(expenses)

# Task 2

heros=['spider man','thor','hulk','iron man','captain america']

print("Length of the list: ",len(heros))

heros.append("black panther")
print("New List: ", heros)

del heros[len(heros)-1]
heros.insert(3, "black panther")
print("Updated List: ", heros)

heros[1:3] = ["doctor strange"]
print("Updated List: ", heros)

heros.sort()
print("Sorted List: ", heros)

# Task 3

maxnr = int(input("Input MAX Number: "))
oddlist = []

for i in range(maxnr+1):
    if i % 2 != 0:
        oddlist.append(i)

print(f"Odd Number: ", oddlist)