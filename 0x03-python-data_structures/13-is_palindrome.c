#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *runner = *head;
	listint_t *walker = NULL, *prev_walker = NULL;

	if (*head == NULL || runner->next == NULL)
		return (1);
	while (runner != NULL)
	{
		add_nodeint(&walker, runner->n);
		runner = runner->next;
	}
	prev_walker = walker;
	while (*head != NULL)
	{
		if ((*head)->n != prev_walker->n)
		{
			free_listint(walker);
			return (0);
		}
		*head = (*head)->next;
		prev_walker = prev_walker->next;
	}
	free_listint(walker);
	return (1);
}
