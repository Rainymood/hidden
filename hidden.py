from datetime import datetime
import click
import os

try:
    import getch

    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed. Stolen from: https://bit.ly/2YYE22X"""
        print(prompt, end="", flush=True)
        buf = ""
        while True:
            ch = getch.getch()
            if ch == "\n":
                print("")
                break
            else:
                buf += ch
                print("*", end="", flush=True)
        return buf


except ImportError:
    from getpass import getpass


def add_note(note, filepath):
    """Writes note to file at filepath. 

    Example format: 
        [2019-08-12 Mon 11:16] 
        Lorem ipsum dolor sit amet. 
    """
    date_org_fmt = datetime.strftime(datetime.now(), "[%Y-%m-%d %a %H:%M]")
    content = date_org_fmt + "\n" + note + "\n\n"

    with open(filepath, "a") as f:
        click.echo(f"Adding note to ./notes.org...")
        f.write(content)


@click.command()
@click.option("--filepath", default="./notes.org", help="Path to file.")
def main(filepath):
    note = getpass(prompt="Note: ")
    add_note(note, filepath)


if __name__ == "__main__":
    main()
