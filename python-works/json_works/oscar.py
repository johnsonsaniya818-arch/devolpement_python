from json import load

file_path="python-works\json_works\oscar-best-picture-award-winners.json"

fr=open(file_path,"r")

data=load(fr)

#print(len(data))

# Q1. Create a new list that contains only the movie titles from the dataset.

movies=[r.get("name") for r in data ]

#print(movies)

# Q2. Create a list that contains the movie title and release year for each Oscar-winning film.

oscar={r.get("name"):r.get("released_year")for r in data if r.get("oscar")==2010}

#print(oscar)

# Q3. Get all movies that were released before the year 2000.

year = [r.get("name") for r in data if r.get("released_year") < 2000]

#print(year)

# Q4. Find all movies whose runtime is greater than 150 minutes.

running_time=[r.get("name")for r in data if r.get("duration")>"150"]

#print(running_time)

# Q5. Create a list of movies where the director name starts with the letter “S”.

directors=[r.get("name")for r in data if r.get("directors").startswith("S")]

#print(directors)
# Q6. Count the total number of Oscar-winning movies in the dataset.

# Q7. Calculate the average runtime of all Oscar Best Picture winners.
# Q8. Create a dictionary that shows the number of movies won per decade
# (example: 1990s, 2000s, 2010s).
# Q9. Find the earliest released movie in the dataset.
# Q10. Check whether any movie in the dataset has a runtime less than 90 minutes.
# Q11. Check whether all movies in the dataset have a valid release year (greater than 1900).
# Q12. Find all movies that were released after 2015 and won the Oscar.
# Q13. Create a list of unique directors from the dataset.
# Q14. Check whether any director has won the Oscar more than once.
# Q15. Verify whether all movies in the dataset contain both director and runtime information.