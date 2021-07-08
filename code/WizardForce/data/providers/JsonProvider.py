import json
from io import StringIO


class JsonProvider:

	@classmethod
	def LoadIntoObject(cls, child, json_fp):
		try:
			with open(f"../WizardForce/resources/data/json/{json_fp}", 'r') as file:
				data = file.read()

			child.__dict__.update(json.loads(data))
		except:
			print("loading the json file was not successful")

	@classmethod
	def SaveIntoFile(cls, obj, json_fp, encoder):
		try:
			with open(f"../WizardForce/resources/data/json/{json_fp}", 'w', encoding='utf-8') as file:
				json_value = json.dumps(obj, cls=encoder)
				file.write(json_value)

		except Exception as ex:
			print("could not save json object")


def set_default(obj):
	if isinstance(obj, set):
		return list(obj)
