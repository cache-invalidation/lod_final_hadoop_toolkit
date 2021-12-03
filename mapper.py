#!/bin/python3
import sys
from bs4 import BeautifulSoup

def main():
    for page in sys.stdin:
        soup = BeautifulSoup(page, features="html.parser")

        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        print(text)

if __name__ == '__main__':
    main()
