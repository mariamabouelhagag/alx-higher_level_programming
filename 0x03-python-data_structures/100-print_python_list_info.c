#include <Python.h>

/**
 * print_python_list_info - display basic informations about Python lists.
 * @p: A PyObject list of python.
 */
void print_python_list_info(PyObject *p)
{
	int size, cord, j;
	PyObject *obj;

	size = Py_SIZE(p);
	cord = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", cord);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
