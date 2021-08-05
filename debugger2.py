import os
import json
import shutil

paragraph_count = 0
total_count = 0
path = "output"
for root, dirs, files in os.walk(path):
	for file in files:
		if file != ".DS_Store" and file.endswith(".json"):
			with open(os.path.join(root, file), "rb") as json_file:
				data = json.load(json_file)
				if data["para_aligned_status"]:
					paragraph_count += 1
				else:
					print(file)
					shutil.copy("output/" + file, "wrong/" + file)
				total_count += 1

print()
print("paragraph aligned count: " + str(paragraph_count))
print("total count: " + str(total_count))