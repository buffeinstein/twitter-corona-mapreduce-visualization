#!/usr/bin/env python3

#SOME CONTEXT 
#server = YEAR = 2020
#the server's '/data/Twitter dataset' folder has 2020's geotagged tweets
#zipfile = DAY
#one day's tweets are in a geoTwitterYY-MM-DD.zip file
#txt file = HOUR
#opening this zip file gets you 24 text files - one per hour of the day 
#line = TWEET
#each text file contains single tweet per line in JSON format (looks like python dictionary) 

# command line args

#this allows us to specify what file we want to run this program on 
#from within the terminal command line


import argparse
parser = argparse.ArgumentParser()
#input_path = zip file (contains many txt files)  we want to run this on 
parser.add_argument('--input_path',required=True)
#if not specified, this will add to the outputs folder
#within the twitter_coronavirus foler
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

# initialize counters
counter_lang = defaultdict(lambda: Counter()) #MAKE LANG DICT
counter_country = defaultdict(lambda: Counter()) #MAKE COUNTRY DICT

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every (txt file = filename) within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file = txt file with tweets in it
        with archive.open(filename) as f:

            # loop over each line in the inner file = loop over tweets
            for line in f:

                # load the tweet as a python dictionary (MAKE TWEET DICT) 
                tweet = json.loads(line)

                # convert text to lower case
                text = tweet['text'].lower()
                
                # search hashtags
                #referring to the list encoded above in this file
                for hashtag in hashtags: 
                    #referring to the dictionary we made (USE TWEET DICT) 
                    lang = tweet['lang']
                    try: 
                        country = tweet['place']['country_code']
                    except: 
                        country = 'unspecified'
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1 #ADD TO LANG DICT
                        counter_country[hashtag][country] +=1
                    counter_lang['_all'][lang] += 1
                    counter_country['_all'][country] += 1



try:
    #make outputs folder
    os.makedirs(args.output_folder)
except FileExistsError:
    pass

#making the path - outputs/___input_base__ (name of zip folder we specified in terminal) 
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

#adding the .lang to the name to show that we're counting the langauges 
output_path_lang = output_path_base+'.lang'

output_path_country = output_path_base+'.country'

print('saving',output_path_lang)
#now that it has a path and name, we can open it as a file and write to it
with open(output_path_lang,'w') as f:
    #and we'll dump the counter_lang dict we made in json format!! done! yay!!
    f.write(json.dumps(counter_lang))

print('saving',output_path_country)
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))


