### 
import csv 
import json
import pandas as pd


input_file  = "predicted_results.csv"
# json_predicted  = 

csvfile = open(input_file, 'r')

jsonfile = open('test_predictions.json', 'w')

# fieldnames = ("Id","Predicted")
# reader = csv.DictReader(csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     # jsonfile.write('\n')



df = pd.read_csv(input_file)
dictionary = {}
with jsonfile as f:
	for i in range(len(df)):
		# print (df.ix[i,1])
		# print(type(df.ix[i,1]))
		if df.ix[i,1] != 1.0:
			dictionary[df.ix[i,0]] = ""
		else: 
			dictionary[df.ix[i,0]] = df.ix[i,1]
	json.dump(dictionary,f,sort_keys=True, indent=4)

# df.to_json('pandadata.json')


# ### comparevalues
# jsonfile_org = 'predictions.json'
# jsonfile_new = 'test_predictions.json'
# jsonfile_com = open('combined_predictions.json', 'w')

# with open(jsonfile_org) as handle:
#     dictorg = json.loads(handle.read())

# with open(jsonfile_new) as handle:
#     dictnew = json.loads(handle.read())

# # print(dictdump)
# # json_org = json.loads(jsonfile_org)
# # json_new = json.loads(jsonfile_new)
# # json_new = json.parse(json_new.replace(/\bNaN\b/g, "null"))

# dictionary = {}
# with jsonfile_com as f:
# 	for key in dictorg:
# 		if dictnew[key] == "":
# 			dictionary[key] = ""
# 		else: 
# 			dictionary[key] = dictorg[key]
# 	json.dump(dictionary,f,sort_keys=True, indent=4)






