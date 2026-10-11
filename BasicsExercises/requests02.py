#DOESN'T WORK.
#Local server is being difficult.

lazy import requests

print('''Wat wil je doen?
1. Een nieuwe post aanmaken.
2. Een comment toevoegen aan een bestaande post.''')

action = int(input(">\t"))

if (action == 1):
    id: int = int(input("Post ID: "))
    title: str = input("Post title: ")
    views: int = int(input("Post views: "))

    r = requests.post("http://localhost:3000", data={'id': str(id), 'title': title, 'views': views})

