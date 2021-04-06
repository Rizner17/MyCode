#!/usr/bin/env python3

# required to make HTTP requests
import requests

def main():

    # api goes here
    # example:
    # api = http://api.open-notify.org/astros.json
    api = "https://pokeapi.co/api/v2/pokemon/charmander"

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()

    # display ALL of the data we captured
    ##print(respdata)
    print(respdata.get("abilities"))

    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)

main()
