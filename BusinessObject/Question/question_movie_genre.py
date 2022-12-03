from question_movie import QuestionMovie

class QuestionMovieGenre(QuestionMovie):
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        super().__init__(movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot)
    
    def display_question(self):
        return f"What is the main genre of the movie {self.movie_title}?"

    def get_correct_answer(self):
        return self.genres_name[0]


if __name__ == "__main__":
    question = QuestionMovieGenre(
        movie_title='The Fifth Element',
        original_movie_title='The Fifth Element',
        budget = 90000000,
        genres_name = ['Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction'],
        release_date = 1997,
        spoken_languages = ['English', 'Swedish', 'German'],
        plot = 'In 2257, a taxi driver is unintentionally given the task of saving a young girl who is part of the key that will ensure the survival of humanity.'
    )
    print(question.display_question())
    print(question.get_correct_answer())