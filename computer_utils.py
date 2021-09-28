from abc import ABC, abstractmethod
from multiprocessing import Queue
import numpy as np

class Splitter(ABC):

    def __init__(self):
        self.is_working = False
        
    @abstractmethod
    def split(self, data, queue):
        pass
        
class SimpleSplitter(Splitter):
        
    def __init__(self):
        super().__init__()
        
    def split(self, data, queue):
        self.is_working = True
        samples = data.shape[0]
        for i in range(samples):
            queue.put((i, data[i]))    
        self.is_working = False
        
    def working(self):
        return self.is_working
            
class Merger(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def merge(self, data):
        pass
    
class SimpleMerger(Merger):
    
    def __init__(self):
        super().__init__()
        
    def merge(self, data):
        """
        Receives data dict {idx: value}
        and returns stacks data over 0 axis
        based on the idx order in the dict
        """
        sorted_items = sorted(data.items(), key = lambda x: x[0])
        sorted_vals = [val for (key, val) in sorted_items]
        return np.stack(sorted_vals)
