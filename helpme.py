import random
import os
import click

file_path = f"{os.getcwd()}/helptext.txt"

def read_phrases():
    if not os.path.exists(file_path):
        return []    
    with open(file_path, "r") as f:
        return [line.strip("_ \n") for line in f.readlines()]


def write_phrases(phrases):
    if not os.path.exists(file_path):
        return False
    with open(file_path, "w") as f:
        f.write("\n".join(phrases))
    return True


@click.group()
def cli():
    """CLI for generating phrases\n
    Type "support gen" and you will get +5 motivation :)"""


@cli.command()
def pls():
    """Generate mental health support."""
    phrases = read_phrases()
    if phrases:
        click.echo(random.choice(phrases))
    else:
        click.echo(f"Error, list with phrases not found at {file_path}")


@cli.command()
@click.argument("phrase")
def add(phrase):
    """Add new phrase."""
    phrases = read_phrases()
    if phrase in phrases:
        click.echo("Phrase already exists")
    else:
        phrases.append(phrase)
        write_phrases(phrases)
        click.echo("Phrase added!")

@cli.command()
@click.argument("phrase")
def rm(phrase):
    """Remove phrase."""
    phrases = read_phrases()
    if phrase in phrases:
        phrases.remove(phrase)
        write_phrases(phrases)
        click.echo("Phrase removed!")
    else:
        click.echo("Phrase not found :(")


@cli.command()
def ls():
    """Show all phrases"""
    phrases = read_phrases()
    if phrases:
        click.echo("\n".join(phrases))
        click.echo(f"File: {file_path}")
    else:
        click.echo("File empty or error coused :(")

if __name__ == "__main__":
    cli()
