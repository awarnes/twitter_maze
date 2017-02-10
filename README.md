## A Twitter randomized maze:

The players are presented with a grid of letters with _only one acceptable way_ from start to finish: through the text of a randomly selected 'popular' tweet.

#### MVP
A playable game.

##### The program will:
1. Scrape twitter for the top 5-10 most popular tweets at the moment.
* Choose one at random.
* Implant it in a grid (as the correct path through the maze).
    - Will remove user tags, but keep hashtags
* Randomly fill in the remainder of the grid to obfuscate the path.
* Allow the user to traverse the grid.
* The user will be scored on the number of moves it takes them to complete the maze (minimum is the len(tweet)).
* Once completed, displays the tweet and author to the user, and the user's score.

##### Libraries Used:
* Tweepy
* PIL

##### Structure needed:
* Back-end to scrape twitter, scrub text into readable format, return text for the maze generator.
* Back-end for the maze generator that takes the given tweet.
* Back-end to move the character around the maze and score their progress.
* Front-end to display the maze and 'character' moving around it.
* Front-end to display menus for working through the program.

##### Possible Bonus Options:
* Export generated maze to PNG.
* Change difficulty to harvest from less popular tweets.
* Change 'popular' to mean most re-tweeted or most liked.
* Colorize the maze.
* Standalone executable for any file system.
* Web embedded application.
