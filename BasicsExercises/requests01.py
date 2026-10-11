lazy import requests

print("What post do you want to see?")

post_nr = int(input("> "))
response = requests.get(f'http://localhost:3000/posts/{post_nr}')
response_dict = response.json()

print(response_dict["title"], f"({response_dict["views"]} views)")

comments = requests.get('http://localhost:3000/comments')
comments_dict = comments.json()

for comment in comments_dict:
    if comment["postId"] == str(post_nr):
        print(f"- {comment["text"]}") 