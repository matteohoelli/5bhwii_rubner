class Node:
    # Klasse Node definieren, um ein einzelnes Element in einer einfach verketteten Liste zu speichern.
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # Klasse LinkedList definieren, um die einfach verkettete Liste als Datenstruktur zu implementieren.
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        # Methode "am Ende Hinzufügen" implementieren.
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def length(self):
        # Methode zur Ausgabe der Länge der Datenstruktur implementieren.
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def display(self):
        # Methode zur Ausgabe aller Elemente implementieren.
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values


if __name__ == "__main__":
    linked_list = LinkedList()
    # Exemplarische Befüllung der Liste mit Zufallszahlen.
    import random

    for i in range(10):
        linked_list.append(random.randint(1, 100))
    print("Length:", linked_list.length())
    print("Elements:", linked_list.display())
