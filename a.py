import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Disable the warning about pyplot global use
st.set_page_config(page_title= 'IPL Analysis' , page_icon= ':cricket_bat_and_ball:' , layout= 'wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Your Streamlit app code follows below
# ...

# Load IPL data
@st.cache_data
# @st.set_option('deprecation.showPyplotGlobalUse', False)
def load_data():
    matches = pd.read_csv("matches.csv")
    deliveries = pd.read_csv("deliveries.csv")
    return matches, deliveries

matches, deliveries = load_data()

# Sidebar for user options
st.sidebar.header('Options')
analysis_choice = st.sidebar.selectbox('Choose analysis', ('Summary Statistics', 'Matches per Season', 'Top Run Scorers', 'Player of the Match', 'Toss Decision', 'Toss Winner', 'City'))

# Main content based on user selection
st.title('IPL Data Analysis')

if analysis_choice == 'Summary Statistics':
    st.subheader('Summary Statistics')
    st.write(matches.describe())

elif analysis_choice == 'Matches per Season':
    st.subheader('Matches per Season')
    plt.figure(figsize=(12,6))
    sns.countplot(x='Season', data=matches, order=matches['Season'].value_counts().index.sort_values())
    plt.title('Matches played per season')
    plt.xticks(rotation=45)
    st.pyplot()


elif analysis_choice == 'Top Run Scorers':
    st.subheader('Top Run Scorers')
    top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index()
    top_scorers = top_scorers.sort_values(by='batsman_runs', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='batsman_runs', y='batsman', data=top_scorers)
    plt.title('Top 10 run scorers')
    plt.xlabel('Total Runs')
    plt.ylabel('Batsman')
    st.pyplot()

elif analysis_choice == 'Player of the Match':
    st.subheader('Player of the Match')
    player_of_match = matches['player_of_match'].value_counts().head(10)
    st.write(player_of_match)

elif analysis_choice == 'Toss Decision':
    st.subheader('Toss Decision')
    toss_decision = matches['toss_decision'].value_counts()
    st.write(toss_decision)

elif analysis_choice == 'Toss Winner':
    st.subheader('Toss Winner')
    toss_winner = matches['toss_winner'].value_counts()
    st.write(toss_winner)

elif analysis_choice == 'City':
    st.subheader('Matches played in each city')
    city_matches = matches['city'].value_counts()
    st.write(city_matches)
