# from networkx import current_flow_betweenness_centrality_subset
import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        # Create m crewmates and store them in a max heap based on load
        self.crewmates = heap.Heap(heap.min_load, [crewmate.CrewMate() for _ in range(m)])  # Heap of crewmates
        self.treasures = []  # List to store all treasures
        self.crewmates_list = []  # Active crewmates who are assigned treasures
        self.ans=[]# List to store treasures in the order of completion

    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Get the crewmate with the least load (top of the heap)
        crew_member = self.crewmates.top()
        self.crewmates.extract()
        # print(crew_member)
        
        # If this is the first time the crewmate is getting a treasure, add them to the active list
        if crew_member:   
            if not crew_member.isassigned:
                self.crewmates_list.append(crew_member)  # Add crewmate to active list
                crew_member.isassigned = True  # Mark the crewmate as assigned

            # Assign the treasure to the crewmate
            crew_member.treasures.append(treasure)
            

            # Update the crewmate's load
            if crew_member.load<=treasure.arrival_time:
                crew_member.load=treasure.size+treasure.arrival_time
            else:
                crew_member.load+=treasure.size

            # Reinsert the updated crewmate back into the heap
            self.crewmates.insert(crew_member)

    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        # ans=[]


        
        for i in range(len(self.crewmates_list)):
            current_crew=self.crewmates_list[i]
            # print(len(self.crewmates_list), "hi")
            # print(current_crew)
            # Process each treasure of the crewmate
            for j in range(len(current_crew.treasures)):
                # print(current_crew.treasures[j].id,current_crew.treasures[j].size)  
                
                current_treasure = current_crew.treasures[j] 
                if  current_crew.last_trsr is not None :
                    cur_time = current_crew.last_trsr.arrival_time
                    # print(cur_time)
                    # while cur_time < current_treasure.arrival_time and current_crew.treasure_ass:
                    #     last=current_crew.treasure_ass.top()
                    #     current_crew.treasure_ass.extract()
                    #     time_diff = current_treasure.arrival_time - cur_time 

                        # if time_diff < last.size:
                        #     last.size -= time_diff
                           
                        #     last.priority[0]-=time_diff
                        #     current_crew.treasure_ass.insert(last) 
                        #     cur_time = current_treasure.arrival_time
                        # else :
                        #     current_treasure.completion_time = cur_time + last.size
                        #     cur_time += last.size
                        #     if not last.added:  # Prevent duplicates
                        #         self.ans.append(last)
                        #         last.added = True
               
                # Ensure there are treasures in the heap before processing
                    while cur_time < current_treasure.arrival_time and not current_crew.treasure_ass.is_empty():
                        last = current_crew.treasure_ass.top()
                        current_crew.treasure_ass.extract()
                        
                        if last is not None:  # Ensure last is valid
                            time_diff = current_treasure.arrival_time - cur_time

                            if time_diff < last.size:
                                last.size -= time_diff
                                last.priority[0] -= time_diff
                                current_crew.treasure_ass.insert(last)
                                cur_time = current_treasure.arrival_time
                            else:
                                current_treasure.completion_time = cur_time + last.size
                                cur_time += last.size
                                if not last.added:  # Prevent duplicates
                                    self.ans.append(last)
                                    last.added = True
                    
                    

                cur_time=current_treasure.arrival_time

                # if j == 0:
                #     # For the first treasure
                #     if len(current_crew.treasures) > 1:
                #         time_diff = current_crew.treasures[1].arrival_time - current_treasure.arrival_time

                #         if time_diff < current_treasure.size:
                #             current_treasure.size -= time_diff
                #             current_crew.treasure_ass.insert(current_treasure) # Store it back
                #             print(current_treasure.size,time_diff)
                #         else:
                #             current_treasure.completion_time = current_treasure.arrival_time + current_treasure.size
                #             self.ans.append(current_treasure)
                #             cur_time += current_treasure.size
                #     else:
                #         # Handle the treasure's size and completion time
                #         current_crew.treasure_ass.insert(current_treasure)
                #         current_treasure.completion_time = current_treasure.arrival_time + current_treasure.size
                #         current_crew.last_trsr = current_crew.treasures[j]
                #         current_crew.treasures = None
                #         current_crew.treasures=[]
                #         self.ans.append(current_treasure)



                # else:
                    # For subsequent treasures
                if j < len(current_crew.treasures) - 1:
                    time_diff = current_crew.treasures[j + 1].arrival_time - current_treasure.arrival_time
                    cur_time = current_crew.treasures[j + 1].arrival_time - time_diff
                    current_crew.treasure_ass.insert(current_treasure)

                    while cur_time < current_crew.treasures[j + 1].arrival_time and not current_crew.treasure_ass.is_empty():
                        # Extract the current treasure from the assistant queue
                        next_treasure = current_crew.treasure_ass.top()
                        current_crew.treasure_ass.extract()

                        # Check how much time to process the next treasure
                        if time_diff < next_treasure.size:
                            next_treasure.size -= time_diff
                            next_treasure.priority[0]-=time_diff
                            current_crew.treasure_ass.insert(next_treasure)  # Insert it back if not fully processed
                            cur_time = current_crew.treasures[j + 1].arrival_time  # No more time left
                        else:
                            # Fully process the treasure
                            next_treasure.completion_time = cur_time + next_treasure.size
                            if not next_treasure.added:  # Prevent duplicates
                                self.ans.append(next_treasure)
                                next_treasure.added = True
                            # self.ans.append(next_treasure)
                            time_diff -= next_treasure.size  # Subtract the processed time
                            cur_time += next_treasure.size
                else:
                    current_crew.treasure_ass.insert(current_crew.treasures[j])
                    heapi=current_crew.treasure_ass.copy()
                    cur_time = current_crew.treasures[j].arrival_time
                    while not heapi.is_empty():
                        next_treasure = heapi.top()
                        
                        heapi.extract()
                        next_treasure.completion_time = cur_time + next_treasure.size
                        if not next_treasure.added:  # Prevent duplicates
                            self.ans.append(next_treasure)
                            next_treasure.added = True
                            
                        cur_time += next_treasure.size
                    current_crew.last_trsr = current_crew.treasures[j]
                    current_crew.treasures = None
                    current_crew.treasures=[]




        # Sort the treasures by completion time
        sorted_ans = heap.heapsort(self.ans)
        return sorted_ans
 