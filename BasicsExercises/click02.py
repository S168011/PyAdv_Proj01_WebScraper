import click

@click.command()
@click.argument('value', nargs=1, type=int)
@click.option('--rate', 'rate', type=float)
def convert(value: int, rate: float) -> None:
    print(round((value * rate), 2))

convert();