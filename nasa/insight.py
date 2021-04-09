#!/usr/bin/env python3
""" AJRodriguez | Using Authorization key for API"""

# python3 -m pip install requests
import requests

def apikey():
    """returns a str containing our api key"""
    with open("/home/student/nasa.cred", "r") as nc: #opens this file to read the api key
        apikey = nc.readline() # returns the first line in a file
        #print(apikey)
        return apikey.rstrip("\n") #returns first line of file with trailing white space removed

def main():
    """run-time code"""
    # our var apikey will be defined by the results of apikey() function call above
    api = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={apikey()}"# if appi requires more key/value pairs, tweak                                                                    # this
    # sends HTTP GET to our API
    nasaresp = requests.get(api)
    
    # we now have a 200 + JSON response
    nasajson = nasaresp.json()# strips JSON off our response

    #print(nasajson)
    print(nasajson.get("photos")[0].get("img_src"))
    print(nasaresp.status_code)
if __name__ == "__main__":
    main()
