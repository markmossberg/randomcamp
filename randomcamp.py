#!/usr/bin/python

# Mark Mossberg
# Finds almost-random bands on Bandcamp to help people find new music and support artists.

import random, subprocess, urllib, json, sys

### functions ##########

def rand_words():
    # string constants
    api_key = "32549059d8e5389e4432f22bd79186407ce3eca763cd3564b"
    wordnik_url = "http://api.wordnik.com/v4/words.json/randomWords?limit=12&maxLength=8"
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

    def run_bcamp_search(url):
        bcamp_results = []

        try: # sometimes there's a weird error with the wordnik api
            bcamp_req = urllib.urlopen(url)
            bcamp_resp = bcamp_req.read()
            bcamp_response = json.loads(bcamp_resp)
            bcamp_results = bcamp_response['results']
        except:
            pass # i know, i know :/
        finally:
            return bcamp_results

    # craft query
    bcamp_url = "http://api.bandcamp.com/api/band/3/search?key=vatnajokull&name="
    for word in list:
        bcamp_url += word + ","
    bcamp_url = bcamp_url[:-1]

    # run bandcamp search
    query_results = run_bcamp_search(bcamp_url)

    return query_results

def get_bandcamp_results():
    word_list = rand_words()
    bcamp_results = bcamp_query(word_list)

    # if words are weird enough, bandcamp returns nothing
    if len(bcamp_results) == 0:
        while len(bcamp_results) == 0:
            word_list = rand_words()
            bcamp_results = bcamp_query(word_list)
    return bcamp_results

def osx():
    results = get_bandcamp_results()

    # gets band's url
    selection = random.randint(0,len(results)-1)
    chosen_band = results[selection]
    band_subdomain = chosen_band['subdomain']
    band_url = "http://%s.bandcamp.com" % (band_subdomain)

    # opens it in default browser
    osx_cmd = 'open "%s"' % (band_url)
    subprocess.call(osx_cmd, shell=True)

def win():
    results = get_bandcamp_results()

    # gets band's url
    selection = random.randint(0,len(results)-1)
    chosen_band = results[selection]
    band_subdomain = chosen_band['subdomain']
    band_url = "http://%s.bandcamp.com" % (band_subdomain)

    # opens it in default browser
    win_cmd = 'start %s"' % (band_url)
    subprocess.call(win_cmd, shell=True)

def other_os(results):
    results = get_bandcamp_results()
    selection = random.randint(0,len(results)-1)
    chosen_band = results[selection]
    chosen_band_url = chosen_band['url']
    print "Bands:"
    print "%s: %s" % (chosen_band, chosen_band_url)

### main ##########

def main():

    # check args
    if len(sys.argv) == 1:
        print """
Randomcamp, by Mark Mossberg
A small tool to help you discover new artists on Bandcamp.
        """
        raw_input('I recommend that you have your default web browser open at this point. \nPress <Enter> to continue.\n')
        num_bands = raw_input("Number of bands you want to discover: ")
    else:
        num_bands = sys.argv[1]

    try:
        num_bands = int(num_bands)
    except ValueError:
        raw_input("Argument needs to be int value. Exiting on <Enter>...")
        sys.exit()

    # main stuff
    for i in range(num_bands):
        if sys.platform == 'darwin':
            osx()
        elif sys.platform.startswith('win'):
            win()
        else:
            other_os()

    if sys.platform.startswith('win'):
        raw_input("\nDone!")
    else:
        print "Done!"

if __name__ == '__main__':
    main()
