import typer
from typing_extensions import Annotated

app = typer.Typer(add_completion=False)

@app.command()
def greet(first: Annotated[str, typer.Argument(help="First name")],
          # use Annotated for optional arguments with default values
          last: Annotated[str, typer.Argument(help="Last name")] = "B", 
          formal: Annotated[bool, typer.Option(help="Use formal address")] = False):
    """
    Say hello to FIRST, optionally with a LAST name and --formal flag.
    typer is used to generate a CLI interface from this function.
    """
    if formal:
        typer.echo(f"Hello, Mr. {last}.")
    else:
        typer.echo(f"Hello, {first} {last}!")

if __name__ == "__main__":
    app()
