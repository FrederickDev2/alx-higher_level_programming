#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - This function insert number into
 * a sorted singly linked list
 * @head: The pointer to the head node
 * @number: integer to assign to the inserted node
 *
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;
	listint_t *ptr;

	ptr = *head;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		insert->next = ptr;
		*head = insert;
		return (insert);
	}
	
	while (ptr && ptr->next &&  ptr->next->n < number)
		ptr = ptr->next;

	insert->next = ptr->next;
	ptr->next = insert;

return (insert);
}
