#include "lists.h"

/**
* insert_dnodeint_at_index - Inserts a new node at a given position
* @h: A pointer to a pointer to the head of the list.
* @idx: The index at which the new node should be added (starting at 0).
* @n: The integer value to be stored in the new node.
*
* Return: The address of the new node, or NULL if it failed.
*/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
dlistint_t *new_node, *temp = *h;
unsigned int count = 0;
if (idx == 0)
return (add_dnodein(h, n));
while (temp != NULL && count < idx - 1)
{
temp = temp->next;
count++;
}
if (temp == NULL || count < idx - 1)
return (NULL);
new_node = malloc(sizeof(dlistint_t));
if (new_node == NULL)
return (NULL);
new_node->n = n;
new_node->prev = temp;
new_node->next = temp->next;
if (temp->next != NULL)
temp->next->prev = new_node;
temp->next = new_node;
return (new_node);
}
