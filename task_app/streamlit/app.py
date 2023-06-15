import streamlit as st

import requests
import altair as alt
from streamlit_option_menu import option_menu


st.set_page_config(layout="wide")

local_host = 'http://localhost:8000/'

session_state = st.session_state

def get_jwt_token(username, password):
    
    url = local_host + 'api/token/'
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        token = response.json()
        access_token = token['access']
        return access_token
    else:
        return None
    

def get_data(token):
    url = local_host + 'data/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return token
    else:
        return None

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    # st.markdown(
        
    #     <style>
    #     .login-container {
    #         background-image: url('/home/jahnavi/Downloads/pexels-anthony-)-158834.jpg');
    #         background-size: cover;
    #         height: 100vh;
    #         display: flex;
    #         align-items: center;
    #         justify-content: center;
    #     }
    #     </style>
        
    #     unsafe_allow_html=True
    #            )
    
    st.markdown("<h1 style='text-align: center; '>LOGIN PAGE</h1> <br>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        col1, col2 ,col3= st.columns(3)
        with col2:
            login_button = st.button("Login")

    if login_button:
        token = get_jwt_token(username, password)
        
        if token:
            data = get_data(token)
            
            if data:
                st.session_state['logged_in'] = True
                st.session_state['token'] = token
                st.session_state['username'] = username
                st.experimental_rerun()
            else:
                 st.write("You do not have permission to access the next page")

        else:
            st.error("Invalid username or password.")
if 'logged_in' in st.session_state and st.session_state['logged_in']:

    token=st.session_state['token']    
    userName = session_state['username']
   


    # def main():
    #     st.sidebar.title("Menu")
    #     menu = ["Todo", "History"]
    #     choice = st.sidebar.radio("Go to", menu)

    #     if choice == "Todo":
    #         #st.title("Add Task here")
    #         st.write("Click below")
    #         if st.button("Add Task"):
    #             # Perform task addition logic here
    #             task =st.text_input("task")
    #             add=st.button("ADD")
    #             if add:
    #                 st.success("Task added successfully!")

    #     elif choice == "History":
    #         st.title("History")
    #         # Add your history implementation here

    # if __name__ == "__main__":
    #     main()

    selected = option_menu(
        menu_title="Menu",
        options= ["To-Do","History"],
        orientation = "horizontal",
    )
    if selected == "To-Do":
        st.sidebar.title("tasks list")
        task = st.text_input("Task")
        add = st.button("ADD TASK")
        
        if add:
            data ={
            "user ":userName,
            "task" :task,
            "description":"",
            "status":"In Progress",
        }
            url=local_host+'todo/?type=create'
            headers = {'Authorization': f'Bearer {token}'}
            response=requests.post(url,headers=headers,params=data)
            if response.status_code == 200:
                st.success("added")
        

    
   