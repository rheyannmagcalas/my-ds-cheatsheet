import pandas as pd
import streamlit as st

st.title('MY DS Cheatsheet')


topic = st.sidebar.radio("Topics", ('Data Visualization', 'Git', 'KMeans', 'Heroku Commands', 'Conda Virtualenv',))

if topic == 'Data Visualization':
    st.markdown('<hr>', unsafe_allow_html=True)
elif topic == 'Git':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader('a. Cloning a repository:')
    st.write('1. Create new repository: https://github.com/new')
    st.write('2. Copy new repo URL')
    st.write('3. Download: https://desktop.github.com/')
    st.write('4. Open Github Desktop > Select Clone Repository from Internet')
    st.write('5. Go to URL Tab > Paste new repo URL > Specify local path > Click Clone')

    st.subheader('b. Push changes to github:')
    st.write('1. Select the files to be committed')
    st.write('2. Input your commit message and click commit')
    st.write('3. To update github repo make sure to click publish to branch ')

    st.subheader('c. Pull changes from github:')
    st.write('1. Click fetch origin')
    st.write('2. Click pull origin')

    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader('Git Commands')
    st.markdown('<table style="font-size:11px">'\
                '<thead><tr><th>Command</th><th>Command</th></tr></thead>'\
                '<tbody><td>git status</td><td>Displays the state of the working directory</td></tbody>'\
                '<tbody><td>git add your_filename</td><td>Adds a change in the working directory to the staging area.</td></tbody>'\
                '<tbody><td>git commit -m your_message</td><td>Saving Changes to local repository</td></tbody>'\
                '<tbody><td>git push origin your_branch</td><td>Command used to upload local repository to a remote repository</td></tbody>'\
                '<tbody><td>git pull origin your_branch</td><td>Command used to fetch and download content from a remote repository.</td></tbody>'\
                '<tbody><td>git stash</td><td>Command to go back to a clean working directory.</td></tbody>'\
                '<tbody><td>git log</td><td>View Information to previous commits.</td></tbody>'\
                '<tbody><td>git checkout your_commit_id</td><td>Switch branches or restore working tree files</td></tbody>'\
                '</table>', unsafe_allow_html=True)
elif topic == 'KMeans':
    st.markdown('<hr>', unsafe_allow_html=True)
    
elif topic == 'Heroku Commands':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.text('Make sure you are inside the repository')
    st.markdown('<table style="font-size:11px">'\
                '<thead><tr><th>Usage</th><th>Command</th></tr></thead>'\
                '<tbody><td>Login</td><td>heroku login -i</td></tbody>'\
                '<tbody><td>Create Instance</td><td>heroku create</td></tbody>'\
                '<tbody><td>Install your Code</td><td>git push heroku your_branch_name</td></tbody>'\
                '<tbody><td>Install your Code</td><td>git push heroku your_branch_name</td></tbody>'\
                '<tbody><td>Scaling your app to one dyno</td><td>heroku ps:scale web=1</td></tbody>'\
                '<tbody><td>Checking logs</td><td>heroku logs --tail</td></tbody>'\
                '<tbody><td>Rename Applications</td><td>heroku apps:rename newname --app oldname</td></tbody>'\
                '</table>', unsafe_allow_html=True)

    
elif topic == 'Conda Virtualenv':
    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader('What is virtualenv?')
    st.write('Virtualenv is a tool to create isolated Python environments. ')
    
    st.subheader('Steps to Create and Use Virtualenv:')
    st.markdown('<b>1. pip install virtualenv', unsafe_allow_html=True)
    st.markdown('<b>2. virtualenv <env_name>', unsafe_allow_html=True)
    st.markdown('<b>3. source <env_name>/bin/activate', unsafe_allow_html=True)
    st.markdown('<b>4. pip install ipykernel', unsafe_allow_html=True)
    st.markdown('<b>4. sudo python -m ipykernel install --user --name <env_name> --display-name "Python (myenv)"', unsafe_allow_html=True)
    st.markdown('<b>5. open jupyter notebook >> select the created virtualenv', unsafe_allow_html=True)
    
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<b>Save Installed Libraries:</b> pip freeze > requirements.txt', unsafe_allow_html=True)
    st.markdown('<b>Install Multiple Libraries:</b> pip install -r requirements.txt', unsafe_allow_html=True)
    
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<b>Delete Kernel Enviroment:</b>&nbsp;&nbsp;&nbsp;&nbsp;sudo jupyter kernelspec uninstall <env_name>', unsafe_allow_html=True)
    

