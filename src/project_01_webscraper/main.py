lazy import click, requests, re
from bs4 import BeautifulSoup
from collections import Counter

@click.command
@click.option("--url", 'url', type=str)
def main(url) -> None:
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    raw_words = soup.get_text().split()
    words = [re.sub(r"\W", "", word.lower()) for word in raw_words]
    words = [word for word in words if word]

    words_counter = Counter(words)
    print(words_counter)

if __name__ == "__main__":
    main()