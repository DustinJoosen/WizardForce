import sqlite3


class SqliteProvider:
	__DB_FP = "../WizardForce/resources/data/WizardForce.db"

	def __init__(self, table_name, output_type):
		#child_properties are all the properties of the class. These need to match the database columns
		self.child_properties = list(vars(self).keys())
		#the type of the child, and the name of the table
		self.output_type = output_type
		self.table_name = table_name

		#to check if the base class was initialized
		self.is_initialized = True

	#returns the item of the table, with Id set to the parameter
	def GetById(self, id):
		if not hasattr(self, 'is_initialized'):
			raise RuntimeError("Base class is not initialized. You can do this by this line:\n"
								"'super().__init__(*table_name*, *child_type*)'")

		item = self.GetByQuery(f"SELECT * FROM {self.table_name} WHERE Id = {id}")
		return item[0]

	#returns all the records of the table
	def GetAll(self):
		if not hasattr(self, 'is_initialized'):
			raise RuntimeError("Base class is not initialized. You can do this by this line:\n"
								"'super().__init__(*table_name*, *child_type*)'")

		return self.GetByQuery(f"SELECT * FROM {self.table_name}")

	#returns the records found by the query, mapped to the output type, in a list
	def GetByQuery(self, query):
		if not hasattr(self, 'is_initialized'):
			raise RuntimeError("Base class is not initialized. You can do this by this line:\n"
								"'super().__init__(*table_name*, *child_type*)'")

		records = self.__RetrieveRecords(query)
		items = []

		for record_idx in range(len(records)):
			items.append(self.output_type())
			for prop_idx in range(len(self.child_properties)):
				setattr(items[record_idx], self.child_properties[prop_idx], records[record_idx][prop_idx])

		return items

	#queries all the records in the database, and returns a list of tuples
	@staticmethod
	def __RetrieveRecords(query):
		with sqlite3.connect(SqliteProvider.__DB_FP) as connection:
			output = []

			cursor = connection.cursor()
			cursor.execute(query)

			records = cursor.fetchall()
			for record in records:
				output.append(record)

		return output

