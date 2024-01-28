#!/usr/bin/python3
"""Sends a request to the URL and
displays the body of the response.
"""


if __name__ == "__main__":
    from requests import get
    import sys

    response = get(sys.argv[1])
    status = response.status_code
    e_text = 'Error code: {}'
    print(e_text.format(status) if (status >= 400) else response.text)
