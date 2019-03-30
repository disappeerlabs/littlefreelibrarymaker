# Piratebox Little Free Library

A simple script to checkout .html books from the Gutenberg Project
and generate .html files that can be read locally and/or dropped into 
a Piratebox file share. These .html output files are slightly edited
to optimize viewing on mobile devices and clean up errant utf characters.

## Requirements
Basic Requirements:

- Python >= 3.5 for print error formatting. 
- BeautifulSoup4
- Requests

You can install these in the usual way from the project director into your virtualenv: 

`pip install -r requirements`


## Usage
To grab a book or set of books from the Gutenberg project, simply edit
your `sources.py` file by adding the requisite information to the `sources_list`.

The `sources_list` is a list of tuples containing two strings:
 
 `(GUTENBERG_BOOK_HTML_URL, NAME_OF_OUTPUT_HTML_FILE)`

After you have updated your `sources_list`, simply run the script:

`python freelib.py`

The newly generated .html files will be written to a folder called `output`
in the project's working directory. You can then view these files on your local machine
and copy them over to your Piratebox files share folder. 

## Caveats

If you have a large sources list, you should make sure you read the Gutenberg Project's 
[rules for robot access](https://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages).

By default, the main loop sleeps for 1 second between requests.

If the .html source file contains images, these will not be downloaded. Many Gutenberg 
project books contain multiple links, one with images and one without.

## License
GPLv3