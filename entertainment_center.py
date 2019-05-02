import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy",
            "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
            "https://www.youtube.com/watch?v=wmiIUN-7qhE")


school_of_rock = media.Movie("School of Rock",
                "Using rock music to learn",
                "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                    "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story, school_of_rock, hunger_games]
fresh_tomatoes.open_movies_page(movies)
