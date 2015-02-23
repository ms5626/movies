#imports:
import fresh_tomatoes
import media

#instances of movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                        "A marine on an alien planet.",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn.",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                        "A rat is a chef in Paris.",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                        "Going back in time to meet authors.",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                        "A really real reality show.",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63a7H0bo")
prisoners = media.Movie("Prisoners",
                        "Boston father crosses the line in a crime thriller.",
                        "http://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg",
                        "https://www.youtube.com/watch?v=sfRckdHq--c")
fifty_shades = media.Movie("Fifty Shades of Grey",
                        "Adaptaion of a novel by the same name.",
                        "http://upload.wikimedia.org/wikipedia/en/5/5e/50ShadesofGreyCoverArt.jpg",
                        "https://www.youtube.com/watch?v=CQERFnGvi_A")
there_is_mary = media.Movie("There's Something About Mary",
                        "An outrageous battle for Mary's affections.",
                        "http://upload.wikimedia.org/wikipedia/en/d/df/There%27s_Something_About_Mary_POSTER.jpg",
                        "https://www.youtube.com/watch?v=uYFwrK8qCOk")

#movies array include all of the movies to be displayed on the Fresh Tomatoes Website
movies = [fifty_shades,prisoners,hunger_games, toy_story, avatar, school_of_rock, ratatouille,  midnight_in_paris, there_is_mary ]

#function call to open_movies_page method sending the movies array as input parameter
fresh_tomatoes.open_movies_page(movies)

