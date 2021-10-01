#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Pet1:
    def __init__(self,age): # this is an constructor
        self.age= age
        print("A Dog object is created: ")

class Pet:
    def __init__(self, name): # this is an constructor
        self.name= name
        print("A Dog object is created: ")

class cat(Pet,Pet1):
    def __init__(self, name, age):
              self.name= name
              self.age= age
              
    


# In[ ]:


# class in once file
class pet:
    def __init__(self, name, age): # this is an constructor
        self.name= name
        self.age= age
        print("A Dog object is created: ")
class Dog(pet):
    def __init__(self, name, age):
              self.name= name
              self.age= age

