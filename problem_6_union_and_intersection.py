class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_set = set()
    union_list = LinkedList()
    if llist_1.head is not None:
        current = llist_1.head
        while current:
            union_set.add(current.value)
            current = current.next
    if llist_2.head is not None:
        current = llist_2.head

        while current:
            union_set.add(current.value)
            current = current.next

    if len(union_set) == 0:
        msg = "Union set is empty!"
        return msg

    for node in sorted(list(union_set)):
        union_list.append(node)
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    llist_1_set = set()
    llist_2_set = set()
    intersection_list = LinkedList()

    if llist_1.head is not None:
        current = llist_1.head
        while current:
            llist_1_set.add(current.value)
            current = current.next

    if llist_2.head is not None:
        current = llist_2.head
        while current:
            llist_2_set.add(current.value)
            current = current.next

    intersection_set = llist_1_set & llist_2_set

    if len(intersection_set) == 0:
        msg = "Intersection set is empty!"
        return msg

    for node in sorted(list(intersection_set)):
        intersection_list.append(node)

    return intersection_list


print("Test case 1")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2)) # Returns: 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 ->
print(intersection(linked_list_1,linked_list_2)) # Returns: 4 -> 6 -> 21 ->

print("Test case 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4)) # Returns: 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 ->
print(intersection(linked_list_3,linked_list_4)) # Returns: Intersection set is empty!

print("Test case 3")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,6,8,9,7,4,51,45]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6)) # Returns: 1 -> 4 -> 6 -> 7 -> 8 -> 9 -> 45 -> 51 ->
print(intersection(linked_list_5, linked_list_6)) # Returns: Intersection set is empty!

print("Test case 4")

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [9,5,3,21,47,52,8,6,1]
element_2 = [22,2,3,11,21,5,8,6,9]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8)) # Returns: 1 -> 2 -> 3 -> 5 -> 6 -> 8 -> 9 -> 11 -> 21 -> 22 -> 47 -> 52 ->
print(intersection(linked_list_7, linked_list_8)) # Returns: 3 -> 5 -> 6 -> 8 -> 9 -> 21 ->


print("Test case 5")

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10)) # Returns: Union set is empty!
print(intersection(linked_list_9, linked_list_10)) # Returns: Intersection set is empty!
