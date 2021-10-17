import random


class Agent:
    def __init__(self,i,environment,agents,neighbourhood,rows,cols,y,x):
        self.i = i
        self.x = x
        self.y = y
        #self.x = random.randint(0,99)
        #self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.rows = rows 
        self.cols = cols
        self.store = 0 
        
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store)+ ", environment value="+str(self.environment[self.y][self.x])
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows
        else:
            self.y = (self.y - 1) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols
            
    def eat(self):
        if self.environment[self.y][self.x] >10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
               total = self.store + agent.store
               ave = total / 2
               self.store = ave
               agent.store = ave
               print("sharing" +" "+ str(dist) +" "+ str(ave))
               
    def distance_between(self, agent):
       return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
       
        
        
       
        