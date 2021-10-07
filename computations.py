from abc import ABC, abstractmethod
import numpy as np

class Operation(ABC):
    
    def __init__(self, weight = None):
        self.weight = weight
        
    @abstractmethod
    def operate(self, data, weight2 = None):
        pass
    
class DotProduct(Operation):
    
    def __init__(self, weight):
        super().__init__(weight)
        
    def operate(self, data, weight2 = None):
        return np.sum(list(data * self.weight))
    
class Addition(Operation):
    
    def __init__(self, weight = None):
        super().__init__(weight)
        
    def operate(self, data, weight2 = None):
        return data + self.weight
    
class ReLu(Operation):
    
    def __init__(self, weight = None):
        super().__init__(weight)
        
    def operate(self, data, weight2 = None):
        return data if data > 0 else 0
    
class SoftMax(Operation):
    
    def __init__(self, weight = None):
        super().__init__(weight)
        
    def operate(self, data, weight2 = None):
        data = np.array(data)
        return np.exp(data)/sum(np.exp(data))
