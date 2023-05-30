# Movie Recommendation Using Semantic Similarity
Using spaCy to determine similarities in movie descriptions in order to recommend the next movie to watch

## Installation & Usage
* Make sure to have Docker installed.
* Download and extract the files.
* Install all the dependencies in requirements.txt
* Create a build using the Dockerfile
* Run your build

If you wish to change the list of movies to recommend simply add it into the movies.txt file.  
The format for the file is:  
`Movie {Next letter in sequence} :{Movie Description}`

If you wish to change the previously watched movie to base your recommendation off of, then change the `movie_description` variable in the `watch_next.py` file on
line **42**