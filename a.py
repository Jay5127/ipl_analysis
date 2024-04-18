import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_lottie import st_lottie
import requests


# Disable the warning about pyplot global use
st.set_page_config(page_title= 'IPL Analysis' , page_icon= ':cricket_bat_and_ball:' , layout= 'wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Your Streamlit app code follows below
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


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

stats = load_lottie_url('https://lottie.host/85d74037-d38c-4f12-82c1-ec955d754b43/DQQsI1vUWr.json')
season = load_lottie_url('https://lottie.host/8d4d4a8b-4265-46c2-8f59-596724ae56bc/ICT3anM3Gx.json')
runs = load_lottie_url('https://lottie.host/56d625e5-15fc-42f9-a8ba-a67b1d71c5f4/Q4CQstbzXP.json')
player = load_lottie_url('https://lottie.host/d3931ee1-daf2-4426-87db-7ba809227460/l2Pkw05Ciz.json')
toss = load_lottie_url('https://lottie.host/db161f6f-8995-41ac-a26e-4bc858af552d/siAMtHyFhj.json')
venue = load_lottie_url('https://lottie.host/ee512b8c-c8bb-4a54-ba71-9e2037e92b82/URKUG4oW3k.json')
# Main content based on user selection
st.title('IPL Data Analysis')

if analysis_choice == 'Summary Statistics':
    st.subheader('Summary Statistics')
    st_lottie(stats , height= 200)
    st.write(matches.describe())
    

elif analysis_choice == 'Matches per Season':
    st.subheader('Matches per Season')
    st_lottie(season ,height=200)
    plt.figure(figsize=(12,6))
    sns.countplot(x='Season', data=matches, order=matches['Season'].value_counts().index.sort_values())
    plt.title('Matches played per season')
    plt.xticks(rotation=45)
    st.pyplot()


elif analysis_choice == 'Top Run Scorers':
    st.subheader('Top Run Scorers')
    st_lottie(runs , height= 200)
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
    st_lottie(player , height= 200)
    player_of_match = matches['Man of the Match'].value_counts().head(10)
    st.write(player_of_match)

elif analysis_choice == 'Toss Decision':
    st.subheader('Toss Decision')
    toss_decision = matches['Toss Decision'].value_counts()
    st.write(toss_decision)

elif analysis_choice == 'Toss Winner':
    st.subheader('Toss Winner')
    st_lottie(toss , height= 200)
    toss_winner = matches['Toss Winner'].value_counts()
    st.write(toss_winner)

elif analysis_choice == 'City':
    st.subheader('Matches played in each city')
    st_lottie(venue , height= 200)
    city_matches = matches['City'].value_counts()
    st.write(city_matches)




# if analysis_choice == 'Summary Statistics':
#     st_lottie(stats , height= 600)
