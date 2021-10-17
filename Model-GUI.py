import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import requests
import bs4



# Read in the in.txt file into a list of lists called environment 
environment = [] #Set empty list to write environment data
f = open('in.txt', newline='')
dataset =csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    rowlist = [] #Set new row
    for values in row:
        rowlist.append(values)
    environment.append(rowlist) #Add rowlist to environment
f.close()

#check environment 
rows = len(environment)
cols = len(environment[0])
#print("rows",rows)
#print("cols",cols)
#check the number of rows in the data have the same number of columns
for row in range(rows):
    if(len(environment[row])!= cols):
        print("unhappy")
        
        
#Variable initialisation
num_of_agents = 10 # set the number of agents
num_of_iterations = 300 #Number of initialization iterations
neighbourhood = 20 #Number of initialization neighbourhood
agents = [] #Create an empty list
   
# scraping data from the html
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#Print out the x and y values to see if the data was obtained successfully
#print(td_ys)
#print(td_xs)
 
#Make the agents from web data.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i,environment,agents,neighbourhood,rows,cols,y,x))
#print the agents to check the x,y value
for i in range(num_of_agents):
    print(agents[i])
    
#for i in range(num_of_agents): #Iterate through all agents
    #agents.append(agentframework.Agent(i,environment,agents,neighbourhood,rows,cols))

def run():   # Define the function that run the model  
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#Create fig and ax variables to animate the display
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create the simple GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#Create the dropdown menu
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


carry_on = True	

# Define update function for visualisation
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, cols)
    matplotlib.pyplot.ylim(0, rows)

# Move the agents.
 #for j in range(num_of_iterations):
    #random.shuffle(agents) # randomize the order of agents
    for i in range(num_of_agents):
      #print("before move",agents[i])
      agents[i].move()
      #print("after move",agents[i])# test if this move class works
      agents[i].eat()
      #print("after eat",agents[i]) # test if this eat class works
      agents[i].share_with_neighbours(neighbourhood)# calculate the distance between agents
      
    # set a stop condition    
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")
    # Plotting scatter plots
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        

# Defining the stop of the model
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1



matplotlib.pyplot.show()


# write out the agents to a file
with open("output.txt", "w") as f:
    for i in range(num_of_agents):
        f.write(str(agents[i]) + " ")
        f.write("\n")

tkinter.mainloop()

