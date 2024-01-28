#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests import get
    import sys

    url = "https://api.github.com/user"

    uname = sys.argv[1]
    passw = sys.argv[2]

    response = get(url, auth=(uname, passw))
    txt_json = response.json()

    print(txt_json.get('id'))
