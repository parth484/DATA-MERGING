import csv
df = []

with open("bright_stars.csv","r",encoding = 'utf8') as f:
    csvReader = csv.reader(f)
    for row in csvReader:

        df.append(row)
star_data = df[1:]

headers = df[0]

for datapoint in star_data:
    datapoint[2] = datapoint[2].lower()
    
star_data.sort(key = lambda star_data: star_data[2])
    
with open("bright_stars_sorted.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

df.dropna()