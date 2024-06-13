# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდე მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.




# List to store actor information
actors_list = [
    ['Robert', 'Downey', 'Known for his role as Iron Man in the Marvel Cinematic Universe.'],
    ['Scarlett', 'Johansson', 'Known for her role as Black Widow in the Marvel Cinematic Universe.'],
    ['Leonardo', 'DiCaprio', 'Known for his role in Titanic and his Oscar-winning performance in The Revenant.'],
    ['Meryl', 'Streep', 'Renowned actress known for her roles in The Devil Wears Prada and Mamma Mia!'],
    ['Tom', 'Hanks', 'Famous for his roles in Forrest Gump, Saving Private Ryan, and Cast Away.']
]


def search_actor(actor_name):
    for actor in actors_list:
        if actor[0].lower() == actor_name.lower() or actor[1].lower() == actor_name.lower():
            return f'Name: {actor[0]}\nLastname: {actor[1]}\nResume: {actor[2]}'
        
    return "Artist not found in the list!"


search_artist = input("Enter the name or last name of the actor/actress you are looking for: ").strip()

result = search_actor(search_artist)

print(result)