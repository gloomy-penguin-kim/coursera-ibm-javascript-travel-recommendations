
import json
from decimal import Decimal

#Does quasi the same things as json.loads from here: https://pypi.org/project/dynamodb-json/
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


import wikipedia
#print(wikipedia.summary("Albert Einstein", sentences=2))

import json
# Opening JSON file 
f = open('list.json') 
 

# returns JSON object as a list 
data = json.load(f) 
 
with open('outfile.json', 'w', encoding='utf-8') as outfile:
	#outfile.write('[')
	for row in data:
		strr = row['Name'] + ' ' + row["Location"]
		strr = strr.lower()

		if "wikipedia" not in row['Image']:
			try: 

				page = wikipedia.page(row['Name']) 
				image = page.images[0]
				print(page.original_title)
				print(image) 
			except wikipedia.exceptions.WikipediaException as e:

					page = wikipedia.page(row['Name'] + ", " + row["Location"]) 
					image = page.images[0]
					print(image) 

		# except wikipedia.exceptions.WikipediaException as e:
		# 	try:
		# 		page = wikipedia.page(row["Name"]) 
		# 		row['Name'] = page.original_title 
		# 		page = wikipedia.page(row["Name"]) 
		# 		row['wikipedia'] = page.url
		# 		try: 
		# 			row['coordinates'] = page.coordinates
		# 		except:
		# 			row['coordinates'] = [] 

		# 		print(row['Name'])
		# 		print(row['wikipedia'])
		# 		print(row['coordinates'])
		# 	except wikipedia.exceptions.WikipediaException as ee:
		# 		print(row['wikipedia'])
		# 		print(f"Error: {ee}")
		# 		print("\n\n")
				#with open('outfile.json', 'w', encoding='utf-8') as f
		#json.dump(row, outfile, ensure_ascii=False, indent=4, cls=JSONEncoder)
		#outfile.write(',\n') 

	#outfile.write(']')
