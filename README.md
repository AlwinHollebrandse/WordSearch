# WordSearch
a 2D and 3D word search solver and generator 

# 2D Word Search Solver Algorithm
The basic idea is to loop through the word search and at each position check if the value at the current word search location matches the first letter of any word in the word list. If it does, then check every direction to see if a word can be found. If it was found, print the location and the direction. 

# 2D Word Search Generator Algorithm
First the height and width dimensions of the word search need to be determined so that it can be guaranteed that there is space in the blank word search for every word. This was done by determining the maximum length of the longest word in the word list and by finding the nearest square value that was larger than or equal to the total number of characters in the word list. The minimum height and width were then the maximum of those two values, plus one (the one was added to increase the likelihood that an attempt of filling out the word search would work). The longest word length had to be found so that there would be room for the longest word in the word list (For instances where word list held any word as a word search requires that each word only goes in one continuous direction. I was not developing a “Boggle” simulator), while the square was found to ensure that each word would fit (for instances where the word list was very numerous) as every character was accounted for. For variety, the word search would be created with a random number between these minimum values and that number multiplied by a multiplier value that the user could change if they wanted to. A higher value equates to a larger word search which would be more difficult.

After this, the generator would pick a random untried and available word search index value and then randomly shuffle a list of directions and the remaining words. It would then try each direction with each word until one worked. If none did, then said position would be removed as a candidate. If a word worked, it would be added to the word search in the matched direction. This word would then be removed from word list while the word, direction, and position would be printed out. This process gets repeated until either all words were added, or all positions were tried.

If the word list still has words in it (because they cannot fit anywhere in the current created word search) then the whole process repeats with the same size word search. Because of the predetermined minimum word search dimensions, this algorithm will work eventually and terminate.
	
# 3D Word Search Solver and Generator Algorithm
This works the same the 2D version, just with an extra dimension.

# Developer’s Note
This project was inspired by my dislike of solving word searches. The task seemed so tedious that I knew it was something a computer was meant to do. Initially I just created the 2D word search solver. After completing this, I realized that I did not want to write my own word searches to test my solver with. This led me to designing the 2D world search generator. Upon completing this, I wondered if I could create 3D versions. It turns out that I could, but it was more difficult than I anticipated. Because the project seemed small and simple to me when I started it, I did not create it on Github. As the scope ramped up it became apparent that I should have used Github. Hence the large initial commit.
Because this project was a way for me to learn python, there were a few design things I would change. I should have used numpy arrays instead of lists. While I was developing this, I assumed that lists worked like arrays because of the ‘[]’s. My java background betrayed me. I learned the hard way that the reading order is the opposite of what I expected. As in a python list with the indexes of [1][2][3] will check the depth 1, the hweight2, and the width 3 as opposed to my expected array reading of width 1, height 2, and depth 3. At least the numerous and seemingly impossible “list out of bounds” errors taught me well. 

# Local Usage
Install the components needed to use a virtual shell
In one terminal, enter the needed shell. Ex: 'pipenv shell'
In that same terminal, run the bootstrap file. './bootstrap.sh'
In an other terminal hit the endpoint you want. Ex: 'curl http://localhost:5000/solveWordSearch'