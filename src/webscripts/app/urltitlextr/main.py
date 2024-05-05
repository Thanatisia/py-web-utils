"""
Python Web Scraping using BeautifulSoup(4): Get the YouTube video title by its url using python
"""
import os
import sys
import requests
import json
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool, SimpleQueue, current_process
from ytscripts.utils import remove_tags

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

def progress_bar(curr_index, number_of_urls, bar_opts={"end" : ","}):
    """
    Progress Bar
    """
    ## Calculate percentage increment
    inc_perc = (curr_index / number_of_urls) * 100

    ## Print Progress Bar
    print("Current Progress: {}".format(inc_perc), **bar_opts)

def serial_process_url(urls):
    """
    Iterate through the URL list usign for loop and process each URL, exporting accordingly

    :: Params
    - urls : Specify a list of URLs to iterate through via for loop
        + Type: List
    """
    # Initialize Variables
    file_contents:list = []
    api_res:list = []

    # Iterate through all URLs provided by the user
    for i in range(len(urls)):
        # Get current URL
        url = urls[i]

        # Initialize Variables
        file_content = ""

        # Check if URL is provided
        if url != "":
            # Check if current URL start with a '#'
            if url.startswith('#'):
                # Check if is not the first line
                if i != 0: 
                    ## Write a newline
                    file_content += "\n"

                # Is a comment, append
                file_content += "{}\n".format(url)
            else:
                # Is not a comment, proceed

                ## Initialize API result map for current entry
                api_res.append({
                    "process" : {"id" : i},
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
                        file_content += "{} : {}\n".format(url, title)

                        # Map the status code
                        api_res[curr_res_idx]["content"]["status_code"] = 0
                        # Map the standard output for the HTTP request
                        api_res[curr_res_idx]["request"]["stdout"] = str(link)
                        # Map the obtained title
                        api_res[curr_res_idx]["content"]["title"] = str(title)
                    except Exception as ex:
                        # Error encountered
                        api_res[curr_res_idx]["request"]["stderr"] = str(ex)
                        file_content += "{} : {}\n".format(url, "")
                        print("[-] Error obtaining title: {}\n".format(ex))
                else:
                    # Map the standard error for the HTTP request
                    api_res[curr_res_idx]["request"]["stderr"] = str(response_text)
                    file_content += "{} : {}\n".format(url, "")
                    print("[-] Error sending HTTP GET request ({})\n".format(response_status_code))

        # Append current file content to list
        file_contents.append(file_content)

    # Return/Output
    return [api_res, file_contents]

def multi_process_url(url):
    """
    Process the given URL and export accordingly using multiprocessing for concurrency/parallelism
    """
    global queue, api_res

    # Initialize Variables
    file_contents = ""
    api_res_curr = {}

    # Get current process ID
    curr_proc_id = os.getpid()

    # Check if URL is provided
    if url != "":
        # Convert the task into a string
        url = str(url)

        # Check if current URL start with a '#'
        if url.startswith('#'):
            # Is a comment, append
            ## Write a newline
            file_contents = "\n{}\n".format(url)
        else:
            # Is not a comment, proceed
            print("[i] Current Task: {}".format(url))

            ## Initialize API result map for current entry
            api_res_curr = {
                "process" : {"id" : curr_proc_id},
                "request" : {"stdout" : "", "stderr" : "", "status_code" : -1},
                "content" : {"url" : url, "title"  : "", "status_code" : -1},
            }

            print("[*] Obtaining title of URL [{}]".format(url))

            # Send a HTTP REST API GET request to the youtube URL and return the response stream
            response = requests.get(url)

            # Obtain API response parameters
            response_status_code = response.status_code
            response_text = response.text
            api_res_curr["request"]["status_code"] = response_status_code

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
                    file_contents = "{} : {}\n".format(url, title)

                    # Map the status code
                    api_res_curr["content"]["status_code"] = 0
                    # Map the standard output for the HTTP request
                    api_res_curr["request"]["stdout"] = str(link)
                    # Map the obtained title
                    api_res_curr["content"]["title"] = str(title)
                except Exception as ex:
                    # Error encountered
                    api_res_curr["request"]["stderr"] = str(ex)
                    ## Write to a list
                    file_contents = "{} : {}\n".format(url, "")
                    print("[-] Error obtaining title: {}\n".format(ex))
            else:
                # Map the standard error for the HTTP request
                api_res_curr["request"]["stderr"] = str(response_text)
                file_contents = "{} : {}\n".format(url, "")
                print("[-] Error sending HTTP GET request ({})\n".format(response_status_code))

    # Sleep for 1 second
    time.sleep(1)

    # Perform validation

    # Store the results into the SharedQueue memory object
    return [curr_proc_id, api_res_curr, file_contents]

def multi_execute_tasks(urls):
    global file_contents, api_res

    # Initialize variables
    results = []

    # Initialize/Create a shared queue for use
    shared_queue = SimpleQueue()

    # Create and configure the process pool
    with Pool(initializer=init_worker, initargs=(shared_queue, )) as pool:
        # Generate a Multiprocessing Pool and issue tasks to be executed concurrently/parallely
        proc_ret = pool.map(multi_process_url, urls)
        # _ = pool.map_async(multi_process_url, urls)

        print("Sync completed")

        # Return process data
        results = proc_ret

        # Close the Shared Queue after usage
        shared_queue.close()

        # Close pool after usager
        pool.close()

    return results

def export_titles(titles_list:list, export_filename="titles-list.txt", mode="a+", encoding="utf-8"):
    """
    Export/Write the titles list into a file
    """
    # Open videos output list file for writing
    with open(export_filename, mode, encoding=encoding) as export_file:
        # Iterate through the titles and write to file
        for i in range(len(titles_list)):
            # Get current title
            curr_title = titles_list[i]

            # Strip the newlines if is the first line
            if i == 0:
                # Get current title
                curr_title = curr_title.lstrip()

            # Write to file
            export_file.write(curr_title)

        # Close file after usage
        export_file.close()

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
    with open(res_output_file, "a+", encoding="utf-8") as export_json:
        match res_output_file_extension:
            case "json":
                ## Export the contents to the file pointer/descriptor stream
                # json.dump(results, export_json, indent=4, sort_keys=True)
                json.dump(results, export_json, indent=4)

        # Close file after usage
        export_json.close()

def sanitize_task_results(results):
    """
    Go through all the elements ansd return the api results and the file contents
    """
    global api_res, file_contents

    for row in results:
        # Split current element into variables
        ## Get current process elements
        curr_proc_id = row[0]
        curr_api_res = row[1]
        curr_file_contents = row[2]

        # Sanitize and remove all empty values
        if len(curr_api_res) != 0:
            # Append the entry into the list
            api_res.append(curr_api_res)

        if len(curr_file_contents) != 0:
            # Map the entry to the process ID
            file_contents.append(curr_file_contents)

    # Return
    return [api_res, file_contents]

def sort_by_file(target_file, target_list:list):
    """
    Import a file into a list, sort a list by the contents of the file
    """
    # Initialize Variables
    sort_key = []

    # Open file for reading
    with open(target_file, "r") as read_file:
        # Import file
        sort_key = read_file.readlines()

        # Close file after usage
        read_file.close()

    # Sort the target list by the key
    target_list.sort()

def init_worker(shared_queue):
    """
    Initialize global variables and components for Multiprocessing
    """
    global queue, api_res
    queue = shared_queue
    api_res = [
        # { "request" : {"stdout" : "", "stderr" : "", "status_code" : -1}, "content" : {"url" : url, "title" : "", "status_code" : -1} }
    ]

def init():
    """
    Initialize global variables and components
    """
    global file_contents, api_res
    file_contents = []
    api_res = [
        # { "request" : {"stdout" : "", "stderr" : "", "status_code" : -1}, "content" : {"url" : url, "title" : "", "status_code" : -1} }
    ]

def main():
    global api_res, file_contents
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

    try:
        # Begin processing of URLs
        processing_types = ["serial", "multiprocessing"]
        selected_processing_type = processing_types[1]
        match selected_processing_type:
            case "multiprocessing":
                # Execute the tasks concurrently/parallely and return the results
                results = list(multi_execute_tasks(urls))

                # Sanitize and filter the required parameters from the task results
                api_res, file_contents = sanitize_task_results(results)

            case "serial":
                # Execute the tasks serially using for loop
                api_res, file_contents = serial_process_url(urls)
            case _:
                # Default
                print("Invalid processing type: {}".format(selected_processing_type))

        # Check if there are files to export
        if len(file_contents) > 0:
            # Open a file and export all titles into the file
            export_titles(file_contents)

            # Print JSON result
            export_operation_results(api_res)
        else:
            print("No titles to be exported.")
    except Exception as ex:
        print("Exception: {}".format(ex))

if __name__ == "__main__":
    main()

