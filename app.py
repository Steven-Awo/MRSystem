import pickle

import streamlit as st

import requests

def fetching_poster(moviee_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(moviee_id)

    datta = requests.get(url)

    datta = datta.json()

    postter_path = datta['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + postter_path

    return full_path


def recomMovie(movie):
    indx = moviess[moviess['title'] == movie].index[0]

    distn = sorted(list(enumerate(similar[indx])), reverse=True, key= lambda r: r[1])

    name_of_movie_recommendation = []

    movie_recommended_poster = []

    for r in distn[1:31]:
        movie_id = moviess.iloc[r[0]]['movie_id']
        
        movie_recommended_poster.append(fetching_poster(movie_id))

        name_of_movie_recommendation.append(moviess.iloc[r[0]]['title'])

    return name_of_movie_recommendation, movie_recommended_poster        


st.header("Movie Recommendation System  Website using Machine Learning")

moviess = pickle.load(open('artificatss/movies_list.pkl', 'rb'))

similar = pickle.load(open('artificatss/similarity.pkl', 'rb'))

movie_lists = moviess['title'].values

the_selected_movies = st.selectbox(
    'Type or Select A Particular Movie to Get Some Recommendations', movie_lists)

if  st.button('Showing the Recommendation'):
    name_of_movie_recommendation,movie_recommended_poster = recomMovie(the_selected_movies)

    coln1, coln2, coln3, coln4, coln5 = st.columns(5)
    coln6, coln7, coln8, coln9, coln10 = st.columns(5)
    coln11, coln12, coln13, coln14, coln15 = st.columns(5)
    coln16, coln17, coln18, coln19, coln20 = st.columns(5)
    coln21, coln22, coln23, coln24, coln25 = st.columns(5)
    coln26, coln27, coln28, coln29, coln30 = st.columns(5)

    with coln1:
        st.text(name_of_movie_recommendation[0])
        st.image(movie_recommended_poster[0])
    with coln2:
        st.text(name_of_movie_recommendation[1])
        st.image(movie_recommended_poster[1])

    with coln3:
        st.text(name_of_movie_recommendation[2])
        st.image(movie_recommended_poster[2])
    with coln4:
        st.text(name_of_movie_recommendation[3])
        st.image(movie_recommended_poster[3])
    with coln5:
        st.text(name_of_movie_recommendation[4])
        st.image(movie_recommended_poster[4])
    with coln6:
        st.text(name_of_movie_recommendation[5])
        st.image(movie_recommended_poster[5])
    with coln7:
        st.text(name_of_movie_recommendation[6])
        st.image(movie_recommended_poster[6])
    with coln8:
        st.text(name_of_movie_recommendation[7])
        st.image(movie_recommended_poster[7])
    with coln9:
        st.text(name_of_movie_recommendation[8])
        st.image(movie_recommended_poster[8])
    with coln10:
        st.text(name_of_movie_recommendation[9])
        st.image(movie_recommended_poster[9])
    with coln11:
        st.text(name_of_movie_recommendation[10])
        st.image(movie_recommended_poster[10])
    with coln12:
        st.text(name_of_movie_recommendation[11])
        st.image(movie_recommended_poster[11])
    with coln13:
        st.text(name_of_movie_recommendation[12])
        st.image(movie_recommended_poster[12])
    with coln14:
        st.text(name_of_movie_recommendation[13])
        st.image(movie_recommended_poster[13])
    with coln15:
        st.text(name_of_movie_recommendation[14])
        st.image(movie_recommended_poster[14])
    with coln16:
        st.text(name_of_movie_recommendation[15])
        st.image(movie_recommended_poster[15])
    with coln17:
        st.text(name_of_movie_recommendation[16])
        st.image(movie_recommended_poster[16])
    with coln18:
        st.text(name_of_movie_recommendation[17])
        st.image(movie_recommended_poster[17])
    with coln19:
        st.text(name_of_movie_recommendation[18])
        st.image(movie_recommended_poster[18])
    with coln20:
        st.text(name_of_movie_recommendation[19])
        st.image(movie_recommended_poster[19])
    with coln21:
        st.text(name_of_movie_recommendation[20])
        st.image(movie_recommended_poster[20])
    with coln22:
        st.text(name_of_movie_recommendation[21])
        st.image(movie_recommended_poster[21])
    with coln23:
        st.text(name_of_movie_recommendation[22])
        st.image(movie_recommended_poster[22])
    with coln24:
        st.text(name_of_movie_recommendation[23])
        st.image(movie_recommended_poster[23])
    with coln25:
        st.text(name_of_movie_recommendation[24])
        st.image(movie_recommended_poster[24])
    with coln26:
        st.text(name_of_movie_recommendation[25])
        st.image(movie_recommended_poster[25])
    with coln27:
        st.text(name_of_movie_recommendation[26])
        st.image(movie_recommended_poster[26])
    with coln28:
        st.text(name_of_movie_recommendation[27])
        st.image(movie_recommended_poster[27])
    with coln29:
        st.text(name_of_movie_recommendation[28])
        st.image(movie_recommended_poster[28])
    with coln30:
        st.text(name_of_movie_recommendation[29])
        st.image(movie_recommended_poster[29])
    