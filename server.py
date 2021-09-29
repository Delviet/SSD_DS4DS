import rpyc
rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True

class ProcessingService(rpyc.Service):
    
    def on_connect(self, conn):
        pass
    
    def on_disconnect(self, conn):
        pass
    
    def exposed_process(self, data, weight = 10):
        new_array = [i * weight for i in data]
        print(new_array)
        return new_array

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(ProcessingService, port=18861)
    t.start()
