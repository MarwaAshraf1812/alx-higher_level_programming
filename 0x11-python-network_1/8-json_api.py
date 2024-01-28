#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    from requests import post
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = post(url, data={'q': q})

    resp_type = response.headers['content-type']

    if resp_type and 'application/json' in resp_type:
        try:
            result = response.json()
            if result:
                print("[{}] {}".format(result['id'], result['name']))
            else:
                print('No result')
        except ValueError:
            print("Not a valid JSON")
