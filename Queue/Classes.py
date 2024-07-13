
class Queue:
    class Element:
        def __init__(self, data: any) -> None:
            self.data = data
            self.__next = None

        def set_next(self, next_element: object) -> None:
            if isinstance(next_element, Queue.Element) == False: return

            self.__next = next_element 

        def get_next(self) -> object:
            return self.__next
    
    class Iterator:
        def __init__(self, first_element: object) -> object:
            self.__counter = 0
            self.__current_element = first_element

        def __next__(self) -> any:
            if self.__current_element == None: raise(StopIteration)

            data = self.__current_element.data
            self.__current_element = self.__current_element.get_next()

            return data

    def __init__(self) -> object:
        self.__len = 0
        self.__first = None
        self.__last = None

    def len(self) -> int:
        return self.__len

    def enqueue(self, data: any) -> None:
        if self.__len == 0: 
            self.__first = Queue.Element(data)
            self.__last = self.__first
        else:
            self.__last.set_next(Queue.Element(data))
            self.__last = self.__last.get_next()

        self.__len += 1

    def dequeue(self) -> any:
        if self.__len == 0: return None

        poped_element = self.__first

        if self.__len == 1:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.get_next()

        self.__len -= 1

        return poped_element.data

    def peek(self) -> any:
        return self.__first.data

    def extend(self, iterable: any) -> None:
        for item in iterable:
            self.enqueue(item)

    def contain(self, item: any) -> bool:
        current_element = self.__first
        
        while current_element != None:
            if self.__itemMatching(item, current_element.data) == True: return True

            current_element = current_element.get_next()

        return False

    def count(self, item: any) -> int:
        current_element = self.__first
        count = 0

        while current_element != None:
            if self.__itemMatching(item, current_element.data) == True: count += 1

            current_element = current_element.get_next()

        return count

    def remove(self, item: any) -> bool:
        current_element = self.__first

        if self.__itemMatching(item, current_element.data) == True: 
            self.__first = self.__first.get_next()

            if self.__len == 1:
                self.__last = self.__first

            self.__len -= 1
            return True

        while current_element.get_next() != None:
            if self.__itemMatching(item, current_element.get_next().data) == True: 
                current_element.set_next(current_element.get_next().get_next())

                if current_element.get_next() == None: self.__last = current_element

                self.__len -= 1
                return True
            
            current_element = current_element.get_next()

        return False

    def clear(self) -> None:
        while self.dequeue() != None:
            pass

    def __str__(self) -> str:
        current_element = self.__first
        string_form = ""

        while current_element != None:
            string_form += str(current_element.data) + " "
            current_element = current_element.get_next()

        return string_form

    def __iter__(self) -> Iterator:
            return self.Iterator(self.__first)

    def __itemMatching(self, item1: any, item2: any) -> bool:
            if hasattr(item1, '__iter__') == hasattr(item2, '__iter__') == True:
                if len(item1) != len (item2): return False

                iterator1, iterator2 = iter(item1), iter(item2)

                while True:
                    try:
                        if next(iterator1) != next(iterator2): return False
                    except StopIteration:
                        return True
            else:
                if item1 == item2: return True
                return False

