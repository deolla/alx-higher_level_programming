#include <Python.h>
/**
 * print_python_list - prints python list information.
 * @p: List.
 *
 * Return: no return.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *element;
	const char *element_type;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		element_type = element->ob_type->tp_name;
		printf("Element %ld: %s\n", i, element_type);
	}
}

/**
 * print_python_bytes - print python bytes.
 * @p: bytes.
 *
 * Return: no return.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	Py_ssize_t max_display_bytes;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}
	size = PyBytes_Size(p);
	max_display_bytes = (size > 10) ? 10 : size;

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes = %ld\n", size);
	printf("first %ld bytes: ", max_display_bytes);

	for (i = 0; i < max_display_bytes; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < max_display_bytes - 1)
		printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - print python float information.
 * @p: Python Object.
 *
 * Return: no return.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}
	printf("[*] Python float info\n");
	printf("[.] value: %f\n", PyFloat_AsDouble(p));
}
