import rpyc

class ComputingService(rpyc.Service):
    
    def on_connect(self, conn):
        pass
    
    def on_disconnect(self, conn):
        pass
    
    def exposed_perform_multiplication(self, array, weight = 10):
        new_array = [i * weight for i in array]
        print(new_array)
        return new_array

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(ComputingService, port=18861)
    t.start()
