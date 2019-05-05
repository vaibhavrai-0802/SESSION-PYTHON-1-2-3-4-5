#!/usr/bin/env python
# coding: utf-8

# # Python 1,2,3,4 & 5: Assignment 1 

# ## 2.1. Problem Statement: PYTHON 1

# In[5]:


#2
num_list = []
for number in range (2000, 3200):
    if number%7 == 0 and number%5 != 0:
        num_list.append(str(number))
print (",".join(num_list))


# In[7]:


#3
first_name = input('enter your first name: ')
last_name = input('enter your last name: ')
required_string = (first_name + " " +last_name)
print (required_string[::-1])


# In[8]:


#4
import math
dia = 12
radius = dia/2
Volume = 4/3 * math.pi * radius **3
print (Volume)


# ## 2.2. Problem Statement: PYTHON 2

# In[10]:


#1
input_num = input('Enter comma seperated numbers: ')
out_list = input_num.split(',')
print (out_list)


# In[11]:


#2
patern = '*'
for i in range (5):
    for num in range(i):
        print (patern, end = "")
    print (end ='\n')
for i in range (6, 0, -1):
    for num in range(i):
        print (patern, end="")
    print (end ='\n')


# In[12]:


#3
input_string = input("Enter the string to be reversed: ")
out_string = input_string[::-1]
print (out_string)


# In[13]:


#4
input_para = '''WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, 
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens'''
sample_out = '''WE, THE PEOPLE OF INDIA,
                    having solemnly resolved to constitute India into a SOVEREIGN, !
                        SOCIALIST, SECULAR, DEMOCRATIC
                         REPUBLIC and to secure to all its citizens'''
input_para = input_para.split(" ")
for string in input_para:
    if ('\n' in string):
        string = (string.strip('\n'))
    
    print (string, end = ' ')
    if ('INDIA,' in string):
        print (end ='\n\t')
    elif('SOVEREIGN,' in string):
        print (end = '!\n\t\t')
    elif('DEMOCRATIC' in string):
        print (end = ('\n\t\t '))


# ## 2.3. Problem Statement: PYTHON 3

# In[30]:


#1.1
def myreduce(function, iterable, initial_val = None):
    seq = iter(iterable)
    if initial_val == None:
        red_item = next(seq)
    else:
        red_item = initial_val
    for item in seq:
        red_item = function(red_item, item)
    return red_item


# In[28]:


def multiply(x,y):
    return x*y


# In[29]:


samp_lst = [2,3,4]
myreduce(multiply, samp_lst)


# In[24]:


#1.2
def myfilter(function, iterable):
    result_list = []
    for item in iterable:
        if function(item):
            result_list.append(item)
    return result_list


# In[25]:


def even_chk(num):
    if num%2 == 0:
        return True


# In[26]:


sample_list = range(20)
list(myfilter(even_chk, sample_list))


# In[32]:


#2
string = "ACADGILD"
result = [i for i in string]
print (result)


# In[33]:


in_string = ['x','y','z']
re_list = []
re_list = [(i*j) for i in in_string for j in range(1,5)]
print (re_list)


# In[34]:


in_string = ['x','y','z']
re_list = []
re_list =[(i*j) for j in range(1,5) for i in in_string]
print (re_list)


# In[37]:


inp_lst = [3,4,5,6]
op_lst1 = []
op_lst2 = []
op_lst1 = [[j] for i in inp_lst for j in range(i-1, i+2) if i <= 5]
op_lst2 = [[i-1, i, i+1] for i in inp_lst]
print (op_lst1, op_lst2)


# In[36]:


in_lst = [1,2,3]
out_lst = [(j,i) for i in in_lst for j in in_lst]
print (out_lst)


# In[22]:


#3
def longestWord(list_of_words):
    max_len = 0
    longest_word = ''
    for word in list_of_words:
        if len(word) > max_len:
            longest_word = word
            max_len = len(word)
    return longest_word


# In[31]:


list_words = ['Implement', 'a', 'function', 'longestWord', 'that', 'takes', 'a', 'list', 'of', 'words',
              'and', 'returns', 'the', 'longest', 'one']
longestWord(list_words)


# ## 2.4. Problem Statement: PYTHON 4

# In[14]:


#1.1
class Triangle:
    def get_length(self):
        self.side1 = input("Please enter the length of side 1: ")
        self.side2 = input("Please enter the length of side 2: ")
        self.side3 = input("Please enter the length of side 3: ")
        return [self.side1, self.side2, self.side3]
    
class Area(Triangle):
    def area_func(self):
        length_list = self.get_length()
        a = int(length_list[0])
        b = int(length_list[1])
        c = int(length_list[2])
        s = (a+b+c/2)
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area


# In[15]:


cal_area = Area()
cal_area.area_func()


# In[16]:


#1.2
def filter_long_words(word_list, desired_length):
    new_word_list = []
    for word in word_list:
        word = word.strip(' ')
        if len(word) > desired_length:
            new_word_list.append(word)
    return (new_word_list)


# In[17]:


word_list = input('Enter some words with comma separeated.\nPress enter at the end.\n')
desired_length = int(input('Enter desired word length: '))
word_list = word_list.split(',')
filter_long_words(word_list, desired_length)


# In[18]:


#2.1
word_list = ['ab', 'cde', 'erty']
def map_word_length(word):
    return (len(word))


# In[19]:


word_len_list = list(map(map_word_length, word_list))
word_len_list


# In[20]:


#2.2
def check_if_vowel(character):
    if character in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

chara = input("PLease enter a character: ")
if len(chara) == 1:
    print (check_if_vowel(chara))
else:
    print ("Please enter single character/letter")


# ## 2.5. Problem Statement: PYTHON 5

# In[2]:


#1
def div_func(num, divisor):
    try:
        div = num/divisor
        print ("divison successful")
    except Exception as e:
        print ("Exception raised: ", e)
        print ("divison unsuccessful")


# In[3]:


div_func(5, 0)


# In[4]:


#2
subjects = ["Americans","Indians"]
verbs = ["play","watch"]
objects = ["Baseball","Cricket"]

for item1 in subjects:
    for item2 in verbs:
        for item3 in objects:
            print (item1 + ' ' + item2 + ' ' + item3)

