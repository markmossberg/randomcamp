#!/usr/bin/python

import random, subprocess, urllib, json, sys

def get_url():
    id = random.getrandbits(32)
    usable = str(id)
    #print usable
    # bandcamp isn't giving out dev keys, so I'm just using the sample one
    url = "http://api.bandcamp.com/api/band/3/info?key=vatnajokull&band_id=%s" % usable
    #print url
    return url, usable

for i in range(15): # script tries in bursts of 15 requests
    url, digits = get_url()

    http_req = urllib.urlopen(url)
    resp = http_req.read()
    try:
        response = json.loads(resp)[0]
        print response
        print "Holy sweet mother of fuck, you have defied probability itself and actually found a band. Behold: " + response['results'][0]['name']
    except KeyError:
        print 'Empty Response :( [%s]' % (digits)
