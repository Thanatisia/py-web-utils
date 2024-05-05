# CHANGELOGS

## Table of Contents
+ [2024-04-06](#2024-04-06)
+ [2024-04-25](#2024-04-25)
+ [2024-04-30](#2024-04-30)
+ [2024-05-05](#2024-05-05)

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

#### 2119H
- Updates
    - Updated main entry point 'main.py' for 'yt-obtain-url' in 'src/ytscripts/yt_obtain_url/'
        - Bug Fixes
            + Fixed an encoding issue
            - Fixed an issue where due to the nature of concurrency, parallelism and multiprocessing, there will be desynchronization in the input data stream and the output data stream
                + Used the task's system process ID as an anchor point
        - Dependencies change
            + Added library 'time'
        - Feature Change
            + Added obtaining of process ID for multiprocess tasks (Serial processing via for loop will use the index of the loop instead)
            + Replaced the usage of Shared Queues to store results of a task from multiprocessing with just returning a list containing `[current-process-id, api-results, file-contents]`
            + Replaced async (map.async) pool execution with sync (map)
            + Added encoding to 'export_titles()' to solve an encoding issue when used with Windows
            + Removed 'sort_keys=True' from json.dump so that the json dumper does not automatically sort on export
            + Added function 'sort_by_file()' (UNUSED)
            + Added output title length validation

#### 2131H
+ Version: v0.4.0

- Version Changes
    - yt-obtain-url
        - Bug Fixes
            + Fixed an encoding issue
            - Fixed an issue where due to the nature of concurrency, parallelism and multiprocessing, there will be desynchronization in the input data stream and the output data stream
                + Used the task's system process ID as an anchor point
        - Dependencies change
            + Added library 'time'
        - Feature Change
            + Added obtaining of process ID for multiprocess tasks (Serial processing via for loop will use the index of the loop instead)
            + Replaced the usage of Shared Queues to store results of a task from multiprocessing with just returning a list containing `[current-process-id, api-results, file-contents]`
            + Replaced async (map.async) pool execution with sync (map)
            + Added encoding to 'export_titles()' to solve an encoding issue when used with Windows
            + Removed 'sort_keys=True' from json.dump so that the json dumper does not automatically sort on export
            + Added function 'sort_by_file()' (UNUSED)
            + Added output title length validation

- Updates
    - Updated document 'README.md'
        + Updated version to 'v0.4.0'
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.4.0'
    - Updated document 'scripts.md' in 'docs/'
        + Updated version to 'v0.4.0'
    - Updated main entry point 'main.py' for 'yt-obtain-url' in 'src/ytscripts/yt_obtain_url/'
        - Bug Fixes
            + Fixed an encoding issue
            - Fixed an issue where due to the nature of concurrency, parallelism and multiprocessing, there will be desynchronization in the input data stream and the output data stream
                + Used the task's system process ID as an anchor point
        - Dependencies change
            + Added library 'time'
        - Feature Change
            + Added obtaining of process ID for multiprocess tasks (Serial processing via for loop will use the index of the loop instead)
            + Replaced the usage of Shared Queues to store results of a task from multiprocessing with just returning a list containing `[current-process-id, api-results, file-contents]`
            + Replaced async (map.async) pool execution with sync (map)
            + Added encoding to 'export_titles()' to solve an encoding issue when used with Windows
            + Removed 'sort_keys=True' from json.dump so that the json dumper does not automatically sort on export
            + Added function 'sort_by_file()' (UNUSED)
            + Added output title length validation

- TODO
    + Add CLI argument parsing for optional parameters
    - Add optional arguments for
        + Verbosity
        + Printing/exporting of JSON file (or Disable)

### 2024-05-05
#### 0748H
- Renaming the project from 'py-webscraper-yt' to 'py-web-utils'
    - The intent is to generalize the project into a Web/URL-holding utility package (i.e. via webscraping) 
        + since it has went from being a specifically-youtube webscraper 
        + into a holding general network-focused collection

- New
    + Created new directory 'app' in 'src/ytscripts' to store all project application layer source codes
    + Created new directory 'core' in 'src/ytscripts' to store all project core utilities

- Updates
    + Moved module 'utils.py' from 'src/ytscripts' => 'src/ytscripts/core'
    + Moved project application source directory 'yt-obtain-url' from 'src/ytscripts' => 'src/ytscripts/app/'
    + Renamed project application 'yt-obtain-url' => 'urltitlextr' (URL title eXtractor)


#### 0931H
- Updates
    + Renamed package 'ytscripts' => 'webscripts'
    - Updated document 'README.md'
        + Edited occurences of 'yt-obtain-url' => 'urltitlextr'
        + Updated setup documentations
    - Updated python packaging configuration file 'pyproject.toml'
        + Replaced package and script entry points
    - Updated document 'scripts.md' in 'docs/'
        + Replaced 'yt-obtain-url' => 'urltitlextr'

