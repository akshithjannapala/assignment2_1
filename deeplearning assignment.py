#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D


# In[5]:


def h11(x1,x2):
    return 1/(1 + np.exp(-(x1 + 50*x2 + 100)))


# In[6]:


def h12(x1,x2):
    return 1/(1 + np.exp(-(x1 + 50*x2 - 100)))


# In[7]:


def h13(x1,x2):
    return 1/(1 + np.exp(-(50*x1 + x2 + 100)))


# In[8]:


def h14(x1,x2):
    return 1/(1 + np.exp(-(50*x1 + x2 - 100)))


# In[9]:


def h21(x1,x2):
    return h11(x1,x2) - h12(x1,x2)


# In[10]:


def h22(x1,x2):
    return h13(x1,x2) - h14(x1,x2)


# In[11]:


def h31(x1,x2):
    return h21(x1,x2) + h22(x1,x2)


# In[12]:


def f(x1,x2):
    return 1/(1 + np.exp(-(100*h31(x1,x2) - 200)))


# In[13]:


x1 = np.arange(-5,5,0.01)
x2 = np.arange(-5,5,0.01)


# In[14]:


X, Y = np.meshgrid(x1, x2)


# In[15]:


from mpl_toolkits.mplot3d import axes3d, Axes3D


# In[16]:


Z = h11(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h11');


# In[17]:


Z = h12(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x_1')
ax.set_ylabel('x_2')
ax.set_zlabel('h12');


# In[18]:


Z = h13(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h13');


# In[19]:


Z = h14(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h14');


# In[20]:


Z = h21(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h21');


# In[21]:


Z = h22(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h22');


# In[22]:


Z = h31(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h31');


# In[23]:


Z = f(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f');


# In[ ]:




