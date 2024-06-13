# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21


customer_info = []

for _ in range(3):
    name = input('Name: ')
    lastname = input('Lastname: ')
    age = int(input('Age: '))
    print()
    customer_info.append([name, lastname, age])



customer_num = int(input("Enter the number to find customer in the list: "))

if 0 <= customer_num < len(customer_info):
    print(f"Name: {customer_info[customer_num][0]}\nLastname: {customer_info[customer_num][1]}\nAge: {customer_info[customer_num][2]}")
else:
    print("Customer is not in the list!")