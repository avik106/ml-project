import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown
if not os.path.exists("similar.pkl"):
    url = 'https://drive.google.com/uc?id=1c28TQ2BSEzYw4YliU1w0D5LUgjAZlUIv'
    gdown.download(url, 'similar.pkl', quiet=False)

similarity = pickle.load(open('similar.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e7699b733c8aeeb32392bebf0c0f416a&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]
    recommended_movie_posters=[]
    for i in movie_list:
       movie_id=movies.iloc[i[0]].movie_id
       recommended_movie.append(movies.iloc[i[0]].title)
       recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters
    
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommender System')
select_movie=st.selectbox('Select your Favourite Movie',movies['title'].values)
if st.button('Recommend'):
    title,posters=recommend(select_movie)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(title[0])
        st.image(posters[0])
    with col2:
        st.text(title[1])
        st.image(posters[1])
    with col3:
        st.text(title[2])
        st.image(posters[2])
    with col4:
        st.text(title[3])
        st.image(posters[3])
    with col5:
        st.text(title[4])
        st.image(posters[4])