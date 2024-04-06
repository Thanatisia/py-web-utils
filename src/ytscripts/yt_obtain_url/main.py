"""
Python Web Scraping using BeautifulSoup(4): Get the YouTube video title by its url using python
"""
import os
import sys
from ytscripts.utils import remove_tags
import requests
from bs4 import BeautifulSoup

def get_cli_arguments():
    """
    Get CLI arguments
    """
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    return [argv, argc]

def process_cli_arguments(argv, argc):
    """
    Process the obtained CLI arguments
    """
    # Initialize variables
    url = ""

    # Check if required arguments exists
    if argc >= 1:
        # Parse in required configuration files
        url = argv[0:]

    # Output
    return url

def main():
    # Initialize Variables
    yt_url = ""
    urls = []

    # Use stdin stream if its full
    if not sys.stdin.isatty():
        in_stream = sys.stdin

        # Process standard input
        for line in in_stream:
            # Sanitize current line
            line = line.strip()

            # Append into urls list
            urls.append(line)
    else:
        # Get CLI arguments
        argv, argc = get_cli_arguments()

        # Process CLI arguments
        urls = process_cli_arguments(argv, argc)

    print("URLs: {}".format(urls))

    # Open videos output list file for writing
    with open("videos-list.txt", "a+") as write_videos_list:
        # Iterate through all URLs provided by the user
        for i in range(len(urls)):
            # Get current URL
            url = urls[i]

            # Send a HTTP REST API GET request to the youtube URL and return the response stream
            response = requests.get(url)

            # Initialize BeautifulSoup to crawl the response text HTML5 code
            soup = BeautifulSoup(response.text, features="html.parser")

            # Find all occurences of the title which is the link
            link = soup.find_all(name="title")[0]

            # Obtain the text returned (the title)
            title = link.text

            # Cleanup and Sanitize result output
            title = remove_tags(title, ["<title>", "</title>"])

            # Output

            ## Write to a list
            write_videos_list.write("{} : {}".format(url, title))

            ## Write a newline
            write_videos_list.write("\n")

        ## Close file after usage
        write_videos_list.close()

if __name__ == "__main__":
    main()

