fMovieTitle = "The Matrix"
fMovieYear= 1999
fMovieDescription = '''In dystopian future, humanity is unknowingly trapped inside a simulated reality known as,
the Matrix. The Matrix is created by intelligent machines to distract humans while they use their bodies as a source of energy.
A computer programmer by the handler "Neo", uncovers the truth and joins a rebellion against the machines. 
Traversing from the Matrix and reality to defeat the machines.'''

print("Welcome! I'm Dru, your new virtual assistant. I will ask you some questions so we can get to know each other.")
print("Ready? (Press 'Enter' when ready)")
enter = input("")
name = input("What's your name?")
print("Hello " + name +".")
userFavMovieTitle = input("What's your favorite movie?")
print(userFavMovieTitle + "? Never heard of it.")
userFavMovieYear = input("What year was it released?")
print(userFavMovieYear + "...Hmmm... still no clue.")                         
userMovieDescription = input("Can you describe the movie for me?")
print(f"""Thanks! I'll remember that {name}'s favorite movie is {userFavMovieTitle}({userFavMovieYear})
and is about: {userMovieDescription}""")
print("""
Ready to hear mine?
(Press 'Enter' when ready)""")

enter =input("")
                         
print(f"""My favorite movie is {fMovieTitle} ({fMovieYear}). It is about: {fMovieDescription}""")
adj1 = input ("Enter an adjective: ")



