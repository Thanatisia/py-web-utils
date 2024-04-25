# CHANGELOGS

## Table of Contents
+ [2024-04-06](#2024-04-06)
+ [2024-04-25](#2024-04-25)

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

