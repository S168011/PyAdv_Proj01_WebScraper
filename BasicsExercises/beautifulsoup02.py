from bs4 import BeautifulSoup

file = input("Enter the location of the HTML file: ")

with open(file) as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

images = soup.find_all('img')

for image in images:
    if (image['src'][-3:] == "jpg"):
        print(image)