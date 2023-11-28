#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if (temp == NULL || temp->n >= number)
	{
		newnode->next = temp;
		*head = newnode;
		return (newnode);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	newnode->next = temp->next;
	newnode->next = newnode;

	return (newnode);
}
