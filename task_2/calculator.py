
number = int(input("Enter number: "))


for i in range(1, number + 1):
    print()
    for j in range(1, number + 1):
        print(f"{i} * {j} =", i*j)
        