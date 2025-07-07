class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            # move the accessed node to the front
            node = self.cache[key]
            # remove node from current position in double linked list
            node.prev.next = node.next
            node.next.prev = node.prev
            # move the accessed node (removed) to the front
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
             # remove node from current position in double linked list
            node.prev.next = node.next
            node.next.prev = node.prev
            # move the accessed node (removed) to the front
            node.next = self.head.next
            node.prev = self.head
            # update double link stuff when node in the front
            self.head.next.prev = node
            self.head.next = node
        else:
            # add new node to front
            # if you hit max capacity, use the lease recently used item
            if len(self.cache) == self.capacity:
                # least used is in the back
                lru = self.tail.prev
                lru.prev.next = self.tail
                self.tail.prev = lru.prev
                del self.cache[lru.key]
            # add the new node to the very front and connect everything
            new_node = Node(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)