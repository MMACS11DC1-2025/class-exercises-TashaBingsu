file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

print("Dance score \tSong")
for item in drake_data:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])

for j in range(j+1, len(drake_data)):
	if drake_data[j] < smallest:
		smallest = drake_data[j]
		lowest_index = j

drake_data[lowest_index], drake_data[lowest_index] = drake_data[lowest_index],

print(drake_data)
