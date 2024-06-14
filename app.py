import streamlit as st
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎞️",
    layout="centered",
    initial_sidebar_state="expanded"

)

movie_list = pickle.load(open('movie_list.pkl', 'rb'))
movie_title_list = movie_list['title'].values

similarity_vector = pickle.load(open('similarity.pkl', 'rb'))

st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>By Fatima Amani</h5>", unsafe_allow_html=True)
st.write("")
st.write("")


def get_poster_path(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}")
    poster_path = response.json()['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity_vector[movie_index]
    recommendation_list_id = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommendation_list = []
    poster_path = []

    for i in recommendation_list_id:
        recommendation_list.append(movie_list.iloc[i[0]].title)
        movie_id = movie_list.iloc[i[0]].movie_id
        poster_path.append(get_poster_path(movie_id))

    return recommendation_list, poster_path


st.markdown("<h3>Select your favourite movie from the dropdown menu </h3>", unsafe_allow_html=True)

selected_movie = st.selectbox("", movie_title_list)
st.write("")

if st.button("Get similar Recommendations"):
    recommend_movie_list, posters = recommend(selected_movie)

    col1, col2, col3, = st.columns(3)

    with col1:
        st.subheader(recommend_movie_list[0])
        st.image(posters[0])

    with col2:
        st.subheader(recommend_movie_list[1])
        st.image(posters[1])

    with col3:
        st.subheader(recommend_movie_list[2])
        st.image(posters[2])

    st.write("")
    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader(recommend_movie_list[3])
        st.image(posters[3])

    with col5:
        st.subheader(recommend_movie_list[4])
        st.image(posters[4])

    with col6:
        st.subheader(recommend_movie_list[5])
        st.image(posters[5])

    st.divider()

st.write("Created with ❤️ by Fatima")
