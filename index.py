import folium
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from streamlit_folium import folium_static


st.set_page_config(
    page_title="My DS Cheatsheet",
    layout="wide",
    initial_sidebar_state="expanded",
)


topic = st.sidebar.radio("Topics", ('Data Wrangling', 'Data Visualization', 'Feature Engineering', 'Git', 'Unsupervised Learning', 'Heroku Commands'))

if topic == 'Data Wrangling':
    st.markdown('<hr>', unsafe_allow_html=True)
    data_wrangling_option = st.selectbox(
        'Chart',  ('Reading', 'Aggregation', 'Conditions'))
    
    if data_wrangling_option == 'Reading':
        with st.echo():
            import pandas as pd
            import numpy as np
            import matplotlib.pyplot as plt
            
            #df = pd.read_csv("schools.csv")
            
            #df.shape
            
            #df.head()
            
            #df.tail()
            
            #Check additional info
#             df.info()
            
#             # Check column names
#             df.columns
            
#             ## Check missing values
#             df.isna().sum()
            
#             ## Check for duplicates
#             df["ID"].nunique()
            
            
            
    elif data_wrangling_option == 'Aggregation':
        
        with st.echo():
            import numpy as np
            import pandas as pd
            
            df = pd.DataFrame({
                "A": [1, 1, 2, 2],
                "B": [1, 2, 3, 4],
                "C": [0.362838, 0.227877, 1.267767, -0.562860]})
            
            df.groupby('A').agg({'B': ['min', 'max', np.mean], 'C': 'sum'})
        
        
        

    elif data_wrangling_option == 'Conditions':        
        new_column_conditions = st.beta_expander('Creating New Column From Conditions')
        with new_column_conditions:        
            st.write('Option 1:')
            with st.echo():
                numbers = {'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]}
                df = pd.DataFrame(numbers,columns=['set_of_numbers'])

                df.loc[df['set_of_numbers'] <= 4, 'equal_or_lower_than_4?'] = 'True' 
                df.loc[df['set_of_numbers'] > 4, 'equal_or_lower_than_4?'] = 'False' 

            st.write('Option 2:')
            with st.echo():
                numbers = {'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]}
                df = pd.DataFrame(numbers,columns=['set_of_numbers'])

                df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')
        
    
elif topic == 'Feature Engineering':
    st.markdown('<hr>', unsafe_allow_html=True)
    
    
elif topic == 'Data Visualization':
    st.markdown('<hr>', unsafe_allow_html=True)

    data_visualization_option = st.selectbox(
        'Chart',  ('Column', 'Bar', 'Line', 'Scatterplot', 'Bubble', 'Histogram', 'Boxplot', 'Map'))

    if data_visualization_option == 'Column':
        st.markdown('A column chart is used to show a <b>COMPARISON</b> among different items, or it can show a comparison \
        of items over time.', unsafe_allow_html=True)
        st.markdown('<b>Design Best Practices:</b>', unsafe_allow_html=True)
        st.markdown('<ul>\
            <li>Use consistent colors throughout the chart, selecting accent colors to highlight meaningful data points or changes over time.</li>\
            <li>Use horizontal labels to improve readability.</li>\
            <li>Start the y-axis at 0 to appropriately reflect the values in your graph.</li></ul>', unsafe_allow_html=True)
        
        st.markdown('<b>Example:</b>', unsafe_allow_html=True)
        sns.set(style="whitegrid")
        tips = sns.load_dataset("tips")

        col1, col2 = st.beta_columns(2)

        fig_1 = plt.figure(figsize=(5,3.75))
        ax1 = sns.barplot(x="day", y="total_bill", data=tips, ci = None, color='#5499c7')
        ax1.set_title('Total Bills per Day')
        ax1.set(xlabel='Day', ylabel='Total Bills')        
        col1.pyplot(fig_1)
        
        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns
            sns.set(style="whitegrid")
            tips = sns.load_dataset("tips")

            fig = plt.figure(figsize=(5,3.75))
            ax1 = sns.barplot(x="day", y="total_bill", data=tips, ci = None, color='#5499c7')
            ax1.set_title('Total Bills per Day')
            ax1.set(xlabel='Day', ylabel='Total Bills')        
            plt.show()
        
        
        df = pd.DataFrame({'names': ['Mon', 'Tue', 'Wed', 'Thurs'], 
                           'h2': [100, 90, 80, 70]})
        
        colors = df['names'].apply(lambda x: 'red' if x =='Mon' else '#bfc9ca')
        
        fig_2 = plt.figure(figsize=(5,3.75))
        ax2 = sns.barplot(x='names', y='h2', palette=colors,  dodge=False, data=df)
        ax2.set_xticklabels(labels=df['names'], rotation=90, fontsize=15)
        ax2.set_title('Total Bills per Day')
        ax2.set(xlabel='Day', ylabel='Total Bills')   
        
        col2.pyplot(fig_2)
        
        
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns
            sns.set(style="whitegrid")            
            df = pd.DataFrame({'names': ['Mon', 'Tue', 'Wed', 'Thurs'], 
                           'h2': [100, 90, 80, 70]})
            
            colors = df['names'].apply(lambda x: 'red' if x =='Mon' else 'gray')

            fig_2 = plt.figure(figsize=(5,3.75))
            ax2 = sns.barplot(x='names', y='h2', palette=colors,  dodge=False, data=df)
            ax2.set_xticklabels(labels=df['names'], rotation=90, fontsize=15)
            ax2.set_title('Total Bills per Day')
            ax2.set(xlabel='Day', ylabel='Total Bills') 
            plt.show()
        
  

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
        ax = sns.barplot(data=df, orient = 'h', ci = None, color='#5499c7')
        ax.set_title('Sample Bar Graph')
        ax.set(xlabel='X-Axis', ylabel='Y-Axis')
        col1.pyplot(fig)

        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import matplotlib.pyplot as plt
            import numpy as np
            import pandas as pd
            import seaborn as sns

            df = pd.DataFrame(np.random.randint(0,10,size=(10, 4)), columns=list('ABCD'))
            plt.figure(figsize=(15,8))
            ax = sns.barplot(data=df, orient = 'h', ci = None, color='#5499c7')
            ax.set_title('Sample Bar Graph')
            ax.set(xlabel='X-Axis', ylabel='Y-Axis')
            plt.show()

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
        
    elif data_visualization_option == 'Scatterplot':
        st.markdown('A scatterplot is a type of data display that shows the relationship between two numerical variables', unsafe_allow_html=True)
        
        sns.set(style="whitegrid")
        tips = sns.load_dataset("tips")

        col1, col2 = st.beta_columns(2)

        fig_1 = plt.figure(figsize=(5,3.75))
        ax1 = sns.scatterplot(data=tips, x="total_bill", y="tip")
        ax1.set_title('Total Bills per Day')
        ax1.set(xlabel='Day', ylabel='Total Bills')        
        col1.pyplot(fig_1)
        
        st.markdown('<b>Seaborn Code:</b>', unsafe_allow_html=True)
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns
            sns.set(style="whitegrid")
            tips = sns.load_dataset("tips")

            fig_1 = plt.figure(figsize=(5,3.75))
            ax1 = sns.scatterplot(data=tips, x="total_bill", y="tip")
            ax1.set_title('Total Bills per Day')
            ax1.set(xlabel='Day', ylabel='Total Bills')    
            plt.show()
            
    elif data_visualization_option == 'Bubble':
        st.markdown('A bubble plot is basically a scatterplot with an additional dimension: size of points.', unsafe_allow_html=True)
        
        sns.set(style="whitegrid")
        col1, col2 = st.beta_columns(2)
        
        from gapminder import gapminder
        fig_1 = plt.figure(figsize=(5,3.75))
        data = gapminder.loc[gapminder.year == 2007]
        ax1 = sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", size="pop", legend=False, sizes=(20, 2000))
        ax1.set_title('Relationship between life expectancy (y) and gdp per capita (x)')
        ax1.set(xlabel='GDP Per Capita', ylabel='Life Expectancy') 
        col1.pyplot(fig_1)
        
        
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns
            from gapminder import gapminder 

            fig_1 = plt.figure(figsize=(5,3.75))
            data = gapminder.loc[gapminder.year == 2007]
            ax1 = sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", size="pop", legend=False, sizes=(20, 2000))
            ax1.set_title('Relationship between life expectancy (y) and gdp per capita (x)')
            ax1.set(xlabel='GDP Per Capita', ylabel='Life Expectancy') 
            plt.show()
            
    elif data_visualization_option == 'Histogram':
        st.markdown('A histogram is the most commonly used graph to show frequency distributions.', unsafe_allow_html=True)
        
        sns.set(style="whitegrid")
        col1, col2 = st.beta_columns(2)
        
        penguins = sns.load_dataset("penguins")

        fig_1 = plt.figure(figsize=(5,3.75))
        ax1 = sns.histplot(data=penguins, x="flipper_length_mm")
        ax1.set_title('Flipper_length_mm Distribution')
        ax1.set(xlabel='flipper_length_mm', ylabel='Count') 
        col1.pyplot(fig_1)
        
        
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns

            fig_1 = plt.figure(figsize=(5,3.75))
            penguins = sns.load_dataset("penguins")
            fig_1 = plt.figure(figsize=(5,3.75))
            ax1 = sns.histplot(data=penguins, x="flipper_length_mm")
            ax1.set_title('Flipper_length_mm Distribution')
            ax1.set(xlabel='flipper_length_mm', ylabel='Count') 
            plt.show()
            
    elif data_visualization_option == 'Boxplot':
        st.markdown('A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”). It can tell you about your outliers and what their values are.', unsafe_allow_html=True)
        
        col1, col2 = st.beta_columns(2)
        
        tips = sns.load_dataset("tips")

        fig_1 = plt.figure(figsize=(5,3.75))
        ax1 = sns.boxplot(x="day", y="total_bill", data=tips)
        ax1.set_title('Total Bills Per Day')
        ax1.set(xlabel='day', ylabel='Total Bill') 
        col1.pyplot(fig_1)
        
        with st.echo():
            import matplotlib.pyplot as plt
            import seaborn as sns

            fig_1 = plt.figure(figsize=(5,3.75))
            ax1 = sns.boxplot(x="day", y="total_bill", data=tips)
            ax1.set_title('Total Bills Per Day')
            ax1.set(xlabel='day', ylabel='Total Bill') 
            plt.show()
            
            
    elif data_visualization_option == 'Map':
        import folium
        from streamlit_folium import folium_static
        
        
        m = folium.Map(location = [7.6955724,122.0074178],
                       zoom_start=6, 
                       control_scale=True,
                       prefer_canvas=True)
        
        folium.Marker(
            [7.2359082, 124.2669569],
            icon=folium.Icon(color='red',icon="hospital-o", prefix='fa'),
            tooltip='COTABATO SANITARIUM'
        ).add_to(m)
        
        folium.Marker(
            [8.001110, 125.171670], popup="ACCUSAFE DIAGNOSTIC LABORATORY", tooltip='ACCUSAFE DIAGNOSTIC LABORATORY'
        ).add_to(m)
        
        folium_static(m)
        
        
        with st.echo():
            m = folium.Map(location = [7.6955724,122.0074178],
                       zoom_start=6, 
                       control_scale=True,
                       prefer_canvas=True)
        
            folium.Marker(
                [7.2359082, 124.2669569],
                icon=folium.Icon(color='red',icon="hospital-o", prefix='fa'),
                tooltip='COTABATO SANITARIUM'
            ).add_to(m)

            folium.Marker(
                [8.001110, 125.171670], popup="ACCUSAFE DIAGNOSTIC LABORATORY", tooltip='ACCUSAFE DIAGNOSTIC LABORATORY'
            ).add_to(m)

            m
        

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
elif topic == 'Unsupervised Machine Learning':
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
    

