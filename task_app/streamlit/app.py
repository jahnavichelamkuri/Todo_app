from turtle import pd
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

    # if _name_ == "_main_":
    #     main()

    selected = option_menu(
        menu_title="Menu",
        options= ["To-Do","History"],
        icons=["card-list","clock-history"],
        menu_icon="cast",
        default_index=0,
        orientation = "horizontal",
    )
    if selected == "To-Do":
        col1, col2 = st.columns([2, 1])
        with col1:
            st.title("To-Do")
            task = st.text_input("Task")
            add = st.button("ADD TASK")
            data ={
                "user":userName,
                "task" :task,
                "description":"",
                "status":"In Progress",
            }
            if add:
                url=local_host+'todo/?type=create'
                headers = {'Authorization': f'Bearer {token}'}
                response=requests.post(url,headers=headers,params=data)
                if response.status_code == 200:
                    st.success("added")
                else:
                    st.error("Failed")
            
        with col2:
            # st.sidebar.title("Menu")
            st.title("Tasks List")
            url = local_host + 'todo/?type=fetch_data'
            headers = {'Authorization': f'Bearer {token}'}
            data = {
                "user" :userName
            }
            response = requests.get(url, headers=headers,params=data)
            if response.status_code == 200:
                data = response.json()
                tasks = data['task']

                # for i in range(len(tasks)):
                #     st.write(tasks[i])
                for item in tasks:
                    task_completed=st.checkbox(item,key=item)
                # for item in tasks:
                #     button=st.button("item")
                    if task_completed:
                        description = st.text_area("Description")
                        add = st.button("click")
                        if add:
                            url=local_host+'todo/?type=update'
                            headers = {'Authorization': f'Bearer {token}'}
                            data={
                                "user":userName,
                                "task":item,
                                "description":description,
                                "status":"done",
                            }
                            response=requests.post(url,headers=headers,params=data)
                            if response.status_code==200:
                                data=response.json()
                                st.write(data)
                                st.write(data['message'])
                                
                

    if selected == "History":
        
        url=local_host+'todo/?type=history'
        headers = {'Authorization': f'Bearer {token}'}
        data={
            "user":userName,
        }
        
        response=requests.post(url,headers=headers,params=data)
                        
        if response.status_code == 200:
            data = response.json()
            tasks = data['tasklist']
            for i in range(len(tasks)):
                st.subheader(tasks[i])
        else:
            st.error(f'Error: {response.status_code}')