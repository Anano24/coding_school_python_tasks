# 1. 
# შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“



def tripled_word(word):
    return word * 3


word = input("Enter some word: ")
print(f"Tripled: {tripled_word(word)}")