"""
General HTML utilities
"""
import os
import sys

def remove_tags(text, tags=None):
    """
    Cleanup and Sanitize result output by removing tags

    :: Params
    - text : Your text to remove tags
        Type: String

    - tags : List containing your opening tag and closing tag to remove from the text
        + Type: List
        - Notes
            + Ensure that there are only 2 elements in the list - the opening tag and the closing tag
    """
    if tags != None and len(tags) == 2:
        for tag in tags:
            text = text.replace(tag, "")

    return text

