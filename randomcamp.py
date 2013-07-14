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

#for i in range(15): # script tries in bursts of 15 requests
#    url, digits = get_url()
#
#    http_req = urllib.urlopen(url)
#    resp = http_req.read()
#    try:
#        response = json.loads(resp)[0]
#        print response
#        print "Holy sweet mother of fuck, you have defied probability itself and actually found a band. Behold: " + response['results'][0]['name']
#    except KeyError:
#        print 'Empty Response :( [%s]' % (digits)

def rand_words():
    # string constants
    api_key = "32549059d8e5389e4432f22bd79186407ce3eca763cd3564b"
    wordnik_url = "http://api.wordnik.com/v4/words.json/randomWords?maxLength=8"
    wordnik_url = wordnik_url + "&api_key=" + api_key

    # get random words list
    wordnik_req = urllib.urlopen(wordnik_url)
    wordnik_resp = wordnik_req.read()
    wordnik_response = json.loads(wordnik_resp)
    rand_words = []
    for entry in wordnik_response:
        rand_words.append(entry['word'])

    return rand_words

def bcamp_query(list):
    bcamp_url = "http://api.bandcamp.com/api/band/3/search?key=vatnajokull&name="

    # craft query
    for word in list:
        bcamp_url += word + ","
    bcamp_url = bcamp_url[:-1]

    # run bandcamp search
    bcamp_req = urllib.urlopen(bcamp_url)
    bcamp_resp = bcamp_req.read()
    bcamp_response = json.loads(bcamp_resp)
    bcamp_results = bcamp_response['results']
    return bcamp_results

def main():

    word_list = rand_words()
    results = bcamp_query(word_list)

    print word_list
    print
    print results

    #cmd = 'open "' + bcamp_url + '"'
    #print cmd
    #proc = subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    main()
