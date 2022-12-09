from BusinessObject.Question.question_movie import QuestionMovie

class QuestionMovieReleaseDate(QuestionMovie):
    '''
        A question about the release date of a movie

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
            Synopsis of the movie in few lines
        self.type : string
            Type of the question
    '''
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        super().__init__(movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot)
        self.type = "movie release date"
    
    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"When was the film {self.movie_title} released?"
    
    def get_correct_answer(self):
        '''
            Returns the correct answer of the corresponding question.
        '''
        return self.release_date

