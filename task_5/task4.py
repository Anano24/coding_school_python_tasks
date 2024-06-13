# შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# def set_to_tuple():
# ...
# return ...


def set_to_tuple(set_1, set_2):
    new_set = set_1.union(set_2)
    return tuple(new_set)


set_1 = {1, 4, 'a'}
set_2 = {3, 'b', 4, 5}

result = set_to_tuple(set_1, set_2)

print(result)