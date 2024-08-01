import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Simple Dashboard", layout="wide")

# Load external CSS file
def load_css(file_path):
    with open(file_path, "r") as file:
        css = file.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css("s1.css")
# Load Data file
df = pd.read_csv('student-scores.csv')
# Sidebar
st.sidebar.title("Dashboard Sidebar")
cities = df['city'].unique()
selected_city = st.sidebar.selectbox('Select City', options=['All Cities'] + list(cities))

# Find Pecentage and Total of each student for seven subjects
df['Total'] = df['math_score'] + df['history_score'] + df['physics_score'] + df['chemistry_score'] + df['biology_score'] + df['english_score'] + df['geography_score']
df['Percentage'] = df['Total'] / 7
df['Percentage'] = df['Percentage'].round(2) # Round to 2 decimal places

# Filter the DataFrame based on selected city
if selected_city != 'All Cities':
    df_filtered = df[df['city'] == selected_city]
else:
    df_filtered = df


# Find total number of students in the filtered DataFrame
total_students = len(df_filtered)

# Total number of male and female students in the filtered DataFrame
male_count = df_filtered['gender'].value_counts().get('male', 0)
female_count = df_filtered['gender'].value_counts().get('female', 0)

# Highest total and highest percentage
highest_total = df_filtered['Total'].max()
highest_percentage = df_filtered['Percentage'].max()

# Subject Wise Highest Score
math_highest_score = df_filtered['math_score'].max()
history_highest_score = df_filtered['history_score'].max()
physics_highest_score = df_filtered['physics_score'].max()
chemistry_highest_score = df_filtered['chemistry_score'].max()
biology_highest_score = df_filtered['biology_score'].max()
english_highest_score = df_filtered['english_score'].max()
geography_highest_score = df_filtered['geography_score'].max()

# Aggregate Values 


math_highest_score = df_filtered['math_score'].max()
history_highest_score = df_filtered['history_score'].max()
physics_highest_score = df_filtered['physics_score'].max()
chemistry_highest_score = df_filtered['chemistry_score'].max()
biology_highest_score = df_filtered['biology_score'].max()
english_highest_score = df_filtered['english_score'].max()
geography_highest_score = df_filtered['geography_score'].max()

st.markdown(f"""
    <h1>Students Performance Dashboard</h1>
    <p>Aggregate counts:</p>
    <div class="card-container">
        <div class="card">Total Students  {total_students}</div>
        <div class="card">Male Students<br>{male_count}</div>
        <div class="card">Female Students<br>{female_count}</div>
        <div class="card">Highest Total<br>{highest_total}</div>
        <div class="card">Highest Pecentage<br>{highest_percentage}</div>
    </div>
    </div>
""", unsafe_allow_html=True)


st.markdown(f"""
    <div class="main-content">
    <p>Subject Wise Highest Score</p>
    <div class="card2ndrow-container">
        <div class="card2ndrow">Math<br>{math_highest_score}</div>
        <div class="card2ndrow">History<br>{history_highest_score}</div>
        <div class="card2ndrow">Physics<br>{physics_highest_score}</div>
        <div class="card2ndrow">chemistry<br>{chemistry_highest_score}</div>
        <div class="card2ndrow">Biology<br>{biology_highest_score}</div>
        <div class="card2ndrow">English<br>{english_highest_score}</div>
        <div class="card2ndrow">Geography<br>{geography_highest_score}</div>
    </div>
    </div>
""", unsafe_allow_html=True)

# Graph Section 

# Calculate the average score for each subject
average_scores = df_filtered[['math_score', 'history_score', 'physics_score', 'chemistry_score', 'biology_score', 'english_score', 'geography_score']].mean()

col1 , col2  = st.columns(2)

