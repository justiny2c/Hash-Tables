# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# [1.1][[2.2, 2.3]][3.3, 3.4]


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hashed = hash(key)
        return hashed

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.

        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        pair = LinkedPair(key, value)  # new LinkedPair that gets added

        while node is not None and self.storage[index].key is not key:
            # updates node variable to check each pair in the node
            insert = node
            node = insert.next

        # if statement runs outside of while loop
        if node is not None and node.key is key:  # key is the same
            node.value = value  # updates old value with same key
        else:  # else, if key is not found
            # adds "Linked List" to new LinkedPair @ .next
            pair.next = self.storage[index]
            self.storage[index] = pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        next_node = None

        while node is not None and node.key is not key:

            next_node = node
            node = next_node.next

        if node is None:
            print("Error")

        else:
            if next_node is None:
                self.storage[index] = node.next
            else:
                next_node.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next  # factors in collisions, and runs while loop again

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        old_storage = self.storage
        self.capacity *= 2
        # then reassign a new storage with the now new capacity pretty much "restarting" a new array
        self.storage = [None] * self.capacity
        # then we have to make a 'null' node in which to insert into our new storage
        # this is VERY time consuming since it takes the old storage, makes a new one, doubles the capcacity, then REINSERTS the old capacity into the new one making this o(log)n since it's depenendent on the size of the old capacity
        pair = None
        # so we use a forloop to loop through the new capcity
        for i in old_storage:
            # with every node we have a key value pair so we make the pair equal to the old storage key value pair which is an object so
            pair = i
            # while we are inside each node we run another loop in this case a while loop to run until each key and each value is inserted thus making the node or in this case 'pair' no longer 'None'
            while pair is not None:
                # and while it is "is not None" we insert the pair's key and value into the new new storage which is "this.storage" so we use "insert"
                self.insert(pair.key, pair.value)
                # and we continue down the line of key value pairs going back and fourth through the for loop with the whole object then the while loop through the object itself.
                # again this isn't the best option and it is very costly in terms of memory and time so for large scale operation this isn't ideal at ALL
                pair = pair.next


if __name__ == "__main__":
    # ht = HashTable(3)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # ht.remove("line_1")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
