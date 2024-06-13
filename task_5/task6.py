# დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით
# სტრიქონი: w3schools უნდა დააბრუნოს ლექსიკონი:

# {'w': 1, '3': 1, 's': 2, 'c': 1, 'h': 1, 'o': 2, 'l': 1}



def string_to_dict(my_str):
    my_dict = {}

    for char in my_str:
        my_dict[char] = my_str.count(char)
        
    return my_dict


my_str = 'w3schools'
result = string_to_dict(my_str)
print(result)