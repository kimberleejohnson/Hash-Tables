# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable: 
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    #Googled djb2 hashing, goodmath.org pointed me here 
    def _hash(self, key):
        # Setting the hash as a prime 
        #hash = 5381
        # Iterating arithmetic based on string values 
        ## ord gets an integer representing Unicode point 
        #for c in key: 
            #hash = (hash *33) + ord(c)
        # Return integer
        return hash(key)


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
        # Establishing an index 
        index = self._hash_mod(key) 

        # Displays a warning if there is a value that will be overwritten 
        if self.storage[index] is not None: 
            print("Heads up! You're about to overwrite an existing value.")

        # Create a new key/value pair 
        self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash(key)

        # If there is actually no value there, print a warning 
        if self.storage[index].value == None or self.storage[index].key != key: 
            print("Warning! That key does not exist.")
        # Otherwise, remove the key/value pair by setting LinkedPair values to None
        else: 
            self.storage[index] = LinkedPair(None, None)


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash(key)

        if self.storage[index] is not None and self.storage[index].key == key: 
            return self.storage[index].value
        else: 
            return None 

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        # Create new table self.capacity * 2 
        # Take values out of old, put in new 
        #Hash values are now different, because _hash_mod depends 



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
