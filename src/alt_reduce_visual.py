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
ax.set_xlabel('Year of 2020')
ax.set_ylabel('Amount Of Tweets With Hashtag')
ax.set_title('International Daily Use Of'+tags)

# Add a legend to the plot
ax.legend()
plt.savefig('daily_use_of_'+tags+'2.png')


#input_paths = the paths in outputs (select with *.lang or *.zip)
#keys = hashtags

#items is a list, with tuples in each index.
#the tuple has (language/country, count)

#reduced.lang and reduced.country is what we were running visualize.py on
#which separates the reducing steps and the visualizing step
#creating a bar graph that depicts the final information from the whole year

#but now, we want a line chart that shows the progress of the use of the hashtag
#which requires day-by-day analysis
#and thus we cannot separate the reduce and visualize steps the same way

#instead, we will open up all the .lang files in the outputs folder
#and extract the use of the hashtag
#nad extract the use of the hashtag
