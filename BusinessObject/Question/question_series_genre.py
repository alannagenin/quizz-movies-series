from BusinessObject.Question.question_series import QuestionSeries

class QuestionSeriesGenre(QuestionSeries):
    def __init__(self, series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot):
        '''
        A question about the genre of a TV series based on its name.

        Parameters
        ----------
        self.series_title : string
            Title of the series
        self.original_series_title : string
            Title of the movie in its original language
        self.first_air_date : int
            Date of the first air date (yyyy format)
        self.last_air_date : int
            Date of the last air date (yyyy format)
        self.nb_episodes_per_season : list
            Number of episodes per season 
        self.nb_episodes_tot : int
            Total number of episodes
        self.nb_seasons : int
            Number of seasons
        self.tv_host : string
            Name of the TV host
        self.genres_name : list
            Genres of the TV series
        self.spoken_languages : string
            Languages spoken in the series
        self.plot : string
            Synopsis of the series in few lines
        self.type : string
            Type of the question
        '''
        super().__init__(series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot)
        self.type = "series number seasons"
    
    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"What is the main genre of the TV series {self.series_title}?"

    def get_correct_answer(self):
        '''
            Returns the first answer of the corresponding question.
        '''
        return self.genres_name[0]
    
    def get_all_correct_answer(self):
        '''
            Returns all the correct answers of the corresponding question.
        '''
        return self.genres_name