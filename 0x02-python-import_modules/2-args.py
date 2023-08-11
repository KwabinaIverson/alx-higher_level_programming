#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	arg_len = len(argv)
	if arg_len > 1:
		print("{} arguments:".format(arg_len))
		for arg in range(1, arg_len):
			print("{}: {}".format(arg, argv[arg]))
	else:
		print("0 arguments.")
