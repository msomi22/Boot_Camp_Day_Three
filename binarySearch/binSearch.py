"""
 BinarySearch class, that inherits from the list class.
"""
class BinarySearch(list):
    """
    Attributes:
    listlen: The length of the list to be created 
    interval: The firt element and the interval from one element to the next
    *args: special syntax used to pass a non-keyworded, variable-length argument list
    """
    def __init__(self, listlen, interval, *args):
        
        list.__init__(self, *args)
        self.list_length = listlen
        self.step = interval
        end = self.list_length * self.step
        
        for i in range(self.step, end+1, self.step):
            self.append(i)  #  append the elements from  interval to listlen
            
    @property
    def length(self):
        """
        Python has a great concept called property, 
        which makes the life of an object oriented programmer much simpler.
        It can be used as a getter and a setter

        In this case we use it to get the length

        Return the length of the list generated (i.e total number of elements)
        """
        return len(self)

    """
    Attributes:
    toFind: The toFind to search 
    start: Start index 
    end: End index 
    count: The number of times you function iterated to find the index of the number in question

    """    
    def search(self, toFind, start=0, end=None, count=0):
        if not end:
            end = self.length - 1
            
        if toFind == self[start]:
            return {'index': start, 'count': count}
        elif toFind == self[end]:
            return {'index': end, 'count': count}
          
        mid = (start + end) // 2
        if toFind == self[mid]:
            return {'index': mid, 'count': count}
        elif toFind > self[mid]:
            start = mid + 1
        elif toFind < self[mid]:
            end = mid - 1
            
        if start >= end:
            return {'index': -1, 'count': count}
        count += 1  
        return self.search(toFind, start, end, count)
