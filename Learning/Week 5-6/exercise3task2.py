class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.tail is None:
            print("Linked list is empty")
            return
        itr = self.tail
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                if node.next is None:
                    self.tail = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                else:
                    self.tail = itr
                break
            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if data_after == itr.data:
                node = Node(data_to_insert, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                if node.next is None:
                    self.tail = node
                break
            itr = itr.next
        else:
            print(f"Value {data_after} not found in list")

    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if data == self.head.data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                else:
                    self.tail = itr
                return
            itr = itr.next
        print(f"Value: {data} not found in list")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_forward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.remove_by_value("figs")
    ll.print_forward()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_forward()