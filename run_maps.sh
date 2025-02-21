#map.py works on a single zip file = 1 day 
#this script will feed in all the zip files from 2019 to map.py 

for file in /data/Twitter\ dataset/geoTwitter19*.zip; do
    nohup ./src/map.py --input_path="$file" > "logs/$(basename "$file").log" 2>&1 &
done
