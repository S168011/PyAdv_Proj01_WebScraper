lazy import click, requests, re, asyncio, aiohttp
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

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as e:
        if e.response is not None:
            match e.response.status_code:
                case 404:
                    print(f"This link could not be found (Error 404).\n{e}")
                case 500:
                    print(f"Internal server error (Error 400). \n{e}")
                case _:
                    print(f"HTTP error occured: \n {e}")
            return
        else:
            print(f"HTTP error without response: \n {e}")
            return
    except RuntimeError as e:
        print(f"RuntimeError occured: \n {e}")
        return


    html = response.content

    word_count = extract_word_count(html)
    parsed_hyperlinks, raw_hyperlinks = extract_parsed_links(html)

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


async def async_recursive_lookup(url: str, depth: int, visited: set, max_depth: int) -> None:
    if depth > max_depth:
        return

    if url in visited:
        return

    visited.add(url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                html = await response.read()

    except aiohttp.ClientResponseError as e:
        match e.status:
            case 404:
                print(f"This link could not be found (Error 404).\n{e}")
            case 500:
                print(f"Internal server error (Error 500).\n{e}")
            case _:
                print(f"HTTP error occurred:\n{e}")
        return

    except aiohttp.ClientError as e:
        print(f"HTTP error without response:\n{e}")
        return

    except RuntimeError as e:
        print(f"RuntimeError occurred:\n{e}")
        return

    word_count = extract_word_count(html)
    parsed_hyperlinks, raw_hyperlinks = extract_parsed_links(html)

    print(f"======================== Depth: {depth}: {url} ========================")
    print("------------------------ Word count ------------------------")
    print(word_count)
    print("------------------------ Raw hyperlinks ------------------------")
    print(raw_hyperlinks)
    print("------------------------ Parsed hyperlinks ------------------------")
    print(parsed_hyperlinks)

    useable_links = []

    for link in raw_hyperlinks:
        if link.startswith("http"):
            useable_links.append(link)

    await asyncio.gather(
        *(async_recursive_lookup(link, depth + 1, visited, max_depth) for link in useable_links)
    )



@click.command
@click.option("--url", 'url', type=str)
@click.option("--max-depth", 'max_depth', type=int)
@click.option("--mode", 'mode', type=str)
def start(url, max_depth, mode) -> None:
    if mode not in ["sync", "async"]:
        raise ValueError(f"Unkown mode: '{mode}'")

    visited_links: set = set()

    if mode == "async":
         asyncio.run(async_recursive_lookup(url, 0, visited_links, max_depth))
    else:
        recursive_lookup(url, 0, visited_links, max_depth)

def main():
    start()

if __name__ == "__main__":
    main()