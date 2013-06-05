#!/usr/bin/python

import random, subprocess

def get_url():
    id = random.getrandbits(32)
    usable = str(id)
    #print usable
    # bandcamp isn't giving out dev keys, so I'm just using the sample one
    url = "http://api.bandcamp.com/api/band/3/info?key=vatnajokull&band_id=%s&debug" % usable
    #print url
    return url, usable

for i in range(15): # script tries in bursts of 15 requests
    url, digits = get_url()
    #cmd = 'open "%s"' % url
    cmd = 'curl -s "%s"' % url
    obj = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    out = obj.communicate()[0]
    if out != '{\n}\n': # if there's anything there, print it
        print out
    else: # if not, say so, and the ID used 
        print 'Nope: %d, %s' % (i, digits)
