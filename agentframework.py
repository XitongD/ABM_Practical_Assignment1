import random

#define the Agent class
# X and y was initialised in order to scrape data from a web page
class Agent:
    def __init__(self,i,environment,agents,neighbourhood,rows,cols,y,x): # using __init__ to initialise the model
        self.i = i
        self.x = x
        self.y = y
        #self.x = random.randint(0,99)
        #self.y = random.randint(0,99)
        self.environment = environment # environment variable
        self.agents = agents # agents list
        self.neighbourhood = neighbourhood # neighbourhood variable
        self.rows = rows # the rows of the environment
        self.cols = cols # the cols of the environment
        self.store = 0 
# Returns the x, y coordinates, stores and corresponding environment values   
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store)+ ", environment value="+str(self.environment[self.y][self.x])
      
# Creating the move function. Agents move according to a random number
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows # Preventing the agent from crossing the border
        else:
            self.y = (self.y - 1) % self.rows # Preventing the agent from crossing the border

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols # Preventing the agent from crossing the border
        else:
            self.x = (self.x - 1) % self.cols # Preventing the agent from crossing the border
            
 # Creating eat function  
 # Agents eat the grass(environment) if the  environment value is over 10 (taking 10 from the environment and adding 10 to the store)
 # If the environment value is less than 10, they add the remaining to their store and set the environment value to zero   
    def eat(self):
        if self.environment[self.y][self.x] >10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

# Creating share function
# Exchanging information with neighbouring agents
#For each agent, the distance is calculated and if the distance is less than the neighbour value(20), their store is set to the average of the two
# After each share there will be a printed statement of the distance between them to check if it is less than 20 and the average that the store is set to
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            if agent != self: # This does not happen with agents that have their own
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                   total = self.store + agent.store
                   ave = total / 2
                   self.store = ave
                   agent.store = ave
                   print("sharing" +" "+ str(dist) +" "+ str(ave))
                   
# Calculate the distance between the current agent and the neighbouring agent                
    def distance_between(self, agent):
       return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
       
        
        
       
        