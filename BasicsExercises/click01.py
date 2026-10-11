import click

@click.command()
@click.argument('numbers', nargs=-1, type=int)
def counter(numbers) -> None:
    print(sum(numbers))
    

counter()