import spacy

#Loading the language library
nlp = spacy.load("en_core_web_md")

#Create the function to return similar movies
def recommend_movie(previous_movie_desc : str):

    #Create an nlp doc from the previous_movie_desc
    previous_doc = nlp(previous_movie_desc)

    #Load the lines from the movies.txt file
    with open("movies.txt", "r") as f:
        movies = f.readlines()

    #create a difference between the movie title and description
    movies_data = {}
    for movie in movies:
        #Get the title from indexing and make that the key with the description as the value
        movies_data[movie[0:7]] = movie[9::]

    #Create a tuple to house the movie title with the highest similarity to the previous movie description
    suggested_movie = ("temp", 0.0)
    
    #Loop over every movie in the dict and check its descriptions similarity
    for movie_title in movies_data.keys():
        #Create a doc for the current movie's description
        current_doc = nlp(movies_data[movie_title])
        #Get the similarity between the previous movie's description and the current one's
        similarity = previous_doc.similarity(current_doc)
        #Check if the similarity is greater than the description from the previous loop
        if suggested_movie[1] < similarity:
            suggested_movie = (movie_title, similarity)
        
        #Uncomment to see the results
        # print(f"('{movie_title}', {similarity})")
        # print(suggested_movie)
    
    #Return the movie with the best match
    return suggested_movie[0]

movie_description = "Will he save their world or destroy it?" \
" When the Hulk becomes too dangerous for the Earth, the Illuminati" \
" trick Hulk into a shuttle and launch him into space to a planet where" \
" the Hulk can live in peace. Unfortunately, Hulk land on the planet" \
" Sakaar where he is sold into slavery and trained as a gladiator."

#Print the return of the movie recommendation
print(recommend_movie(movie_description))