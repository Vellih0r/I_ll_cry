import random
import os
import click
from config import FILE_PATH


def read_phrases():
    if not os.path.exists(FILE_PATH):
        return []    
    with open(FILE_PATH, "r") as f:
        return [line.strip("_ \n") for line in f.readlines()]


def write_phrases(phrases):
    if not os.path.exists(FILE_PATH):
        print("File not found!!!")
    with open(FILE_PATH, "w") as f:
        f.write("\n".join(phrases))

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
        click.echo(f"Error, list with phrases not found at {FILE_PATH}")


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
        click.echo(f"File: {FILE_PATH}")
    else:
        click.echo("File empty or error coused :(")
        click.echo(f"File: {FILE_PATH}")

if __name__ == "__main__":
    cli()
