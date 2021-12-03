#!/bin/python3
import sys
from bs4 import BeautifulSoup
from glob import glob

def main():
    filenames = glob('input_html/*')
    for filename in filenames:
        print('Processing ' + filename)
        file = open(filename, 'r') 
        try:
            page = file.read()
        except UnicodeDecodeError:
            file.close()
            continue
        link = page.split('\n')[1].split('saved from url')[1].split(')')[1].split()[0]
        print(link)

        soup = BeautifulSoup(page, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        print(text)
        file.close()

if __name__ == '__main__':
    main()
