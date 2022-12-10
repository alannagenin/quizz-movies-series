from BusinessObject.Question.question_series import QuestionSeries


class QuestionSeriesPlot(QuestionSeries):
    def __init__(
                self, series_title, original_series_title, first_air_date,
                last_air_date, nb_episodes_per_season, nb_episodes_tot,
                nb_seasons, tv_host, genres_name, spoken_languages, plot):
        '''
        A question about the name of a TV series based on its plot.

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
        self.type_question : string
            Type of the question
        '''
        super().__init__(
            series_title, original_series_title, first_air_date,
            last_air_date, nb_episodes_per_season, nb_episodes_tot,
            nb_seasons, tv_host, genres_name, spoken_languages,
            plot
        )
        self.type_question = "series plot"

    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"Which series best describes the description below?"\
            f"\nSynopsis: {self.plot}"

    def get_correct_answer(self):
        '''
            Returns the correct answer of the corresponding question.
        '''
        return self.series_title
