class EventHub:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        """
        Add an observer.
        """
        self.__observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove an observer .
        """
        try:
            if observer in self._observers:
                self._observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self, msg):
        """
        Notify all observers.
        """
        for observer in self.__observers:
            observer(msg)
