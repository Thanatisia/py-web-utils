"""
Python Web Scraping using BeautifulSoup(4): Get the YouTube video title by its url using python
"""
import os
import sys
import requests
import json
from ytscripts.utils import remove_tags
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

def export_operation_results(results:list, res_output_file="output.json"):
    """
    Print the results of the main application thread operations

    :: Params
    - results : A List containing rows of dictionary (key-value) mapping containing the results of the main application's stream
        + Type: List of Dictionaries
        - Format
            ```
            [
                {
                    "request" : {"stdout" : "", "stderr" : "", "status_code" : -1},
                    "content" : {"url" : url, "title" : "", "status_code" : -1}
                },
            ]
            ```

    - res_output_file : Specify the output file to export the results dictionary to
        + Type: String
        + Default: output.json
        - Supported File Types
            + json
    """
    # Get file definitions (path, nametype/extension)
    res_output_file_name_path = res_output_file.split("/")
    if len(res_output_file_name_path) > 0:
        res_output_file_path = res_output_file_name_path[:-2] # Get all elements up to the 2nd last item
        res_output_file_name = res_output_file_name_path[::-1][0] # Get the last element
    else:
        res_output_file_path = "."
        res_output_file_name = res_output_file_name_path[0]
    res_output_file_extension = res_output_file_name.split(".")[1]

    # Open file IO stream for use
    with open(res_output_file, "a+") as export_json:
        match res_output_file_extension:
            case "json":
                ## Export the contents to the file pointer/descriptor stream
                json.dump(results, export_json, indent=4, sort_keys=True)

        # Close file after usage
        export_json.close()

def init():
    """
    Initialize global variables and components
    """
    global api_res
    api_res = [
        # { "request" : {"stdout" : "", "stderr" : "", "status_code" : -1}, "content" : {"url" : url, "title" : "", "status_code" : -1} }
    ]

def main():
    # Initialize Variables
    yt_url = ""
    urls = []

    # Initialize global components
    init()

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

            # Check if URL is provided
            if url != "":
                # Check if current URL start with a '#'
                if url.startswith('#'):
                    # Check if is not the first line
                    if i != 0: 
                        ## Write a newline
                        write_videos_list.write("\n")

                    # Is a comment, append
                    write_videos_list.write(url)
                    write_videos_list.write("\n")
                else:
                    # Is not a comment, proceed

                    ## Initialize API result map for current entry
                    api_res.append({
                        "request" : {"stdout" : "", "stderr" : "", "status_code" : -1},
                        "content" : {"url" : url, "title"  : "", "status_code" : -1},
                    })
                    curr_res_idx = len(api_res)-1

                    print("[*] Obtaining title of URL [{}]".format(url))

                    # Send a HTTP REST API GET request to the youtube URL and return the response stream
                    response = requests.get(url)

                    # Obtain API response parameters
                    response_status_code = response.status_code
                    response_text = response.text
                    api_res[curr_res_idx]["request"]["status_code"] = response_status_code

                    # Check if response status code is 200 (OK)
                    if response_status_code == 200:
                        ## Try to parse the HTML response string and find all the titles
                        try:
                            # Initialize BeautifulSoup to crawl the response text HTML5 code
                            soup = BeautifulSoup(response_text, features="html.parser")

                            # Find all occurences of the title which is the link
                            link = soup.find_all(name="title")[0]

                            # Obtain the text returned (the title)
                            title = link.text

                            # Cleanup and Sanitize result output
                            title = remove_tags(title, ["<title>", "</title>"]).strip()

                            # Output
                            print("[+] Title received: {}\n".format(title))

                            ## Write to a list
                            write_videos_list.write("{} : {}".format(url, title))

                            ## Write a newline
                            write_videos_list.write("\n")

                            # Map the status code
                            api_res[curr_res_idx]["content"]["status_code"] = 0
                            # Map the standard output for the HTTP request
                            api_res[curr_res_idx]["request"]["stdout"] = str(link)
                            # Map the obtained title
                            api_res[curr_res_idx]["content"]["title"] = str(title)
                        except Exception as ex:
                            # Error encountered
                            api_res[curr_res_idx]["stderr"] = str(ex)
                            print("[-] Error obtaining title: {}\n".format(ex))
                    else:
                        # Map the standard error for the HTTP request
                        api_res[curr_res_idx]["request"]["stderr"] = str(response_text)
                        print("[-] Error sending HTTP GET request ({})\n".format(response_status_code))

        ## Close file after usage
        write_videos_list.close()

        # Print JSON result
        export_operation_results(api_res)

if __name__ == "__main__":
    main()

