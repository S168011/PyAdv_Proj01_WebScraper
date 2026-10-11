from bs4 import BeautifulSoup

file = input("Enter the location of the HTML file: ")

with open(file) as html_file:
    soup = BeautifulSoup(html_file)

print(soup.prettify())