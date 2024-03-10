#!/usr/bin/env python3

from dotenv import load_dotenv
import os

load_dotenv()

user_password =os.getenv('USER_PASSWORD')
user_id =os.getenv("USER_ID")

print("User Password Is =",user_password)
print("User Id =",user_id)



