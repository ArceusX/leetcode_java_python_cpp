# Relevant to webpage servicing and CPU resource management 

# Requires 2 data structures: map + double-linked list
# Use map to track which keys/items are in cache of given capacity
# Use DLL to track order of recent use of keys

# In DLL, most-recently-used (MRU) key as tail, LRU as head
# For key in cache, if [get|put](key), moveToTail(key)/set it as MRU
# (ie key represents webpage and webpage was fetched or edited) 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # const
        self.LLHead   = None
        self.LLTail   = None

        # len(self.mrcMap) gives cache used
        self.mrcMap   = dict()
        
    def get(self, key: int) -> int:
        if key in self.mrcMap: # Set fetched key as MRU 
            node = self.mrcMap[key]
            self.moveToTail(node)
            
            return node.value
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        # if capacity < 1 : return
        if key in self.mrcMap: # Key is modified, set as MRU
            node = self.mrcMap[key]
            node.value = value
            self.moveToTail(node)

        else:
            # Cache may be empty and MRU not exist (ie tail is None) 
            node = Node(key, value, self.LLTail)
            if self.LLTail: self.LLTail.front = node
            self.LLTail = node
                
            # If cache is full, purge LRU. Set new LRU 
            if  len(self.mrcMap) == self.capacity:
                del self.mrcMap[self.LLHead.key]
                self.LLHead = self.LLHead.front

        self.mrcMap[key] = self.LLTail
        if len(self.mrcMap) == 1: self.LLHead = self.LLTail
       
    # To move node to tail spot, only if cache has < 2 keys
    def moveToTail(self, node) -> None:
        if len(self.mrcMap) > 1 and node is not self.LLTail:
            
            # LRU just became MRU. Set 2nd LRU as new LRU
            if node is self.LLHead:
                self.LLHead      = self.LLHead.front
                self.LLHead.back = None
                
            else:
                if node.back:
                    node.back.front = node.front
                    
                if node.front:
                    node.front.back = node.back
                
            self.setTail(node)
        
    # Call only thru moveToTail that checked node is not tail
    def setTail(self, node) -> None:
        # Set node as new tail, with its back being previous tail
        # ie New MRU's less recent neighbor is previous MRU
        self.LLTail.front = node
        node.back   = self.LLTail
        node.front  = None
        self.LLTail = node
            
# back is less recent item, front is more recent item
class Node:
    def __init__(self, key, value, back):
        self.key   = key
        self.value = value
        self.back  = back
        self.front = None
    