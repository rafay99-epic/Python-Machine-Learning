#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Dog:
    
    counter = 0 # class vairiables
    
    def __init__(self, name, age): # this is an constructor
        self.name= name  # data Members
        self.age= age      # data Members
        print("A Dog object is created: ")
        Dog.counter += 1 # increasing the value in the counter
    
    def __del__(self):
        print("Object is Deleted")
        Dog.counter -= 1
    
    def add(self,a,b):
        self.a=rafay
        self.b=moeez
        print(rafay+moeez)
   

