class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def resize(self):
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity
        print(f"Resized to {self.capacity}")

    def pop(self):
        if self.size == 0:
            return "Underflow"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print([self.arr[i] for i in range(self.size)])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_at_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete_by_value(self, x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp
                if temp.next:
                    temp.next.prev = new
                temp.next = new
                return
            temp = temp.next

    def delete_at_position(self, pos):
        if not self.head:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        for _ in range(pos):
            if not temp:
                return
            temp = temp.next
        if temp:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None


# MAIN TESTING
if __name__ == "__main__":
    print("Dynamic Array Test")
    da = DynamicArray(2)
    for i in range(10):
        da.append(i)
    da.display()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.display()

    print("\nSingly Linked List Test")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    sll.traverse()

    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.traverse()

    sll.delete_by_value(3)
    sll.traverse()

    print("\nDoubly Linked List Test")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.traverse()

    dll.insert_after(2, 5)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    print("\nStack Test")
    st = Stack()
    st.push(10)
    st.push(20)
    print(st.pop())
    print(st.peek())

    print("\nQueue Test")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.front())

    print("\nParentheses Checker")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")