lazy import click, requests, re
from bs4 import BeautifulSoup
from collections import Counter

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

def extract_links(src: bytes) -> list[str]:
    """Count the amount of times a word appears on a website.
    
    Args:
        - src (bytes): the to be examined HTML data.
    
    Returns:
        - list[str]: list with all links found in the HTML."""
    soup = BeautifulSoup(src, "html.parser")
    raw_data = soup.find_all('a')
    links = [str(link.get('href')) for link in raw_data]
    return links

@click.command
@click.option("--url", 'url', type=str)
def main(url) -> None:
    response = requests.get(url)
    html = response.content

    word_count = extract_word_count(html)
    hyperlinks = extract_links(html)

if __name__ == "__main__":
    main()