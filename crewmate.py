'''
    Python file to implement the class CrewMate
'''
import heap
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.load =0   # total remaining size of all assigned treasures
        self.isassigned=False
        self.treasure_ass = heap.Heap(heap.max_priority,[]) #max priority heap
        self.treasures=[]
        self.last_trsr = None
        self.total_com=0
    
    # Add more methods if required
    


    


    