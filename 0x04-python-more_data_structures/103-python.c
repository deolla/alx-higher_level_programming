#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: A pointer to a PyObject that represents a bytes object
 *
 * Return: no return.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, pop;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		pop = 10;
	else
		pop = size + 1;

	printf("  first %ld bytes:", pop);
	for (i = 0; i < pop; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: A pointer to a PyObject that represents a list object
 * 
 * Return: no return.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	long int size, i;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
