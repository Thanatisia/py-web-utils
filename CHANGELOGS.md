# CHANGELOGS

## Table of Contents
+ [2024-04-06](#2024-04-06)
+ [2024-04-25](#2024-04-25)
+ [2024-04-30](#2024-04-30)

## Logs
### 2024-04-06
#### 2313H
+ Version: v0.1.0

- Version Changes
    + Initial Commit
    + Added python packaging configuration file 'pyproject.tom;
    + Added new source directory and modules for CLI utility 'yt-obtain-url': Simple Video URL title finder CLI utility

- New
    + Added new document '.gitignore'
    + Added new document 'CHANGELOGS.md'
    + Added new document 'README.md'
    + Added new document 'USAGE.md'
    + Added new document 'pyproject.toml'
    + Added new document 'requirements.txt'
    - Added new directory 'src' for all source codes
        - Added new directory 'ytscripts' for the package 'yt-scripts'
            + Added new module 'utils.py' for general utilities
            - Added new submodule 'yt_obtain_url/' directory: Source code for the CLI utility 'yt-obtain-url'
                + Added new source file 'main.py'

### 2024-04-25
#### 1806H
- Updates
    - Updated document 'USAGE.md'
        + Added documentation for visualizing the JSON file produced with the results
    - Updated main entry point 'main.py' for 'yt-obtain-url' in 'src/ytscripts/yt_obtain_url/'
        - Bug Fixes
        - Dependencies change
            + Added library 'json'
        - Feature Change
            - Added exporting of results to a data serialization configuration file type
                - Currently supporting:
                    + json
            + Added URL Null validation check
            + Added comments validation check (if the line starts with '#')
            + Added Progression messages
            + Added formatted status messages - Successful and Error
            + Added a list container for holding dictionary (key-value) mappings holding results for each URL, which will be outputted to a data file/printed to standard output for analysis

- TODO
    + Add CLI argument parsing for optional parameters
    - Add optional arguments for
        + Verbosity
        + Printing/exporting of JSON file (or Disable)

#### 2058H
+ Version: v0.2.0

- Version Changes
    - yt-obtain-url
        - Bug Fixes
            + Fixed bug where comments are not caught
        - Dependencies change
            + Added library 'json'
        - Feature Change
            - Added exporting of results to a data serialization configuration file type
                - Currently supporting:
                    + json
            + Added URL Null validation check
            + Added comments validation check (if the line starts with '#')
            + Added Progression messages
            + Added formatted status messages - Successful and Error
            + Added a list container for holding dictionary (key-value) mappings holding results for each URL, which will be outputted to a data file/printed to standard output for analysis

- New
    - Added new directory 'docs/' for documentations
        + Added new document 'scripts.md' for holding all scripts/CLI utility and executables in the package

- Updates
    - Updated document 'USAGE.md'
        + Added documentation for visualizing the JSON file produced with the results
    - Updated main entry point 'main.py' for 'yt-obtain-url' in 'src/ytscripts/yt_obtain_url/'
        - Bug Fixes
        - Dependencies change
            + Added library 'json'
        - Feature Change
            - Added exporting of results to a data serialization configuration file type
                - Currently supporting:
                    + json
            + Added URL Null validation check
            + Added comments validation check (if the line starts with '#')
            + Added Progression messages
            + Added formatted status messages - Successful and Error
            + Added a list container for holding dictionary (key-value) mappings holding results for each URL, which will be outputted to a data file/printed to standard output for analysis

- TODO
    + Add CLI argument parsing for optional parameters
    - Add optional arguments for
        + Verbosity
        + Printing/exporting of JSON file (or Disable)

### 2024-04-30
#### 2056H
+ Version: v0.3.0

- Version Changes
    - yt-obtain-url
        - Bug Fixes
        - Dependencies change
            + Added library 'multiprocessing'
        - Feature Change
            + Added multiprocessing functionalities
            + Added progress bar function
            + Added function 'multi_process_url()' for processing the URLs list elements concurrently/parallely
            + Added function 'multi_execute_tasks()' for generating/creating the Multiprocessing Pool to hold the 'pool' of 'tasks' (effectively every element of the iterable/list is a single task) that will be executing concurrently/parallely, and return the results of each task to a 'results' list
            + Added function 'sanitize_task_results()' for sanitizing and processing all the results of 'multi_execute_tasks()' and return the 'api_res' and 'file_contents' list objects
            + Added function 'serial_process_url()' for processing the URLs list elements using for loop (consecutively/iteratively, hence, serial)
            + Added function 'export_titles()' to export/write the resulting titles list into a file
            + Moved the main() function logic into the respecitve functions for cleaner code
            + Added switch-case to switch between executing the URL reading serially via for loop, or multiprocessing
    - Debugging and Testing
        - Added new benchmark scripts into the testing toolkit/chain
            + benchmark-communicate.py : For benchmarking the execution of commands using 'Popen.communicate()'
            + benchmark-for-loop.py : For benchmarking the execution of commands by iterating through lines from 'Popen.stdout' as a list
            + benchmark-real-time.py : For benchmarking the execution of commands and printing each line in real time (latency and speed dependends on system buffer)

- New
    - Added new benchmark scripts into 'test' directory
        + benchmark-communicate.py : For benchmarking the execution of commands using 'Popen.communicate()'
        + benchmark-for-loop.py : For benchmarking the execution of commands by iterating through lines from 'Popen.stdout' as a list
        + benchmark-real-time.py : For benchmarking the execution of commands and printing each line in real time (latency and speed dependends on system buffer)

- Updates
    - Updated document 'README.md'
        + Updated version to 'v0.3.0'
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.3.0'
    - Updated document 'scripts.md' in 'docs/'
        + Updated version to 'v0.3.0'
    - Updated document 'USAGE.md'
        + Updated documentation to be more generic
        + Added documentation for piping and streaming data into yt-obtain-url
    - Updated main entry point 'main.py' for 'yt-obtain-url' in 'src/ytscripts/yt_obtain_url/'
        - Bug Fixes
        - Dependencies change
            + Added library 'multiprocessing'
        - Feature Change
            + Added multiprocessing functionalities
            + Added progress bar function
            + Added function 'multi_process_url()' for processing the URLs list elements concurrently/parallely
            + Added function 'multi_execute_tasks()' for generating/creating the Multiprocessing Pool to hold the 'pool' of 'tasks' (effectively every element of the iterable/list is a single task) that will be executing concurrently/parallely, and return the results of each task to a 'results' list
            + Added function 'sanitize_task_results()' for sanitizing and processing all the results of 'multi_execute_tasks()' and return the 'api_res' and 'file_contents' list objects
            + Added function 'serial_process_url()' for processing the URLs list elements using for loop (consecutively/iteratively, hence, serial)
            + Added function 'export_titles()' to export/write the resulting titles list into a file
            + Moved the main() function logic into the respecitve functions for cleaner code
            + Added switch-case to switch between executing the URL reading serially via for loop, or multiprocessing

- TODO
    + Add CLI argument parsing for optional parameters
    - Add optional arguments for
        + Verbosity
        + Printing/exporting of JSON file (or Disable)

