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

x_var = [item[0] for item in items[:10]]  # Take the first 10 languages

counts = [item[1] for item in items[:10]]  # Take the corresponding counts

x_var.reverse()
counts.reverse() 


if path[-4:] == 'lang':
    label = 'Languages'
else: 
    label = 'Countries'

# Create a vertical bar graph
plt.bar(range(len(x_var)), counts, tick_label=x_var)
plt.xlabel(label)
plt.ylabel('Counts')
plt.title('Top 10 languages That Used ' + args.key + ' In 2019')  
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()

tag = args.key[1:]
# Display the plot
plt.savefig(tag + label  +'Count.png', format='png')  # Save as PNG image

