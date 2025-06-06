import streamlit as st
import requests
import pandas as pd
import numpy as np
import pickle


def fetch_poster(id):
    pass

def recommend(movie):
    m_index = movies[movies['title'] == movie].index[0]
    # m_index = m_index.iloc[0]  # Convert from Series to scalar
    # st.write(f"Movie index: {m_index}")

    # Get similarity scores for the selected movie
    # distance = similarity
    # Sort the scores in descending order (excluding the movie itself)
    m_list = sorted(list(enumerate(similarity[m_index])), reverse=True, key=lambda x: x[1])[1:6]
    # st.write(m_list)
    recommended_movies =[]
    for i in m_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]]['title'])
        # st.write(recommended_movies)
    return recommended_movies

movie_list = pickle.load(open("movies_recommendation_dict.pkl","rb"))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open("similarity.pkl","rb"))

st.write("Movie Recommendation System")

selected_movie = st.selectbox("Select you favorite movie",movies['title'].values)

if st.button("Recommended Movies"):
    recommended = recommend(selected_movie)
    for i in recommended:
        st.write(i)

