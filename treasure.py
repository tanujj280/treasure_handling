'''
    Python file to implement the Treasure class
'''

class Treasure:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''
        
        # DO NOT EDIT THE __init__ method
        self.size=size
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None
        self.crew=None
        self.added=False
        self.priority=[self.size+self.arrival_time,self.id]
    
    # You can add more methods if required