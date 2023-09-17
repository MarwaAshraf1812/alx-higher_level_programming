#!/usr/bin/python3
"""
This module contains the base class
"""
import json


class Base:
	"""
	Base of the other shapes
	"""
	__nb_objects = 0
	def __init__(self, id=None):
		if id:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		"""
		Returns JSON string representation
		"""
		if list_dictionaries is None or len(list_dictionaries) == 0:
			return "[]"
		else:
			return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		"""
		Writes to file with JSON string
		"""
		file_name = cls.__name__ + '.json'
		with open(file_name, mode='w', encoding='UTF8') as f:
			if list_objs is None:
				f.write("[]")
			else:
				#to_json_string to convert list_objs to a JSON string. and to_dictionary to format
				list_dictionary = [item.to_dictionary() for item in list_objs]
				json_string = cls.to_json_string(list_dictionary)
				f.write(json_string)

	@staticmethod
	def from_json_string(json_string):
		"""
		Returns JSON strings in list
		"""
		if json_string is None or json_string == []:
			return '[]'
		return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		"""
		Returns an instance with all attrs already set
		"""
		#create object
		dic1 = cls(1,1)
		dic1.update(**dictionary)
		return dic1

	@classmethod
	def load_from_file(cls):
		"""
		Returns a list of instances
		"""
		file_name = cls.__name__ + '.json'
		try:
			with open(file_name, mode='r', encoding='UTF8') as f:
				file_data = f.read()
		except FileNotFoundError:
			return []

		if not file_data:
			return[]
		data = json.loads(file_data)
		return [cls.create(**line) for line in data]
