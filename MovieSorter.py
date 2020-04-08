movies = {
    2005 : list(["Munich", "Steven Spielberg"]),
    2006 : list([["The Prestige", "Christopher Nolan"],["The Departed", "Martin Scorsese"]]),
    2007 : list(["Into the Wild", "Sean Penn"]),
    2008 : list(["The Dark Knight", "Christopher Nolan"]),
    2009 : list(["Mary and Max", "Adam Elliot"]),
    2010 : list(["The King's Speech", "Tom Hooper"]),
    2011 : list([["The Artist", "Michel Hazanavicius"], ["The Help", "Tate Taylor"]]),
    2012 : list(["Argo", "Ben Affleck"]),
    2013 : list(["12 Years a Slave", "Steve McQueen"]),
    2014 : list(["Birdman", "Alejandro G. Inarritu"]),
    2015 : list(["Spotlight", "Tom McCarthy"]),
    2016 : list(["The BFG", "Steven Spielberg"]),
}
# Separator for reprinting titles.
comma = ", "

# Initial call for user input and year to show movies 
# associated with the year. Keeping it separate from
# the next section improves readability.
user_year = int(input("Enter a year between 2005 and 2016:\n"))
if user_year in movies:
    if isinstance(movies[user_year][0], list):
        for movie in movies[user_year]:
            print("%s, %s" % (movie[0], movie[1]))
    else:
        print("%s" % (comma.join(map(str,movies[user_year]))))
else:
    print("N/A")
    
# The monster menu problem starts - sorting and rearranging 
# the contents of the dictionary based on the user request.
# Here it requests the user's selection before getting into
# the meat of the problem.
print("\nMENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit\n")
user_option = input("Choose an option:\n")


while user_option != 'q':
    if user_option == 'y':
        # Fairly simple, remains the same as the first 'by year'
        # request, but prints all of them instead of only the
        # selected years. We don't have to change the data
        # structure we pull from for this.
        for year in movies:
            print("%s:" % year)
            if isinstance(movies[year][0], list):
                for movie in movies[year]:
                    print("\t%s, %s" % (movie[0], movie[1]))
            else:
                print("\t%s" % (comma.join(map(str,movies[year]))))
            print()
    elif user_option == 'd':
        # Setting the groundwork and building a new dictionary 
        # and lists from the existing movies. This uses existing
        # information consistently and keeps from inconsistencies
        # caused by typing out all the same information again. 
        # It only builds this new list if 'd' is selected, and 
        # doesn't run every time.
        director_movies = {}
        for year in movies:
            # Using the placement from the original list, we
            # are organizing the new information by iterating
            # through the existing list in order of how it 
            # appears. It checks if the value with the key is
            # a list first, then decides how to proceed in
            # organizing the information.
            if isinstance(movies[year][0], list):
                for movie in movies[year]:
                    if movie[1] in director_movies:
                        director_movies[movie[1]] = list([[movie[0], year],director_movies[movie[1]]])
                    else:
                        director_movies[movie[1]] = list([movie[0], year])
            else:
                if movies[year][1] in director_movies:
                    director_movies[movies[year][1]] = list([[movies[year][0], year], director_movies[movies[year][1]]])
                else:
                    director_movies[movies[year][1]] = list([movies[year][0], year])
        # Pulling and printing the information from the new list.
        # Sorting the director movies by keys instead of having to
        # type out and organize the new dictionary manually.
        # Because some of the information in the values is a list,
        # we have to have different methods for printing the information.
        for director in sorted(director_movies.keys()):
            print("%s:" % director)
            if isinstance(director_movies[director][0], list):
                for movie in sorted(director_movies[director]):
                    print("\t%s, %s" % (movie[0], movie[1]))
            else:
                print("\t%s" % (comma.join(map(str,director_movies[director]))))
            print()
    elif user_option == 't':
        # Setting the groundwork and building a new dictionary 
        # and list from the existing movies. This uses existing
        # information consistently and keeps from inconsistencies
        # or having to type out all the same information again. 
        # It only builds this new list if 't' is selected, and 
        # doesn't run every time.
        titled_movies = {}
        for year in movies:
            if isinstance(movies[year][0], list):
                for movie in movies[year]:
                    if movie[0] in titled_movies:
                        titled_movies[movie[0]] = list([[movie[1], year],titled_movies[movie[1]]])
                    else:
                        titled_movies[movie[0]] = list([movie[1], year])
            else:
                if movies[year][0] in titled_movies:
                    titled_movies[movies[year][0]] = list([[movies[year][1], year], titled_movies[movies[year][1]]])
                else:
                    titled_movies[movies[year][0]] = list([movies[year][1], year])
        # Pulling and printing the information from the new list.
        # Sorting the director movies by keys instead of having to
        # type out and organize the new dictionary manually.
        for title in sorted(titled_movies.keys()):
            print("%s:" % title)
            if isinstance(titled_movies[title][0], list):
                for movie in sorted(titled_movies[title]):
                    print("\t%s, %s" % (movie[0], movie[1]))
            else:
                print("\t%s" % (comma.join(map(str,titled_movies[title]))))
            print()
    else: 
        # If an invalid selection is made, this comes up.
        print("\nMENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit\n\n")
        user_option = input("Choose an option:\n")
    # This comes up after running the script so that the user
    # can select another option!
    print("MENU\nSort by:\ny - Year\nd - Director\nt - Movie title\nq - Quit\n")
    user_option = input("Choose an option:\n")
