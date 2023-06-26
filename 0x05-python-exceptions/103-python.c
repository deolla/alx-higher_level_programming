#include <stdio.h>
#include <Python.h>

/**
 * print_python_float - Prints python float information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
	double pop;
	char *lol;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	pop = ((PyFloatObject *)(p))->ob_fval;
	lol = PyOS_double_to_string(pop, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", lol);
	setbuf(stdout, NULL);
}

/**
 * print_python_bytes - Prints python bytes information
 *
 * @p: bytes
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *s;
	long int lenght, i, m;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	lenght = ((PyVarObject *)(p))->ob_size;
	s = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", lenght);
	printf("  trying string: %s\n", s);

	if (lenght >= 10)
		m = 10;
	else
		m = lenght + 1;

	printf("  first %ld bytes:", m);

	for (i = 0; i < m; i++)
		if (s[i] >= 0)
			printf(" %02x", s[i]);
		else
			printf(" %02x", 256 + s[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints python list information
 *
 * @p: List
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, m;
	PyListObject *list;
	PyObject *obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (m = 0; m < size; m++)
	{
		obj = list->ob_item[m];
		printf("Element %ld: %s\n", m, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	setbuf(stdout, NULL);
}
