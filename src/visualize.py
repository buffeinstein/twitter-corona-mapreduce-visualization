#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

path = args.input_path

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

languages = [item[0] for item in items[:10]]  # Take the first 10 languages
counts = [item[1] for item in items[:10]]  # Take the corresponding counts

languages.reverse()
counts.reverse() 
#
#print ('lang=', languages)
#print ('counts=', counts) 
#
# Create a vertical bar graph
plt.bar(range(len(languages)), counts, tick_label=languages)

'''
items = items[:10]
items.reverse()

plt.bar([item[0] for item in items[:10]], [item[1] for item in items[:10]])
'''
plt.xlabel('Languages')
plt.ylabel('Counts')
plt.title('Top 10 countries that used ' + args.key + ' in 2020')  
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()

tag = args.key[1:]
# Display the plot
if path[-4:] == 'lang':
    plt.savefig(tag + 'language_count.png', format='png')  # Save as PNG image
else:
    plt.savefig(tag + 'country_count.png', format='png')

#print (type(items))
#print (items)
#print (items[1])
#print (type(items[1]))
#
#for k,v in items[:10]:
#    print(k,':',v)
#
