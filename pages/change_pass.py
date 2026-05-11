import streamlit as st
import time
import pymongo
st.header("Change Password")
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["cv"]
my=mydb["user_info"]
t1=st.text_input("Old Password")
t2=st.text_input("New Password")
if st.button("Change Password",key="b"):
    res=my.update_one({"password":t1},{'$set':{"password":t2}})
    st.success("Password Changed Successfully!!!")
    st.success(f"value:{res}")
