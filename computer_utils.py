from abc import ABC, abstractmethod
from multiprocessing import Queue
from time import sleep
import numpy as np

class Overseer:
    
    """
    This class uses given connection
    to implement computations with the
    data given in the queue
    """
    
    def __init__(self, connection, op_name):
        self.c = connection
        self.c.root.set_operation(op_name)
    
    def put(self, queue, res_dict, shared_status):
        while True:
            if all(shared_status): # check all tasks completed
                break 
            if queue.empty(): # wait for new tasks
                sleep(0.05)
                continue
            idx, data_frac, weight = queue.get()
            ans = self.c.root.process(data_frac, weight)
            # saving result and changing status
            res_dict[idx] = ans
            shared_status[idx] = 1         

class Splitter(ABC):

    def __init__(self):
        self.is_working = False
        
    @abstractmethod
    def split(self, data, weight, queue, mode):
        pass
        
class SimpleSplitter(Splitter):
        
    def __init__(self):
        super().__init__()
        
    def split(self, data, weight, queue, mode = 'weight'):
        self.is_working = True
        # split across the data, share weight
        if mode == 'data':
            samples = data.shape[0]
            for i in range(samples):
                queue.put((i, data[i], weight))
        # split across the weight, share data
        elif mode == 'weight':
            samples = weight.shape[0]
            for i in range(samples):
                queue.put((i, data, weight[i]))
        # split across both the weight and data 
        # (separate parameter for each data unit)
        elif mode == 'both':
            samples = weight.shape[0]
            for i in range(samples):
                queue.put((i, data[i], weight[i]))
        self.is_working = False 
        return samples
            
class Merger(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def merge(self, data, axis):
        pass
    
class SimpleMerger(Merger):
    
    def __init__(self):
        super().__init__()
        
    def merge(self, data, axis = 0):
        """
        Receives data dict {idx: value} and axis idx, 
        returns stacks data over specified axis
        based on the idx order in the dict
        """
        # recovering correct data order
        sorted_items = sorted(data.items(), key = lambda x: x[0])
        sorted_vals = [val for (key, val) in sorted_items]
        if not axis is None:
            return np.stack(sorted_vals, axis = axis)
        else:
            return np.array(sorted_vals)
