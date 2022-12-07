from BusinessObject.Question.question_movie import QuestionMovie

class QuestionMoviePlot(QuestionMovie):
    '''
        A question about the name of a movie based on its plot.

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
            Date of release of the movie (yyyy format)
        self.spoken_languages : string
            Languages spoken in the movie
        self.plot : string
            Synopsis of the movie in one or few lines
    '''
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        super().__init__(movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot)
    
    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"Which movie best describes the description below?\nSynopsis: {self.plot}"

    def get_correct_answer(self):
        '''
            Returns the name of the movie.
        '''
        return self.movie_title

