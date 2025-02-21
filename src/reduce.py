#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        # python dictionaries are the same format as json files
        # thus, we can load it as a json file 
        tmp = json.load(f)

        # and merge counters
        for k in tmp:
            total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))




