#!/usr/bin/env python
# coding: utf-8

# # 

# # LIST

# ### 1. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

# In[12]:


values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# ### 2. Write a Python program to display the first and last colors from the following list.
#    color_list = ["Red","Green","White" ,"Black"]

# In[13]:


color_list = ["Red","Green","White" ,"Black"]
print("%s , %s" %(color_list[0],color_list[-1]))


# ### 3. Write a Python program to print the even numbers from a given list.

# In[14]:


List = [1,2,3,4,5,6,7,8,9]

List1 = [num for num in List if num % 2 == 0]
print(List1)


# # 

# # MODULE

# ### 1. Write a Python program to calculate number of days between two dates. Hint: use Datetime package/module.

# In[16]:


from datetime import date
first = date(2014, 7, 2)
last = date(2014, 7, 11)
day = last - first
print(day.days, "days")


# # 

# # FUNCTIONS

# ### 1. Write a Python program to get the volume of a sphere with radius 6.

# In[17]:


pi = 3.141
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# ### 2. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum hint: write User defined functions

# In[18]:


def sum_three(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_three(1, 2, 3))
print(sum_three(3, 3, 3))


# ### 3. Write a Python program to count the number 4 in a given list.

# In[19]:


list = [1,4,6,8,4,9,4]
list.count(4)


# ### 4. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 

# In[20]:


numbers = [399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
            815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
            958,743, 527]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x,end=" ")


# ### 5. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

# In[21]:


for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
      print (x,end=" ")


# ### 6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# In[22]:


for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x,end=' ')


# ### 7. Write a Python program to get the Fibonacci series between 0 to 50.

# In[23]:


x,y=0,1

while y<50:
    print(y,end=" ")
    x,y = y,x+y


# ### 8. Write a Python program to get the Fibonacci series between 0 to 50.

# In[24]:


x,y=0,1

while y<50:
    print(y,end=" ")
    x,y = y,x+y


# ### 9. Write a Python function that takes a list and returns a new list with unique elements of the first list.

# In[25]:


def unique_list(l):
  a = []
  for x in l:
    if x not in a:
      a.append(x)
  return a

print(unique_list([1,2,3,3,3,3,4,5]))


# # 

# # STRINGS

# ### 1. Write a Python program to concatenate all elements in a list into a string and return it.

# In[141]:


def concatenate_list_data(list):
    result= ''
    for num in list:
        result += str(num)
    return result

print(concatenate_list_data([1, 5, 12, 2]))


# In[142]:


def Concatenate(list):
    for i in list:
        print(str(i), end='')
Concatenate([1, 5, 12, 2])


# # 

# # DICTIONARY

# ### 1. Write a Python script to concatenate following dictionaries to create a new one.

# In[145]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)


# # 

# # SERIES

# ### 1. Write a Python program to add, subtract, multiple and divide two Pandas Series.

# In[26]:


import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])

print("Add two Series:")
ds = ds1 + ds2
print(ds)

print("Subtract two Series:")
ds = ds1 - ds2
print(ds)

print("Multiply two Series:")
ds = ds1 * ds2
print(ds)

print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


# # 

# # DATA FRAME

# ### 1.  Write a Pandas program to select the specified columns and rows from a given data frame. 

# In[150]:


import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [0, 1]])


# ### 2. Use Crime dataset from LMS

# In[27]:


import pandas as pd

df_crime = pd.read_csv('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\crime_data.csv')


# ###### I) find the aggregations like all moments of business decisions for all columns,value counts.

# In[155]:


