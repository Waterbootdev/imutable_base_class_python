class DefaultUnlockedContext:
    def __init__(self, instance):
        self.instance = instance

    def __enter__(self):
        self.instance.unlock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.instance.lock()
    
    #def __exit__(self, exc_type, exc_val, exc_tb):
        # Immer wieder sperren, auch wenn eine Ausnahme im Block auftritt
        #self.instance.lock()
        # Wenn eine Ausnahme auftritt, wird sie hier weitergegeben
        #if exc_type is not None:
            #print(f"Exception occurred: {exc_val}")
            # Falls du eine andere Logik hinzufügen möchtest:
            # return False, um die Ausnahme zu durchreichen, oder
            # True, um sie zu unterdrücken
            # Hier wird sie durchgereicht:
            #return False