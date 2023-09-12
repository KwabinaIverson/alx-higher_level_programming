#!/usr/bin/python3
""" A function that returns true if the object is an instance """

def is_kind_of_class(obj, a_class):
	""" Checks if a class is an instance or inhereted instance of a class

	Args:
		obj (any): The object to check
		a_class (any): The class to match the object type to
	Return:
		If obj is an instance or inhereted instance of a class - True
		Otherwise: False
	"""
	if isinstance(obj, a_class):
		return True
	return False
