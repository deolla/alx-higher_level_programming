#include <Python.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;
	unsigned char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(bytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = (unsigned char *)PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %ld bytes:", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", string[i]);

	printf("\n");
}

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);

		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyList_Check(item))
		{
			print_python_list(item);
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
		}
		else if (PyUnicode_Check(item))
			printf("str\n");
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
