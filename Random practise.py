#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[6]:


get_ipython().run_cell_magic('time', '', "for i in range(40):\n    print('im timing output {}'.format(i))")


# ## if else statemets

# In[16]:


beers=['large','bud','carona','jonny','brew','stout']
for Beer in beers:
    if Beer=='bmw':
        print(Beer.upper())
    else:
        print(Beer.title())


# In[ ]:




