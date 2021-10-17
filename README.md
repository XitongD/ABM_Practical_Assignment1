# ABM_Practical_Assignment1
This repository contains three files to run an agent-based model of sheep eating grass.  
  
* [Environment]()  
Initial environment file.Representing grass in the environment  

* [Model-GUI.py](https://github.com/XitongD/ABM_Practical_Assignment1/blob/main/Model-GUI.py)  
Sets up and runs the model:  
1.Pulls in the environment file.  
2.Models the agents interacting with each other.  
3.Scrapes the agent coordinates from a website.  
4.Builds a GUI for the model.  
5.Saves the agents to a file as text.  

* [Agentframework.py]()  
Defines the Agent class used in the model.

##  How to run the model
Before running the model, first adjust the graphics backend to tkinter. When you run the model, first the x and y values will be printed, along with the "stores" and corresponding environment values, and you will see a GUI window pop up, click on the drop down menu "Model" and then "Run Model " to allow you to run the model, at which point you should see 10 agents drawn in the 300x300 "environment". These agents will move randomly and as they cross the border they will appear from the other side. You will see changes in the environment around the agents' paths as they graze (the environment) after each move. At the end of the run (which will stop based on a random number) a file will be written, called "output", which contains the x, y coordinates of all the agents and "stores" and the corresponding environment values.

