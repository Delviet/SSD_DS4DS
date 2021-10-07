from computations import *
import rpyc
rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True
import argparse

class ProcessingService(rpyc.Service):
    
    def on_connect(self, conn):
        pass
    
    def on_disconnect(self, conn):
        pass
    
    def exposed_set_operation(self, name):
        if name == 'DotProduct':
            self.op = DotProduct
        elif name == 'Addition':
            self.op = Addition
        elif name == 'ReLu':
            self.op = ReLu
        elif name == 'SoftMax':
            self.op = SoftMax
    
    def exposed_process(self, data, weight = 10):
        dp = self.op(weight)
        new_array = dp.operate(data)
        print(new_array)
        return new_array

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    parser = argparse.ArgumentParser(description='Port parser')
    parser.add_argument('--port', type=int, default = 18861, 
                        help='server port', required = False)
    args = parser.parse_args()
    t = ThreadedServer(ProcessingService, port=args.port)
    t.start()