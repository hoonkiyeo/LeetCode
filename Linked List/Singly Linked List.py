class Node:
    def __init__(self):
        self.val = val
        self.next = None

    def add(self, node):
        if self.next is None:
            self.next = node
        else:
            n = self.next
            while True:
                if n.next is None:
                    n.next = node
                    break
                else:
                    n = n.next

    def select(self, idx):
        n = self.next
        for _ in range(idx-1):
            n = n.next
        return n.val

    def delete(self, idx):
        n = self.next
        for _ in range(idx-2):
            n = n.next
        t = n.next
        n.next = t.next
        del t

    def insert(self, idx, node):
        n = self.next
        for _ in range(idx-2):
            n = n.next
        t = n.next
        n.next = node
        node.next = t

    def pop(self, idx):
        n = self.next
        for _ in range(idx-2):
            n = n.next
        t = n.next
        n.next = t.next
        return t

    def prt(self):
        n = self.next
        while True:
            if n.next is None:
                print(n.val, end = ' ')
                break
            else:
                print(n.val, end = ' ')
                n = n.next
        print()