with col1:
    fig, ax = plt.subplots()  # No size specified
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']
    # Plotting the bar chart
    ax.bar(average_scores.index, average_scores.values, color=colors)
    # Set axis labels with bold font
    ax.set_xlabel('Subjects', fontweight='bold')
    ax.set_ylabel('Average Score', fontweight='bold')
    # Set title with bold font
    ax.set_title('Average Score by Subject', fontweight='bold')

    # Rotate x-axis labels for better readability
    ax.set_xticklabels(average_scores.keys(), rotation=45, ha='right')

    # Adding border to the chart area
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(2)

    # Display the bar chart in Streamlit
    st.pyplot(fig)

with col2:
    subject_columns = ['math_score', 'history_score', 'physics_score', 'chemistry_score', 'biology_score', 'english_score', 'geography_score']
    avg_scores_by_gender = df_filtered.groupby('gender')[subject_columns].mean()

    # Create grouped bar chart using Matplotlib
    fig, ax = plt.subplots()  # No size specified

    # Define the bar width and positions
    bar_width = 0.35
    index = np.arange(len(subject_columns))

    # Plot bars for each gender
    bar1 = ax.bar(index, avg_scores_by_gender.loc['male'], bar_width, label='Male', color='blue')
    bar2 = ax.bar(index + bar_width, avg_scores_by_gender.loc['female'], bar_width, label='Female', color='orange')

    # Add labels, title, and legend
    ax.set_xlabel('Subject',fontweight='bold')
    ax.set_ylabel('Average Score',fontweight='bold')
    ax.set_title('Gender-wise Average Scores by Subject', fontweight='bold')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(subject_columns, rotation=45, ha='right')
    
    # Adjust the legend position
    ax.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))


        # Adding border to the chart area
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(2)
    # Display the plot in Streamlit
    st.pyplot(fig)


col1 , col2 , col3 = st.columns(3)
with col1:
    # Define colors for each pie slice
    colors = ['lightblue', 'lightgreen']
    # Calculate percentages
    part_time_job_counts = df_filtered['part_time_job'].value_counts()
    part_time_job_percentages = (part_time_job_counts / part_time_job_counts.sum()) * 100

    # Create a Plotly figure
    fig = go.Figure(data=[go.Pie(labels=part_time_job_percentages.index, values=part_time_job_percentages.values, textinfo='label+percent', pull=[0, 0.1],marker=dict(colors=colors))])
    fig.update_layout(title_text='Percentage of Students with and Without Part-Time Jobs')

    # Display the figure in Streamlit
    st.plotly_chart(fig)

with col2:
    fig = px.histogram(df_filtered, x='weekly_self_study_hours', nbins=10, title='Distribution of Weekly Self-Study Hours')

    # Customize the layout
    fig.update_layout(
        xaxis_title='Weekly Self-Study Hours',
        yaxis_title='Number of Students',
        bargap=0.2,
        template='simple_white'
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig)

with col3:
    # Top 5 student
    top_5_students = df_filtered.nlargest(5, 'Percentage')[['id','first_name', 'Total', 'Percentage']]

    # Display the table using st.markdown with unsafe_allow_html=True
    fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(top_5_students.columns),
        fill_color='paleturquoise',
        align='center'
    ),
    cells=dict(
        values=[top_5_students[col] for col in top_5_students.columns],
        fill_color='lavender',
        align='left'
    )
    )])

    # Set height of the table
    fig.update_layout(height=500,width=300,title=dict(
        text="Top 5 Students by Percentage",
        font=dict(size=20, color="black"),
        x=0.5,
        xanchor="center",
        yanchor="top"
    ))

    # Display Plotly table in Streamlit
    st.plotly_chart(fig)



# Plot career aspiration counts
career_aspiration_counts = df_filtered['career_aspiration'].value_counts()

fig, ax = plt.subplots()  # No size specified
bar_width = 0.35
career_aspiration_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Proportion of Students by Career Aspiration')
ax.set_xlabel('Career Aspiration')
ax.set_ylabel('Number of Students')
ax.set_xticklabels(career_aspiration_counts.index, rotation=45, ha='right')
ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Display the career aspiration bar chart in Streamlit
st.pyplot(fig)
