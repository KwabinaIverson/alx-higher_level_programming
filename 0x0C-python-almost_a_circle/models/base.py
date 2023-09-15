#!/usr/bin/python3
""" Creation of a Base class """

class Base:
	"""Defination the Base class"""

	__nb_objects = 0

	"""
	Initialization of the Base class

	Arg:
		id (int): An id for the Base class
	"""
	def __init__(self, id=None):
		if id != None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
