import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            #up till this point, this ^^ code was in reduce 
            if k in args.keys:
                total[k][path[21:26]] += sum(tmp[k].values())

#and this is the same as visualize code 
fig, ax = plt.subplots()
for k in total.keys():
    #summing 
    ax.plot(total[k].keys(),total[k].values(),label = f'{k}')

tags = ''
for tag in args.keys: 
    tags += str(tag)

# Configure plot details
ax.set_xlabel('Year of 2019')
ax.set_ylabel('Amount Of Tweets With Hashtag')
ax.set_title('International Daily Use Of'+tags)

# Add a legend to the plot
ax.legend()
plt.savefig('daily_use_of_'+tags+'2.png')


