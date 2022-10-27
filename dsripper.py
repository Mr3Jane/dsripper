#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import io
import requests

from lib.dsstore.dsstore import DS_Store

def rip_store(root_dir_url, path=""):
    current_store = root_dir_url.rstrip("/") + "/.DS_Store"
    
    response = requests.get(current_store)
    if response.status_code == 200:
        store_file = io.BytesIO(response.content) 
        store = DS_Store(store_file.read(), debug=False)
        files = set(store.traverse_root())
        for file in files:
            if(file != "."):
                new_path = path + "/" + file
                yield new_path
                yield from rip_store(root_dir_url.rstrip("/") + "/" + file, new_path)

def main():
    parser = argparse.ArgumentParser(description='Recursive .DS_Store ripper')
    parser.add_argument('-u', '--url',
                        metavar='url',
                        required=True,
                        help='Full URI to .DS_Store file or its directory')
    parser.add_argument('-iu', '--include-url',
                        dest='include_url',
                        action='store_true',
                        help='Set to print full URL')

    args = parser.parse_args()
    
    root_store = args.url
    root_dir = root_store.rstrip('.DS_Store')
    
    for file in rip_store(root_dir):
        if(args.include_url):
            print(root_dir, end='')

        print(file.lstrip("/"))


if __name__ == "__main__":
    main()
