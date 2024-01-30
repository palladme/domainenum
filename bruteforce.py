import requests, sys
import click

@click.command()
# @click.option('--count', default=1, help='Number of greetings.')
@click.option('--target', prompt='Target Site',
              help='The site to conduct brute force on.')
def brutef(target):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    brutef()




target = 'https://0a34007804563dba85ad54550031004d.web-security-academy.net/'
response = requests.get(target)
response1 = requests.get('https://www.iana.org/help/example-domains')

with open('out.txt', 'w') as f:
    print('Filename:', response.text, file=f)

with open('out1.txt', 'w') as f:
    print('Filename:', response.text, file=f)

with open('out2.txt', 'w') as f:
    print('Filename:', response1.text, file=f)