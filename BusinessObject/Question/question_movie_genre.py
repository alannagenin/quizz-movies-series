from BusinessObject.Question.question_movie import QuestionMovie

class QuestionMovieGenre(QuestionMovie):
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        super().__init__(movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot)
    
    def display_question(self):
        return f"What is the main genre of the movie {self.movie_title}?"

    def get_correct_answer(self):
        return self.genres_name[0]
    
    def get_all_correct_answer(self):
        return self.genres_name

