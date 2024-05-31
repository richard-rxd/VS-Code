def areacalc(a,b,shape="triangle"):
    if shape=="triangle":
        area = (1/2)*a*b
    else:
        area = a*b
    return area

def print_pattern(x):
    for i in range(x):
        pattern = ""
        for j in range(i):
            pattern += "*"
        print(pattern)

population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}

task = input("print, add, remove or query?")

if task == "print":
    for i in population:
        print(f"{i}==>{population[i]}")
elif task == "add":
    newcou = input("Country to add: ")
    if newcou in population:
        print(f"Country {newcou} is already listed")
    else:
        newpop = int(input(f"Population of {newcou}: "))
        population.update({newcou: newpop})
        print(f"Country {newcou} has been added with a population of {newpop}")
elif task == "remove":
    delcou = input("Country to delete: ")
    if delcou in population:
        del population[delcou]
    else:
        print(f"Country {delcou} is not listed")
elif task == "query":
    query = input("Country to query: ")
    if query in population :
        print(f"Population of {query} is {population[query]}")
    else:
        print(f"{query} not found in list")

