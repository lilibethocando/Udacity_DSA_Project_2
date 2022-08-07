import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):  # data is the data to be stored in the block
        self.timestamp = self.get_utc_time()  # timestamp is the time when the block is created
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)  # hash is the hash of the data
        self.next = None  # next is the next block in the chain

    def get_utc_time(self):  # get_utc_time is a function to get the current time in UTC
        format = '%H:%M %d/%m/%Y'
        return datetime.utcnow().strftime(format)

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        hash_str = hash_str.encode('utf-8')  # hash_str is the data to be hashed
        sha.update(hash_str)  # sha is the hash of the data
        return sha.hexdigest()

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if data == "":
            return

        if self.head is None:
            self.head = Block(data, 0)

        else:
            current = self.head
            while current.next:
                current = current.next
            previous_hash = current.hash
            current.next = Block(data, previous_hash)

    def print_list(self):
        current = self.head
        while current:
            print("Data:", current.data)
            print("Timestamp in UTC:", current.timestamp)
            print("Hash:", current.hash)
            print("Previous Hash:", current.previous_hash)
            current = current.next


llist = LinkedList()
llist.append("First Block")  # First Block is added to the linked list
llist.append("Second Block")  # Second Block is added to the linked list
llist.append("Third Block")  # Third Block is added to the linked list
llist.print_list()

llist.append("") # Adding empty string, it just returns
llist.print_list()

llist.append("Fourth Block") # Fourth Block is added to the linked list
llist.print_list()

