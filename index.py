import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st


st.set_page_config(
    page_title="My DS Cheatsheet",
    layout="wide",
    initial_sidebar_state="expanded",
)


topic = st.sidebar.radio("Topics", ('Data Visualization', 'Git', 'KMeans', 'Heroku Commands'))



if topic == 'Data Visualization':
    st.markdown('<hr>', unsafe_allow_html=True)

    data_visualization_option = st.selectbox(
        'Chart',  ('Column', 'Bar', 'Line'))

    if data_visualization_option == 'Column':
        st.markdown('A column chart is used to show a <b>COMPARISON</b> among different items, or it can show a comparison of items over time.', unsafe_allow_html=True)
        st.markdown('<b>Design Best Practices:</b>', unsafe_allow_html=True)
        st.markdown('<ul>\
            <li>Use consistent colors throughout the chart, selecting accent colors to highlight meaningful data points or changes over time.</li>\
            <li>Use horizontal labels to improve readability.</li>\
            <li>Start the y-axis at 0 to appropriately reflect the values in your graph.</li></ul>', unsafe_allow_html=True)
        
        st.markdown('<b>Example:</b>', unsafe_allow_html=True)
        tips = sns.load_dataset("tips")

        col1, col2 = st.beta_columns(2)

        fig = plt.figure(figsize=(5,3.75))
        ax = sns.barplot(x="day", y="total_bill", data=tips, ci = None)
        ax.set_title('Sample Column Seaborn Chart')
        ax.set(xlabel='Total Bill', ylabel='Day')
        col1.pyplot(fig)

        data_canada = px.data.gapminder().query("country == 'Canada'")
        fig = px.bar(data_canada, x='year', y='pop',  
                    labels={
                            "year": "Year",
                            "pop": "Population"
                        },
                    title="Sample Column Plotly Chart")
        col2.plotly_chart(fig, use_container_width=True)

        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns
            tips = sns.load_dataset("tips")

            fig = plt.figure(figsize=(15,8))
            ax = sns.barplot(x="day", y="total_bill", data=tips, ci = None)
            ax.set_title('Total Bill Per Day')
            ax.set(xlabel='Total Bill', ylabel='Day')
            # plot.show()

        st.markdown('<b>Plotly Code:</b>', unsafe_allow_html=True)
        with st.echo():
            data_canada = px.data.gapminder().query("country == 'Canada'")
            fig = px.bar(data_canada, x='year', y='pop',  
                        labels={
                                "year": "Year",
                                "pop": "Population"
                            },
                        title="Canada Population")
            #fig.show()
    elif data_visualization_option == 'Bar':
        st.markdown('A bar graph, basically a horizontal column chart, should be used to avoid clutter when one data label is long or if you have \
            <b>more than 10 items to compare</b>. This type of visualization can also be used to <b>display negative numbers.</b>', unsafe_allow_html=True)
        st.markdown('<b>Design Best Practices:</b>', unsafe_allow_html=True)
        st.markdown('<ul>\
            <li>Use consistent colors throughout the chart, selecting accent colors to highlight meaningful data points or changes over time.</li>\
            <li>Use horizontal labels to improve readability.</li>\
            <li>Start the y-axis at 0 to appropriately reflect the values in your graph.</li></ul>', unsafe_allow_html=True)
        
        st.markdown('<b>Example:</b>', unsafe_allow_html=True)
        col1, col2 = st.beta_columns(2)

        df = pd.DataFrame(np.random.randint(0,10,size=(10, 4)), columns=list('ABCD'))
        fig = plt.figure(figsize=(5,3.75))
        ax = sns.barplot(data=df, orient = 'h', ci = None)
        ax.set_title('Sample Bar Graph')
        ax.set(xlabel='X-Axis', ylabel='Y-Axis')
        col1.pyplot(fig)

        fig = go.Figure(go.Bar(
                    x=[20, 14, 23],
                    y=['giraffes', 'orangutans', 'monkeys'],
                    orientation='h',
                    marker=dict(
                        color='rgba(246, 78, 139, 0.6)',
                        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
                    ),
                ), layout=go.Layout(
                        title=go.layout.Title(text="Sample Bar Plotly Chart"),
                        xaxis_title="X Axis Title",
                        yaxis_title="Y Axis Title",
                    ))

        col2.plotly_chart(fig, use_container_width=True)

        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import matplotlib.pyplot as plt
            import numpy as np
            import pandas as pd
            import seaborn as sns

            df = pd.DataFrame(np.random.randint(0,10,size=(10, 4)), columns=list('ABCD'))
            plt.figure(figsize=(15,8))
            ax = sns.barplot(data=df, orient = 'h', ci = None)
            ax.set_title('Sample Bar Graph')
            ax.set(xlabel='X-Axis', ylabel='Y-Axis')
            plt.show()

        st.markdown('<b>Plotly Code:</b>', unsafe_allow_html=True)
        with st.echo():
            fig = go.Figure(go.Bar(
                    x=[20, 14, 23],
                    y=['giraffes', 'orangutans', 'monkeys'],
                    orientation='h',
                    marker=dict(
                        color='rgba(246, 78, 139, 0.6)',
                        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
                    ),
                ), layout=go.Layout(
                        title=go.layout.Title(text="Sample Bar Plotly Chart"),
                        xaxis_title="X Axis Title",
                        yaxis_title="Y Axis Title",
                    ))

    elif data_visualization_option == 'Line':
        st.markdown('A line graph reveals <b>trends or progress over time</b> and can be used to show many different categories of data. \
            You should use it when you chart a <b>continuous data set</b>.', unsafe_allow_html=True)
        st.markdown('<b>Design Best Practices:</b>', unsafe_allow_html=True)
        st.markdown('<ul>\
            <li>Use solid lines only.</li>\
            <li>Don\'t plot more than four lines to avoid visual distractions.</li>\
            <li>Use the right height so the lines take up roughly 2/3 of the y-axis\' height.</li></ul>', unsafe_allow_html=True)
        
        st.markdown('<b>Example:</b>', unsafe_allow_html=True)

        fig = plt.figure(figsize=(7,3.5))
        data = sns.load_dataset("iris") 
        
        ax = sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
        ax.set_title('Sample Line Graph')
        ax.set(xlabel='X-Axis', ylabel='Y-Axis')
        st.pyplot(fig)

        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import seaborn as sns 
            import matplotlib.pyplot as plt 
            

            plt.figure(figsize=(15,6))
            data = sns.load_dataset("iris") 
            
            ax = sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
            ax.set_title('Sample Line Graph')
            ax.set(xlabel='X-Axis', ylabel='Y-Axis')
            #plt.show()


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
    

