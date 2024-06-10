# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)


def calculator(num_1, num_2, operator):
    """
    Perform basic arithmetic operations.
    """

    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "/":
        if num_2 == 0:
            return "Zero division is undefined!"    
        return num_1 / num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "**":
        return num_1 ** num_2
    else:
        return "Please enter valid operator"




def main():

    try:  
        num_1 = float(input("Please enter first number: "))
        operator = input("Please choose operator '+ - * / **' : ").strip()
        num_2 = float(input("Please enter second number: "))
        
        result = calculator(num_1, num_2, operator)
        print(f"{num_1} {operator} {num_2} = {result}")
    except:
        print("Invalid input! Please enter numeric values for numbers.")
        

main()


    