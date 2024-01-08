#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: a Pyobject list
*/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *my_list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", my_list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
