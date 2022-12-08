from BusinessObject.Question.question_series import QuestionSeries

class QuestionSeriesPlot(QuestionSeries):
    def __init__(self, series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot):
        super().__init__(series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot)
        self.type = "series plot"
    
    def display_question(self):
        return f"Which series best describes the description below?\nSynopsis: {self.plot}"

    def get_correct_answer(self):
        return self.series_title