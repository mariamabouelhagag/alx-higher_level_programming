#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * instert_node - inserts in ordered list
 * @head: head of list
 * @number: number to put in
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