# aggregations for all columns
aggregations = df_crime.agg(['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'count'])

# value counts for all columns
value_counts = df_crime.value_counts()

print("Aggregations\n", aggregations)
print("\n\nValue Counts\n", value_counts)


#  ###### II) do the plottings like plottings like histogram, boxplot, scatterplot, barplot, piechart,dot chart.

# In[157]:


import matplotlib.pyplot as plt

df_crime.plot(kind = 'hist')

plt.show()


# In[158]:


df_crime.plot(kind = 'box')

plt.show()


# In[159]:


df_crime.plot(kind = 'scatter', x = 'Unnamed: 0', y = 'Assault')

plt.show()


# In[160]:


df_crime.plot(kind = 'bar')

plt.show()


# In[161]:


df_crime.plot(kind = 'pie', y = 'Murder')

plt.show()


# ### 3. Use mtcars dataset from LMS

# In[ ]:


import pandas as pd

df_mtcars = pd.read_csv('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\mtcars.csv')


# ###### A) delete/ drop rows-10 to 15 of all columns

# In[165]:


df_mtcars.drop(range(0,16))


# ###### B) drop the VOL column

# In[167]:


df_mtcars.drop('vs', axis=1)


# ###### C) write the forloop to get value_counts of all cloumns

# In[169]:


for column in df_mtcars.columns:
    print(df_mtcars[column].value_counts())


# ### 4. Use Bank Dataset from LMS

# In[4]:


import pandas as pd

df_bank = pd.read_csv('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\bank-full.csv')


# ###### A) change all the categorical columns into numerical by creating Dummies and using label encoder.

# In[5]:


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

label = le.fit_transform(df_bank)


# In[6]:


label


# ###### B) rename all the column names DF

# In[7]:


df_bank.columns


# In[8]:


df_bank.rename(columns = {'age' : 'DF'})


# In[9]:


df_bank.columns


# In[10]:


bank_pd = pd.DataFrame(df_bank)
  
# Before renaming the columns
print(bank_pd)
  
bank_pd.rename(columns = {'age':'TEST'})


# ###### C) Rename only one specific column in DF

# In[11]:


df_bank.rename(columns = {'age' : 'DF'})


# ### 5. After doing all the changes in bank data(Q19). save the file in your directory in Csv Format.

# In[14]:


df_bank.to_csv('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\Bank_df.csv')


# # 

# # Basic Programs

# ### 1. Write Python Programs to use various operators in Python

# In[21]:


# 1.Arithmetic Operator

a = 6
b = 4
 
# Addition
add = a + b
 
# Subtraction
sub = a - b
 
# Multiplication
mul = a * b

# division
div = a / b
 
# Modulo
mod = a % b
 
# Power
p = a ** b
 
# print results
print('Addition :',add)
print('Subtration :',sub)
print('Multiplication :',mul)
print ('Division : ', div) 
print('Modulo :',mod)
print('Power :',p)


# In[32]:


# 2.Comparison Operators

a = 15
b = 10

# Greater than
print('a > b =',a > b)

# Less than
print('a < b =',a < b)

# Equal to
print('a == b =',a == b)

# Not equal to
print('a != b =',a != b)

# greater than or equal to
print('a >= b =', a >= b)

# less than or equal to
print('a <= b =', a <= b)


# In[37]:


# 3.Logical Operators

a = True
b = False
 
# AND operator
print(a and b)

# OR operator
print(a or b)

# NOT operator
print(not a)


# In[41]:


# 4.Assignment Operators

# Equal to operator
a = 5
b = a
print(b)

# Addition assignment operator
x = 5
y = 7
x += y
print(x)

# Multiplication assignment operator
p = 6
q = 4
p *= q
print(p)


# In[45]:


# 5.Bitwise Operators

# Bitwise AND operator
a = 10
b = 7
c = a & b
print(c)

# Bitwise OR operator
x = 15
y = 20
z = x | y
print(z)

# Bitwise NOT operator
p = 10
q = ~p
print(q)


# ### 2. Create list of elements and slice and dice it

# In[47]:


# Creating a list of elements
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Printing the entire list
print(my_list)

# Slicing the list from index 2 to index 5
print(my_list[2:5])

# Slicing the list from index 0 to index 6 (exclusive) with a step of 2
print(my_list[0:6:2])

# Slicing the list from index -3 to the end of the list
print(my_list[-3:])

# Reversing the list using slicing
print(my_list[::-1])


# ### 3. Using while loop accept numbers until sum of numbers is less than 100

# In[2]:


# Initializing the sum variables
sum = 0

# Accepting numbers from the user until their sum is less than 100
while sum < 100:
    num = int(input("Enter a number: "))
    sum = sum + num

# Printing the sum of numbers entered
print("Sum of entered numbers:", sum)


# ### 4.Write a python program Read & write Excel files 

# In[6]:


import openpyxl

# Open the workbook
workbook = openpyxl.load_workbook('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\Read & write Excel.xlsx')

# Get the active worksheet
worksheet = workbook.active

# Read a cell value
cell_value = worksheet['A1'].value
print(cell_value)

# Write a value to a cell
worksheet['B1'] = 'Hello, World!'

# Save the workbook
workbook.save('D:\\Sinchal\\Study\\EXCEL R\\DATA ANALYTICS\\Assignment\\Python\\Read & write Excel.xlsx')


# ### 5.Write a python program to scrape reviews from a commercial web site

# In[37]:


import requests
from bs4 import BeautifulSoup

# Set the URL of the page to scrape
url = 'https://www.amazon.in/product-reviews/B09G9HD6PD/ref=cm_cr_arp_d_viewpnt_lft?ie=UTF8&filterByStar=positive&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar'

# send a GET request to the URL
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


for item in reviews:
    
    # extract the reviewer's name
    reviewer_name = item.find('span', class_='a-profile-name').text
    
    # extract the review text
    review_text = item.find('a', {'data-hook': 'review-title'}).text.strip()
    
    # extract the rating
    rating = item.find('i', {'data-hook': 'review-star-rating'}).text
    
    # print the results
    print('Reviewer Name:', reviewer_name)
    print('Review Text:', review_text)
    print('Rating:', rating)
    print('-----------------------')


# ### 6. Create a 3x3 matrix with values ranging from 2 to 10 using numpy

# In[40]:


import numpy as np

# create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)


# ### 7.Write a Python program to convert a list of numeric value into a one-dimensional NumPy array

# In[42]:


import numpy as np

# create a list of numeric values
num_list = [2, 4, 6, 8, 10]

# convert the list to a one-dimensional NumPy array
num_array = np.array(num_list)

print(num_array)


# ### 8.Write a Python program to create a null vector of size 10 and update sixth value to 11.

# In[43]:


import numpy as np

# create a null vector of size 10
null_vector = np.zeros(10)

# update the sixth value to 11
null_vector[5] = 11

print(null_vector)

