# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)



def weight_on_the_moon(weight):
    return weight / 6


weight = float(input("Enter your weight: "))
print(f"Your weight on the moon is: {weight_on_the_moon(weight):.2f} kg")