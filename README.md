# [WIP] Movie and series quizz

The aim of this project is to do a quizz about movies and series requesting an API. Here, the API used is [The Movie DB](https://www.themoviedb.org/).


## Quick start

```python
git clone git@github.com:alannagenin/quizz-movies-series.git
cd quizz-movies-series
pip3 install -r requirements.txt
```

To use the app you must [create an account on the Movie DB](https://www.themoviedb.org/documentation/api) in order to use the API. Then you should create an `.env` file with the following information.

```python
DATABASE_URL = "https://api.themoviedb.org/3/"
API_KEY = <YOUR API KEY>
```