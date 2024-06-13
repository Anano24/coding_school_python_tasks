# შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
# def unique_list():
# ...
# return ...

my_list = ['apple', 5, 'sun', 4, 'apple', 2, 'apple', 4]

def unique_list(items):
    return list(set(items))


print(unique_list(my_list))
