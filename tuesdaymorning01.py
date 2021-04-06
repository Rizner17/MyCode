#!/usr/bin/env python3

"""AJRodriguez | tuesday morning practice
Given the data contained within issnow, available from:
    http://api.open-notify.prg/iss-now.json
write a program that displays:

At <timestamp> the ISS is:
    Longitude - <longitude>
    Latitude - <latitude>
"""

def main():
    #Source data
    issnow = {"message": "success", "timestamp": 1617722150, "iss_position": {"longitude": "135.9156", "latitude": "-41.0150"}}

    #my code
    #print(At <timestamp> the ISS is:)
    print("At, ", issnow.get("timestamp"), " the ISS is: ")
    
    #print"Longitude"
    print("Longitude - ", issnow.get("iss_position").get("longitude"))

    #print "Latitude"
    print("Latitude - ", issnow.get("iss_position").get("latitude"))
   
main()
