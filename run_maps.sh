#map.py works on a single zip file = 1 day 
#this script will feed in all the zip files from 2019 to map.py 

for file in /data/Twitter\ dataset/geoTwitter19-01-0*.zip; do
    ./src/map.py --input_path="$file" &
done 

