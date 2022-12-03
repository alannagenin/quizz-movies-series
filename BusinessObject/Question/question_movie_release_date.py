from question_movie import QuestionMovie

class QuestionMovieGenre(QuestionMovie):
    '''
    A question about the genre of a movie

    Attributes
    ----------
    self.movie_title : string
        Title of the movie
    self.original_movie_title : string
        Title of the movie in its original language
    self.budget : integer
        Budget of the movie
    self.genres_name : string
        Genres of the movie
    self.release_date : string
        Date of release of the movie (yyyy-mm-dd format)
    self.spoken_languages : string
        Languages spoken in the movie
    self.plot : string
        Synopsis of the movie in few lines
    '''
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        super().__init__(movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot)
    
    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"When was the film {self.movie_title} released?"
    
    def get_correct_answer(self):
        return self.release_date


if __name__ == "__main__":
    question = QuestionMovieGenre(
        movie_title='The Fifth Element',
        original_movie_title='The Fifth Element',
        budget = 90000000,
        genres_name = ['Adventure', 'Fantasy', 'Action', 'Thriller', 'Science Fiction'],
        release_date = '1997-05-02',
        spoken_languages = ['English', 'Swedish', 'German'],
        plot = 'In 2257, a taxi driver is unintentionally given the task of saving a young girl who is part of the key that will ensure the survival of humanity.'
    )
     
    print(question.display_question())
    print(question.release_date)
    print(type(question.release_date))