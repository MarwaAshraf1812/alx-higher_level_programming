#!/usr/bin/python3
"""sends a request to the URL and
displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    from requests import get
    import sys

    url = get(sys.argv[1])
    print(url.headers.get('X-Request-Id'))
