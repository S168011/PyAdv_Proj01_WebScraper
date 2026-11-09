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

def extract_parsed_links(src: bytes) -> tuple[list[parse.ParseResult[str]], list[str]]:
    """Count the amount of times a word appears on a website.
    
    Args:
        - src (bytes): the to be examined HTML data.
    
    Returns:
        - list[str]: list with all links found in the HTML."""
    soup = BeautifulSoup(src, "html.parser")
    raw_data = soup.find_all('a')
    raw_links = [str(link.get('href')) for link in raw_data]
    parsed_links = [parse.urlparse(link) for link in raw_links if (link[0:4] == "http" or link[0:3] == "www")]

    return parsed_links, raw_links

def recursive_lookup(url: str, depth: int, visited: set, max_depth: int) -> None:
    if depth > max_depth:
        return

    if url in visited:
        return

    visited.add(url)

    response = requests.get(url)
    html = response.content

    word_count = extract_word_count(html)
    parsed_hyperlinks, raw_hyperlinks = extract_parsed_links(html)

    # print(word_count)
    # print()
    # print(parsed_hyperlinks)
    # print()

    print(f"======================== Depth: {depth}: {url} ========================")
    print("------------------------ Word count ------------------------")
    print(word_count)
    print("------------------------ Raw hyperlinks ------------------------")
    print(raw_hyperlinks)
    print("------------------------ Parsed hyperlinks ------------------------")
    print(parsed_hyperlinks)

    for link in raw_hyperlinks:
        if link.startswith("http"):
            recursive_lookup(link, depth + 1, visited, max_depth)

@click.command
@click.option("--url", 'url', type=str)
@click.option("--max-depth", 'max_depth', type=int)
@click.option("--mode", 'mode', type=str)
def main(url, max_depth, mode) -> None:
    if mode not in ["sync", "async"]:
        raise ValueError(f"Unkown mode: '{mode}'")

    if mode == "async":
        raise NotImplementedError("Code hasn't been written yet")

    visited_links: set = set()
    recursive_lookup(url, 0, visited_links, max_depth)
if __name__ == "__main__":
    main()

