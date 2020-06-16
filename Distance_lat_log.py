#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math


# In[5]:


def get_distance(lat1, lat2, lon1, lon2):
    radians = math.radians(1)
    R = 6.3711e+06
    fi1 = lat1 * radians
    fi2 = lat2 * radians
    delta_fi = (lat2-lat1) * radians
    delta_lambda = (lon2 - lon1) * radians
    a = math.sin(delta_fi/2) * math.sin(delta_fi/2) + math.cos(fi1) * math.cos(fi2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c // 1000
    return distance
#get_distance(45.6497622, 46.0733, 21.5954733, 23.5805)

