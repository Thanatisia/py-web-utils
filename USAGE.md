USAGE
=====

## Documentations

*Tools*
-------
+ yt-obtain-url : Simple YouTube URL title finder CLI utility


## CLI utilities

> yt-obtain-url

*Synopsis/Syntax*
-----------------
- Default
    ```bash
    yt-obtain-url [yt-url-string]
    ```

*Parameters*
------------
- Positionals
    - yt-url-string : Specify the target video URL you wish to search the title of
        + Type: String
- Optionals
    - With Arguments
    - Flags

*Usage*
-------
- Obtain the title of a specified URL link
    - Notes
        - Parse a URL string into the CLI utility argument and
            + the application will output the youtube URL mapped to the title in a text file
    ```bash
    yt-obtain-url [youtube-url-link]
    ```

- Streaming a file of links into the application's standard input stream
    - Prepare a file (currently statically set as 'in-links.txt'
        - Notes
            + Prepend/Start the string with a '#' delimiter to comment out the url, this will be treated as a comment string
        ```
        # header/comment
        url-1-here
        url-2-here
        url-3-here
        url-4-here
        url-5-here
        ```
    - Stream the file into the application as standard input
        ```bash
        yt-obtain-url < filename.txt
        ```

- Pipe the contents of a file of links into the application
    - Prepare a file (currently statically set as 'in-links.txt'
        - Notes
            + Prepend/Start the string with a '#' delimiter to comment out the url, this will be treated as a comment string
        ```
        # header/comment
        url-1-here
        url-2-here
        url-3-here
        url-4-here
        url-5-here
        ```
    - Pipe the contents of the file into the application
        ```bash
        cat filename.txt | yt-obtain-url
        ```

## Importing/Embedding as a library/module

*Library*
---------

### Package
- ytscripts : Collection of YouTube-focused Webscraping CLI utilities, implementation libraries and frameworks for using as an API in your own application

### Modules
- ytscripts
    - core : Core logic library/framework containing classes for each utilities (WIP)
    - utils : Contains general utilities

### Classes

### Functions
- ytscripts.utils
    - `.remove_tags(text, tags=None)`: Cleanup and Sanitize result output by removing tags
        - Parameter/Argument Signatures
            - text : Your text to remove tags
                Type: String

            - tags : List containing your opening tag and closing tag to remove from the text
                + Type: List
                - Notes
                    + Ensure that there are only 2 elements in the list - the opening tag and the closing tag
        - Return
            - text: The 'cleaned' output string with the specified list of tags removed
                + Type: String

### Data Classes/Types

### Attributes/Variables Objects

*Usage*
-------
- Import python package
    - General utilities
        ```python
        from ytscripts.utils import remove_tags
        ```
    - yt-obtain-url source
        ```python
        from ytscripts import yt_obtain_url
        ```

- Initialize Variables
    ```python
    # Initialize Variables
    ```

- Initialize Module Classes

- Remove tags from a HTML tag text
    ```python
    text = remove_tags(text, ["<tag>", "</tag>"])
    ```

## Wiki

### Use Cases
- yt-obtain-url : Usable in scenarios involving the filtering of the title of a video URL (youtube or not)
    - Converting an archive list of video URLs into its file names
        - Preparing an archive list of video URLs
            ```
            url-1
            url-2
            url-3
            url-N
            ```
        - Stream the input list as an input stream into yt-obtain-url
            + and output the URL mapped to the title in an output file
            ```bash
            yt-obtain-url < input-list.txt
            ```
        - Pipe the contents of the input list into yt-obtain-url
            ```bash
            cat input-list.txt | yt-obtain-url
            ```

- Visualizing the JSON file
    - Using jq to filter
        - Obtain all 'content' keys in each row
            ```bash
            cat output.json | jq .[].content
            ```
        - Obtain all 'content' keys in each row and print in raw (No quoted strings)
            ```bash
            cat output.json | jq -r .[].content
            ```
        - Filter all 'content' keys in each row and print out the title, followed by the URL
            ```bash
            cat output.json | jq '.[].content | .title, .url'
            ```

## Resources

## References

## Remarks

