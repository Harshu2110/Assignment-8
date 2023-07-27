#!/usr/bin/env python
# coding: utf-8

# In[14]:



get_ipython().system('pip install pyinputplus')


# In[ ]:


get_ipython().set_next_input('1. Is the Python Standard Library included with PyInputPlus');get_ipython().run_line_magic('pinfo', 'PyInputPlus')


# In[ ]:


Ans: Pyinputplus is a separate third-party library that needs to be installed separately. It is not a part of the Python Standard Library. 


# In[ ]:


get_ipython().set_next_input('2.Why is PyInputPlus commonly imported with import pyinputplus as pypi');get_ipython().run_line_magic('pinfo', 'pypi')


# In[ ]:


Ans:  PyInputPlus is commonly imported using a shorter alias for convenience, pyinputplus is imported as pyip.


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()?


# In[ ]:


Ans: inputInt() : Accepts an integer value, and returns int value
inputFloat() : Accepts integer/floating point value and returns float value


# In[ ]:


4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?


# In[ ]:


Ans: To ensure that the user enters a whole number between 0 and 99 using PyInputPlus, we can use the inputInt() function along with the min and max parameters


# In[1]:


import pyinputplus as pyip

num = pyip.inputInt(prompt='Enter a whole number between 0 and 99: ', min=0, max=99)

print(f"You entered: {num}")


# In[ ]:


get_ipython().set_next_input('5. What is transferred to the keyword arguments allowRegexes and blockRegexes');get_ipython().run_line_magic('pinfo', 'blockRegexes')


# In[ ]:


Ans: In PyInputPlus, the keyword arguments allowRegexes and blockRegexes are used to specify regular expressions that define patterns for allowed and blocked input values, respectively.


# In[ ]:


get_ipython().set_next_input('6. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')


# In[4]:


import pyinputplus as pyip

try:
    user_input = pyip.inputStr(prompt='Enter a string: ', limit=3)
except pyip.RetryLimitException:
    print("Exceeded retry limit. Please provide valid input.")
else:
    print(f"You entered: {user_input}")


# In[ ]:


get_ipython().set_next_input("7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do");get_ipython().run_line_magic('pinfo', 'do')


# In[5]:


import pyinputplus as pyip

user_input = pyip.inputStr(prompt='Enter a string: ', limit=3, default='hello')

print(f"You entered: {user_input}")


# In[ ]:




