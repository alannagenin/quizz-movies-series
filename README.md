# [WIP] Movie and series quizz :movie_camera:

The aim of this project is to create a solo/multiplayer quizz about movies and series requesting the [The Movie Database](https://www.themoviedb.org/) API.

## Quick start

```bash
git clone git@github.com:alannagenin/quizz-movies-series.git
cd quizz-movies-series
pip3 install -r requirements.txt
```

### API Key

In order to use the quizz, you will need an API Key to access [The Movie Database](https://www.themoviedb.org/). To get a key, you must:
1. [Sign up](https://www.themoviedb.org/signup) and verify your account.
2. [Log into](https://www.themoviedb.org/login) your account.
3. Go to [Settings > API](https://www.themoviedb.org/settings/api) and copy you API Key generated.
 
Then you should create an `.env` file with the following information.

```python
DATABASE_URL = "https://api.themoviedb.org/3/"
API_KEY = <YOUR API KEY>
```

