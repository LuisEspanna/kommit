import requests
import sys

def start_loadin(key, table):

    tables = requests.get(url='http://swapi.dev/api')
    tables = tables.json()

    if(table in tables):
        http_url = 'https://swapi.dev/api/' + table

        print("/" * 100)
        print(http_url)
        print("/" * 100)

        r = requests.get(url=http_url)

        for object in r.json()['results']:
            keys = key.split(",")
            for i in keys:
                if (i != "*"):
                    if (i in object):
                        print(object[i], end=' , ')
                    else:
                        print("ERROR!")
                        print(i + " not found in " + str(object))
                else:
                    for param in object:
                        print(str(param) + " : " + str(object[param]))
            print("")
            print("-" * 100)
    else:
        print("Table not found")


if __name__ == '__main__':

    if(len(sys.argv) > 1):
        start_loadin(sys.argv[2], sys.argv[4])
    else:
        start_loadin("name", "people")