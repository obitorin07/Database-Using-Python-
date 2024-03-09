#!/usr/bin/env python3

# Why import the 'os' module? Because it allows us to access environment variables.
import os 

#Before Using Enviroment Variable
User_Name ='obitorin'
password ='123456'
Host_Name ='localhost'

print("The User Name is ",User_Name)
print('The Pass is',password)
print("The Host is",Host_Name)

#After using env variable
#without displaying credentials to public 

User_Name =os.environ.get('User_Name')
password =os.environ.get('Password')
Host_Name =os.environ.get('Host_Name')

print("The User Name is ",User_Name)
print('The Pass is',password)
print("The Host is",Host_Name)
