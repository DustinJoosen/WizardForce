import json


class JsonProvider:

	@classmethod
	def LoadIntoObject(cls, child, json_fp):
		try:
			with open(json_fp, 'r') as file:
				data = file.read()

			child.__dict__.update(json.loads(data))
		except:
			print("loading the json file was not successful")
