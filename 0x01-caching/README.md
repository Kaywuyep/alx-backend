## 0x01-CACHING

In computing, cache replacement policies (also known as cache replacement algorithms or cache algorithms) are optimizing instructions or algorithms which a computer program or hardware-maintained structure can utilize to manage a cache of information. Caching improves performance by keeping recent or often-used data items in memory locations which are faster, or computationally cheaper to access, than normal memory stores. When the cache is full, the algorithm must choose which items to discard to make room for new data.

1. FIFO -  First in first out (FIFO)
With this algorithm, the cache behaves like a FIFO queue; it evicts blocks in the order in which they were added, regardless of how often or how many times they were accessed before

2. LIFO - Last in first out (LIFO) or First in last out (FILO)
The cache behaves like a stack, and unlike a FIFO queue. The cache evicts the block added most recently first, regardless of how often or how many times it was accessed before.

3. LRU - Discards least recently used items first. This algorithm requires keeping track of what was used and when, which is cumbersome. It requires "age bits" for cache lines, and tracks the least recently used cache line based on them. When a cache line is used, the age of the other cache lines changes. LRU is a family of caching Ujjwal, which includes 2Q by Theodore Johnson and Dennis Shasha[7] and LRU/K by Pat O'Neil, Betty O'Neil and Gerhard Weikum.

4. MRU - Unlike LRU, MRU discards the most-recently-used items first. At the 11th VLDB conference, Chou and DeWitt said: "When a file is being repeatedly scanned in a [looping sequential] reference pattern, MRU is the best replacement algorithm."[10] Researchers presenting at the 22nd VLDB conference noted that for random access patterns and repeated scans over large datasets (also known as cyclic access patterns), MRU cache algorithms have more hits than LRU due to their tendency to retain older data

5. LFU - Least frequently used (LFU)
Further information: Least frequently used
The LFU algorithm counts how often an item is needed; those used less often are discarded first. This is similar to LRU, except that how many times a block was accessed is stored instead of how recently. While running an access sequence, the block which was used the fewest times will be removed from the cache

### TASKS

0. Basic dictionary
mandatory
Create a class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None

1. FIFO caching
mandatory
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

2. LIFO Caching
mandatory
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

3. LRU Caching
mandatory
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.

4. MRU Caching
mandatory
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
