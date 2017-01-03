
# coding: utf-8

# In[139]:

# vocabdensity.py
# calculates vocab density (vd) of all .txt files in local folder all-chats
# results will be written over every time the script is run!
# to preserve results, change filename @ vdfile file obj declaration

# question: it's great that os.walk() works to only capture .txt files in
# all-chats but i'm wondering why it's not also grabbing results.txt
# and stopwords.txt in cwd?


# In[130]:

import os
os.getcwd()

# get path name
cwd = str(os.getcwd())


# In[138]:

# put all files in all-chats in files[]
for cwd, folder, f in os.walk(cwd):
    files = f
    
# remove all non .txt files
for f in files:
    if f.endswith('.txt'):
        pass
    else:
        files.remove(f)


# In[135]:

# import stopwords from 'stop-words.txt'

with open('stopwords.txt', 'r') as f:
    stopwords = f.read().split()


# In[124]:

# declare global variables for calculating vd average

numchats = float(len(files))
vdtotal = 0.0

# open file to write to
# change filename to preserve results

vdfile = open('results.txt', 'w')

for filename in files: 
    #this filepath could be refined lol
    with open(cwd + '/' + filename, 'r') as f:
        
        # reset variables
        wordbank = []
        wordlist = []
        denominator = 0
        numerator = 0
        
        # create wordbank + get total number of words (denominator)
        wordbank = f.read().split()
        denominator = float(len(wordbank))
    
        # remove stopwords
        for word in wordbank:
            if word in stopwords:
                wordbank.remove(word)
            
        # create list of unique words + get total number of unique words (numerator)
        for word in wordbank:
            if word not in wordlist:
                wordlist.append(word)
                
        numerator = float(len(wordlist))
    
        # calculate vocab density  
        vd = (numerator/denominator)
        vdtotal = vdtotal + vd
        
        # write each result to vocabdensity.txt
        vdfile.write(filename + ": " + str(vd) + "\n")

vdfile.write('The average is: ' + str(vdtotal/numchats))
vdfile.close()

print 'Done'

os.system("open " + 'results.txt')


# In[ ]:




# In[ ]:



