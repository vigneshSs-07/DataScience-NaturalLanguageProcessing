#!/usr/bin/env python
# coding: utf-8

# ### Remove domain name

# In[5]:


def remove_domain(txt):
    mail = txt.split('@')[0]    
    return mail


# In[6]:


mail = "neethu@gmail.com"


# In[7]:


remove_domain(mail)


# ### Extract domain name from Email address

# In[14]:


def remove_domain(txt):
    mail = txt.split('@')[-1]    
    return mail


# In[15]:


mail = "neethu@gmail.com"


# In[16]:


remove_domain(mail)


# ### (or)

# In[17]:


import re
s = 'My name is Conrad, and blahblah@gmail.com is my email.'
domain = re.search("@[\w.]+", s)


# In[19]:


domain.group()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




