#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	const char *data = PyBytes_AsString(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [Error] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", data);

	printf("  first %zd bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", data[i]);
		if (i + 1 == 10 || i + 1 == size)
			break;
		printf(" ");
	}
	printf("\n");
}
