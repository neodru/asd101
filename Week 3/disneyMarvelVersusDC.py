#Storyline: Which movies belong to the Disney/Marvel Studios? Which movies belong to DC Studios? Which movies are Classics?

dc = ['Batman Begins', 'The Justice League','Constantine', 'Watchmen', 'Green Lantern', 'Man of Steel' , 'Suicide Squad', 'Wonder Woman', 'Shazam!', 'Aquaman']

disneyMarvel = ['Parenthood', 'Star Wars','Ironman', 'Avengers: Age of Ultron', 'Ant-Man', 'Captain America: First Avenger','Dr. Strange', 'Guardians of the Galaxy']

classicMovie = ['Shawshank Redemption', 'The Crucible', 'Matrix',]

movies = dc + disneyMarvel + classicMovie

def favoriteMovieEver():
    print("""From this list:
""")
    print(*movies, sep='\n')
    favoriteMovie = (input("""
What is your favorite movie? """ ))

    if favoriteMovie in dc:
        print("This is a DC Studios movie.")

    elif favoriteMovie in disneyMarvel:
        print("This is a Disney/Marvel movie.")

    elif  favoriteMovie in classicMovie:
        print("Looks like you've chos\n  an classic! ")

    else:
        favoriteMovie not in movies
        print(f"""{favoriteMovie} is not on the list. Please try again
""")
        return favoriteMovieEver()
    print
favoriteMovieEver()


 
