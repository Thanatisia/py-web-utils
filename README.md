Network/Web Application Webscraper CLI libraries, utilities and implementations
===============================================================================

## Information
### Description
- Collection of useful webscraper CLI utilities powered by BeautifulSoup
    + With this being based around Video searches and obtaining information via HTML Parsing

### Package
+ Version: v0.5.0

### Scripts
+ urltitlextr : Previously named yt-obtain-url, This is a Simple URL title extractor CLI utility that does 1 thing - extracts title from a given (or set of) URLs and returns it in a new file

### DISCLAIMER
+ This is for educational and for trial and error and testing purposes only
+ Please do not use this for any illegal purposes (if applicable)

## Setup
### Dependencies
+ python
+ python-pip
+ python-venv

### Pre-Requisites
- Create Python Virtual Environment
    - Generate Virtual Environment
        ```bash
        python3 -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux-based
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows-based
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Optionals
    - Append the Virtual Environment directories into system path
        - 'bin' (binaries) directory
            ```bash
            export PATH+="/path/to/[virtual-environment-name]/bin:"
            ```

### Installation
- Install using pip
    ```bash
    pip install git+https://github.com/Thanatisia/py-web-utils
    ```

- Install from requirements.txt
    - Include the project repository url mapped to the package name in 'requirements.txt'
        ```
        web-utils @ git+https://github.com/Thanatisia/py-web-utils
        ```
    - Install python package dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```

- Install locally in development mode
    - Clone repository
        ```bash
        git clone https://github.com/Thanatisia/py-web-utils
        ```
    - Change directory into repository
        ```bash
        cd frameworks/beautifulsoup4/apps/youtube
        ```
    - Install python package dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```
    - (Optional) Uninstall package
        ```bash
        pip uninstall web-utils
        ```
    - Install locally in development mode
        ```bash
        pip install .
        ```

## Documentations

## Resources

## References

## Remarks

