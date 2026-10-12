lazy import click, requests, re
from bs4 import BeautifulSoup
from collections import Counter
from urllib import parse

def extract_word_count(src: bytes) -> Counter:
    """Count the amount of times a word appears on a website.
    
    Args:
        - src (bytes): the to be examined HTML data.
    
    Returns:
        - Counter: counter object of the amount of times a word was found in the HTML."""

    soup = BeautifulSoup(src, 'html.parser')
    raw_words = soup.get_text().split()
    words = [re.sub(r"\W", "", word.lower()) for word in raw_words]
    words = [word for word in words if word]

    count = Counter(words)

    return count

def extract_parsed_links(src: bytes) -> list[parse.ParseResult[str]]:
    """Count the amount of times a word appears on a website.
    
    Args:
        - src (bytes): the to be examined HTML data.
    
    Returns:
        - list[str]: list with all links found in the HTML."""
    soup = BeautifulSoup(src, "html.parser")
    raw_data = soup.find_all('a')
    raw_links = [str(link.get('href')) for link in raw_data]
    parsed_links = [parse.urlparse(link) for link in raw_links if (link[0:4] == "http" or link[0:3] == "www")]

    return parsed_links

@click.command
@click.option("--url", 'url', type=str)
def main(url) -> None:
    response = requests.get(url)
    html = response.content

    word_count = extract_word_count(html)
    parsed_hyperlinks = extract_parsed_links(html)

if __name__ == "__main__":
    main()

