#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import csv
import time


# In[2]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# In[3]:


try:
    x = open('UdemyCourses.csv')
    print("File exist\nFirst line of file:")
    r=x.readline()
    print(r)
except:
    print("File not exist")  


# In[4]:


print(os.getcwd())


# In[5]:


print("File size:", os.path.getsize(r"C:\Users\lewin\Desktop\Projekt_Python\UdemyCourses.csv"), "bytes")


# In[6]:


print(time.ctime(os.path.getctime("UdemyCourses.csv"))) 


# In[7]:


UdemyCourses=pd.read_csv("UdemyCourses.csv")
UdemyCourses


# In[8]:


display(UdemyCourses[['course_title','price']])  


# In[9]:


display(UdemyCourses.iloc[1:6])


# In[10]:


print(UdemyCourses.iloc[1000,:])


# In[11]:


from csv import DictReader
with open('UdemyCourses.csv', 'r', encoding="utf8") as CoursesDictionary:
    Dictionary_Reader = DictReader(CoursesDictionary)
    for row in Dictionary_Reader:
        print(row)


# In[12]:


UdemyCourses.info()


# In[13]:


UdemyCourses.price.describe() 


# In[14]:


UdemyCourses.sort_values(['price','num_subscribers'], ascending=[1,0]) 


# In[15]:


UdemyCourses.loc[(UdemyCourses["price"]==0)]


# In[16]:


Less100 = UdemyCourses.loc[(UdemyCourses["num_subscribers"]<100)]
Less100


# In[17]:


Less100.reset_index(drop=True, inplace=True) 
Less100


# In[ ]:


Less100.to_csv("Less100Subscribtions.csv")


# In[18]:


Reviews = UdemyCourses.loc[UdemyCourses['num_reviews']>=500] 
Reviews.count()


# In[19]:


MaxSub=UdemyCourses["num_subscribers"].max()
Max = UdemyCourses.loc[(UdemyCourses["num_subscribers"]==MaxSub)]
Max


# In[20]:


MaxP=UdemyCourses["price"].max()
MaxPrice = UdemyCourses.loc[(UdemyCourses["price"]==MaxP)]
MaxPrice


# In[21]:


UdemyCourses[(UdemyCourses.is_paid==False)&(UdemyCourses.subject=="Web Development")]


# In[22]:


BeginnerCourses=UdemyCourses.loc[~(UdemyCourses['level'].str.contains('Beginner'))]
BeginnerCourses


# In[23]:


import re 
UdemyCourses.loc[UdemyCourses['course_title'].str.contains("Photoshop", regex=True)] 


# In[24]:


UdemyCourses.content_duration.mean()


# In[25]:


UdemyCourses.groupby(['level']).mean() 


# In[26]:


UdemyCourses.sort_values(by=['published_timestamp'], ascending=False) 


# In[27]:


sum=UdemyCourses['count']=1
UdemyCourses.groupby(["subject"]).sum()['count']


# In[28]:


UdemyCourses.groupby(['level']).count()['count']


# In[29]:


UdemyCourses['price'].hist()


# In[ ]:


UdemyCourses['level'].hist()


# In[30]:


def priceRange(min,max):
    display(UdemyCourses.loc[(UdemyCourses.price >= min) & (UdemyCourses.price <= max)])


# In[31]:


priceRange(20,100)


# In[33]:


def searchSubject():
    try:
        searched = int(input("Choose a number to select courses: \n 1.Business Finance\n 2.Graphic Design\n 3.Musical Instruments\n 4.Web Development\n"))
        if searched == 1:
            display(UdemyCourses.loc[UdemyCourses['subject'] == "Business Finance"])
        elif searched == 2:
            display(UdemyCourses.loc[UdemyCourses['subject'] == "Graphic Design"])
        elif searched == 3:
            display(UdemyCourses.loc[UdemyCourses['subject'] == "Musical Instruments"])
        elif searched == 4:
            display(UdemyCourses.loc[UdemyCourses['subject'] == "Web Development"])
        else:
            raise ValueError
    except ValueError as y:
        print("Input a correct number!", y)      


# In[34]:


searchSubject()


# In[35]:


def searchKeyword(keyword):
    display(UdemyCourses.loc[(UdemyCourses['course_title'].str.contains(keyword))])   


# In[36]:


searchKeyword("HTML")


# In[37]:


def searchPopular(n):
    display(UdemyCourses.nlargest(n, ['num_subscribers']))


# In[38]:


searchPopular(10)


# In[39]:


def searchID(ID):
    display(UdemyCourses.loc[(UdemyCourses['course_id']==ID)])


# In[40]:


searchID(130064)


# In[ ]:


with open('UdemyCourses.csv', 'a', newline='') as NewCourses:
    Writer = csv.writer(NewCourses, delimiter=',')
    Writer.writerow([423542] + ['Python - Free Tutorial'] + ["https://www.udemy.com/Python-Free-Tutorial"] + [True] +[20] + [400] + [21] +[20]+["All Levels"] + [2] +["2015-11-19T14:22:47Z"] +["Business Finance"])
    Writer.writerow([625311] + ['XML Basic Course'] + ["https://www.udemy.com/XMLBasicCourse"] + [False] +[0] + [4009] + [212] +[230]+["Beginner Level"] + [233] +["2016-12-19T10:11:47Z"] +["Web Development"])
    Writer.writerow([625311] + ['MVC Expert'] + ["https://www.udemy.com/MVCExper"] + [True] +[1000] + [1010] + [112] +[244]+["Expert Level"] + [533] +["2020-10-15T08:11:47Z"] +["Web Development"])


# In[ ]:


UdemyCourses=pd.read_csv("UdemyCourses.csv")
UdemyCourses


# In[41]:


UdemyCourses=UdemyCourses[UdemyCourses.course_id != 297602]


# In[ ]:


searchID(297602)


# In[ ]:




