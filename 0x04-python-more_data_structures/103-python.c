#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about the Python lists
 * @p: list object
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int mem, size, i;
	const char *type;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	mem = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem);
	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - prints basic info about the Python byte objects
 * @p: byte object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	unsigned char c, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	for (c = 0; c < size; c++)
	{
		printf("%02hhx", bytes->ob_sval[c]);
		if (c == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
