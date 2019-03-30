"""
freelib.py

Piratebox Free Little Library Maker

Grab .html files from the Gutenberg project, generate .html files for Piratebox library
"""

import os
import requests
from bs4 import BeautifulSoup
import sources
import time


def get_response(url):
    response = requests.get(url)
    print("Getting:", url, response)
    return response


def make_soup(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    return soup


def add_meta_tag(soup):
    # Add tag for improved display on mobile devices
    # <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width">
    tag = soup.new_tag('meta')
    tag.attrs['name'] = 'viewport'
    tag.attrs['content'] = "initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width"
    soup.head.append(tag)

    # Add tag for handling utf chars
    # <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    tag_1 = soup.new_tag('meta')
    tag_1.attrs['http-equiv'] = "Content-Type"
    tag_1.attrs['content'] = "text/html; charset=UTF-8"
    soup.head.append(tag_1)

    return soup


def modify_anchor_tags(soup):
    """
    Get all anchor tags, if they have an href, modify to remove any base url references.
    This is to ensure that Table-of-Contents type links to the page itself redirect properly.
    """
    for anchor in soup.findAll('a'):
        try:
            href = anchor['href']
        except KeyError as err:
            continue
        split = href.split('#')
        anchor['href'] = '#' + split[-1]
    return soup


def write_soup_to_file(soup, file_name):
    ext = '.html'
    file_name = file_name + ext
    output_dir_name = 'output'

    if not os.path.exists(output_dir_name):
        os.mkdir(output_dir_name)

    path = os.path.join(output_dir_name, file_name)
    print("    Writing:", path)
    with open(path, 'w') as f:
        f.write(str(soup))


def main():
    for item in sources.source_list:
        url = item[0]
        name = item[1]

        response = get_response(url)
        if response.status_code != 200:
            print(f"Error response {response.status_code} getting: " + str(item))
            continue

        soup = make_soup(response.text)
        add_meta_tag(soup)
        modify_anchor_tags(soup)
        write_soup_to_file(soup, name)
        time.sleep(1)


if __name__ == '__main__':
    main()



