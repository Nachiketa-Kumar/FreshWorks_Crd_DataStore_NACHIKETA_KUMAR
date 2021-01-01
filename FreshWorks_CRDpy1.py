#!/usr/bin/env python
# coding: utf-8

# In[1]:


## IMPORTING LIBRARIES AND PAKAGES REQUIRES FOR RENDERING JSON AND THREADING.

import time
import json
import requests
import os
import threading
from threading import*

f1='JsonDataFile.json'
import sys

def write_file(data, f1='JsonDataFile.json'):
    with open(f1,'w')as f2:
        json.dump(data,f2,indent=4)

# This function Creates the datafile in key-value structure
def DataFile_Creation(key,val,timeframe=0,f1='JsonDataFile.json'):
    
        if(os.path.isfile(f1) and os.path.getsize(f1)>0):
            with open(f1) as np:
                d1=json.load(np)
                d2=d1
            if(key in d2):
                print("------There is an Error as-> ",key," pre-exists in the Datafile-----") 
            else:
                if(key.isalpha()):
                    if(len(d2)<(1024*1020*1024) and val<=(16*1024*1024)): #for files having sizes less than 1 GB and JSON key objects less than or equal to 16 kb only!  
                        if(timeframe==0):
                            l1=[val,timeframe]
                        else:
                            l1=[val,time.time()+timeframe]
                        if(len(key)<=32): #key of 32chars
                            d2[key]=l1
                            print(key, "Your key is Successfully Created!!")
                            write_file(d2)  
                    else:
                        print("OOPs There is an Error as ---> Your Key memory limit in the file has exceeded!!")
                else:
                    print("-------OOPs There is an ERROR--->ONLY ALPHABETS ARE ALLOWED IN THE KEY------")

        else:
            d2={}
            if(key.isalpha()):
                    if(val<=(16*1024*1024)): # for files having sizes less than 1 GB and JSON key objects less than or equal to 16 kb only! 
                        if(timeframe==0):
                            l1=[val,timeframe]
                        else:
                            l1=[val,time.time()+timeframe]
                        if(len(key)<=32): 
                            d2[key]=l1
                            print("A new Key is Created named--->",key)
                            write_file(d2)
        print("Your current data store is--->\n")
        print(d2)

# read_datastore returns the value of the corresponding key in the datastore
# parameters: key to be searched
def DataFile_Read(key):
     with open(f1) as np:
        d1=json.load(np)
        d2=d1
        print("READING THE INPUT KEY OBJET------")
        if(key not in d2):
            print("---THERE IS AN ERROR---\n--- KEY ENTERED NOT FOUND IN THE DATABASE, PLEASE ENTER A CORRECT KEY---")
        else:
            z=d2[key]
            if(z[1]!=0):
                if(time.time()<z[1]): #comparing the present time with expiry time
                    st=str(key)+":"+str(z[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                    print(st," is the merit of key",key)
                else:
                    print("-----There is an Error-->",key," time has expired for this key!-----") 
            else:
                st=str(key)+":"+str(z[0])
                print(st,"Is the merit of key",key)
        np.close()


#This Function deletes the given key object from the data file. 
def DataFile_Deletion(key):
     with open(f1) as np:
        d1=json.load(np)
        d2=d1
        print("DELETING THE GIVEN OBJECT FROM DATAFILE----->")
        if(key not in d2):
            print("There is an Error with given key-->Key not present in datafile ----> please enter a valid key present") 
        else:
            z=d2[key]
            if(z[1]!=0):
                if(time.time()<z[1]): 
                    del d2[key] #performing the deletion operation of the given key index in d2 dictionary.
                    
                    print(key," This object key has been deleted Successfully!!")
                else:
                    print("There is an Error with given key-->Time of the given key ",key," has expired") 
            else:
                
                d2.pop(key,None)
                with open('JsonDataFile.json', 'w') as df:
                    d1 = json.dump(d2, df,indent=4)
                print("Your given key",key," has been deleted successfully!! \n")
                
                print("Your current data store is--->\n")
                print(d2)
        np.close()


# In[ ]:




