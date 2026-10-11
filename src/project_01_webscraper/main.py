import click
import requests

@click.command
@click.option("--url", 'url', type=str)
def main(url) -> None:
    response = requests.get(url)
    html = response.content
    print(html)

if __name__ == "__main__":
    main()