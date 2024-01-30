import requests, sys
import click

@click.command()
@click.argument('target')
@click.argument('wordlist', type=click.Path())
def brutef(target,wordlist):
    # with open('out.txt', 'w') as f:
    #     response = requests.get(target)
    #     # print('Filename:', response.text, file=f)
    #     for x in wordlist:
    #         temp_response = requests.get(str(response) + str(x))
    #         print('Filename:', x + " " + temp_response.text, file=f)

    response = requests.get(target)
    with open(wordlist, 'r') as f:
        for x in f:
            temp_target = target + "/" + x
            print(temp_target)
            # temp_response = requests.get(str(response) + str(x))
            # print(x + " " + temp_response.text)
            pass

if __name__ == '__main__':
    brutef()




# target = 'https://0a34007804563dba85ad54550031004d.web-security-academy.net/'
# response = requests.get(target)
# response1 = requests.get('https://www.iana.org/help/example-domains')

# with open('out.txt', 'w') as f:
#     print('Filename:', response.text, file=f)

# with open('out1.txt', 'w') as f:
#     print('Filename:', response.text, file=f)

# with open('out2.txt', 'w') as f:
#     print('Filename:', response1.text, file=f)