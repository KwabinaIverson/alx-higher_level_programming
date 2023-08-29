#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - prints python list
 * @p: Address to the Python object
 */
void print_python_list(PyObject *p)
{
  	/* Check if p is a valid PyListObject */
	if (!PyList_Check(p))
	{
		 printf("[ERROR] Invalid List Object\n");
		return;
	}

	/* Get the size and allocated size of the list */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = PyList_GetAllocSize(p);

	/* Print the size and allocated size of the list */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	/* Iterate over the list and print each element */
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		print_python_object(item);
	}
}

/**
 * print_python_bytes - prints python objects
 * @p: Address to Python object
 */
void print_python_bytes(PyObject *p)
{
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	str = PyBytes_AsString(p);
	if (str == NULL)
	{
		printf("  [ERROR] Failed to convert bytes object to string\n");
		return;
	}

	printf("  trying string: %s\n", str);
	printf("  first %d bytes: %.*s\n", 10, 10, str);
}

/**
 * print_python_float - prints python float
 * @p: Address to the pyhton object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
