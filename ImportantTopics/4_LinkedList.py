class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            return
        
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def insert_after_key(self, key, data):
        new_node = Node(data=data)
        current = self.head
        if current is None:
            print(f'Can\'t find the {key}')
            return
        while current.data != key:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node must be in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        current = self.head
        previous = self.head
        if current is None:
            print(f"List is Empty.")
            return
        while current.data != data:
            previous = current
            current = current.next
        previous.next = current.next
        current = None
    
    def search_node(self, key):
        # current = self.head
        # count = 0
        # if current is None:
        #     print(f"List is Empty.")
        #     return
        # while current.data != key and current.next:
        #     current = current.next
        #     count+=1
        # if current.next is None:
        #     print(f"Key not found.")
        #     return
        # print(f"Found key at position {count}")
        current = self.head
        count=0
        while current:
            if current.data == key:
                print(f'Found key at {count}')
                return
            current = current.next
            count+=1
        print(f'Key not found.')
        return
    
    def length_of_list(self):
        current = self.head
        count=0
        while current:
            count+=1
            current = current.next
        print(f'List size is {count}')
    
    def print_list(self):
        current = self.head
        while current:
            print(f'{current.data} ->', end=' ')
            current = current.next
        print(None)


def main():
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.print_list()
    ll.insert_at_beginning(5)
    ll.print_list()
    ll.insert_at_end(20)
    ll.print_list()
    ll.insert_after_key(10, 15)
    ll.print_list()
    ll.delete_node(15)
    ll.print_list()
    ll.search_node(5)
    ll.search_node(10)
    ll.search_node(20)
    ll.search_node(77)
    ll.print_list()
    ll.length_of_list()


if __name__=='__main__':
    main()



# Output
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics>
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\4_LinkedList
# 10 -> None
# 5 -> 10 -> None
# 5 -> 10 -> 20 -> None
# 5 -> 10 -> 15 -> 20 -> None
# 5 -> 10 -> 20 -> None
# Found key at 0
# Found key at 1
# Found key at 2
# Key not found.
# 5 -> 10 -> 20 -> None
# List size is 3
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics>