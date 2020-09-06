#!/usr/bin/env python
# coding: utf-8

# # you are all pilots,you want to land a plane safely ,so altitude required for landing a plane is 1000ft,it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask the pilot to "come down to 1000ft", else if it more than 5000ft ask the pilot to "go around and try later"

# In[1]:


plane=1000


# In[2]:


if plane <= 1000:
    print("Safe to land")
elif plane <= 4500:
    print("Bring down to 1000ft")
else:
    print("Trun around")


# In[3]:


plane=4500


# In[4]:


if plane <= 1000:
    print("Safe to land")
elif plane <= 4500:
    print("Bring down to 1000ft")
else:
    print("Trun around")


# In[5]:


plane=6500


# In[6]:


if plane <= 1000:
    print("Safe to land")
elif plane <= 4500:
    print("Bring down to 1000ft")
else:
    print("Trun around")


# # Using for loop please print all the prime numbers between 1-200 using For Loop AND RANGE funtion

# In[7]:


lower = int(input("Enter lower range: "))


# In[8]:


upper = int(input("Enter upper range: "))


# In[9]:


for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)


# In[ ]:




