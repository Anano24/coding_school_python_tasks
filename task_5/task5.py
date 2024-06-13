# შექმენი ფუნქცია, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.



def is_dict_empty(my_dict):
    if not my_dict:
        return 'Dictionary is empty!'
    else:
        return 'Dictionary is not empty'


my_dict = {}

result = is_dict_empty(my_dict)

print(result)
