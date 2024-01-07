#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: reversed list
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head != NULL && (*head)->next != NULL)
	{
		listint_t *walker = *head, *runner = *head;
		listint_t *prev_walker = *head, *second_half;
		int is_palindrome = 1;

		while (runner != NULL && runner->next != NULL)
		{
			runner = runner->next->next;
			prev_walker = walker;
			walker = walker->next;
		}
		if (runner != NULL)
		{
			walker = walker->next;
		}
		second_half = walker;
		prev_walker->next = NULL;
		reverse_list(&second_half);

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
		second_half = reverse_list(&second_half);
		prev_walker->next = second_half;

		return (is_palindrome);
	}
	return (0);
}
