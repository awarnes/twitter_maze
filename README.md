## A Twitter randomized maze:

The players are presented with a grid of letters with _only one acceptable way_ from start to finish: through the text of a randomly selected 'popular' tweet.

#### MVP
A playable game.

* The user will be scored on the number of moves it takes them to complete the maze (the minimum is the len(tweet)).


##### The program:
1. Scrapes twitter for the top trends in the USA at the moment.
* Chooses one trend at random.
* Selects a popular tweet from the random trend.
* Implants it in a grid (as the correct path through the maze).
    - We removed the direct Twitter link at the end.
* Randomly fills in the remainder of the grid to obfuscate the path.
* Allows the user to traverse the grid.
* Once completed, displays the tweet and author to the user, and the user's score.


##### Libraries Used:
Standard:
* Curses
 * For display and game play.
* Random
 * For maze generation.
* Pickle (Not implemented in current code)
* Math
* Re
 * For formatting tweet information.

Non-Standard:  
* Tweepy
 * Scraping Twitter


##### Future Possibilities:
* Export generated maze to PNG.
 * Using PIL
* Allow for offline play.
* Change difficulty to harvest from less popular tweets.
* Change 'popular' to mean most re-tweeted or most liked.
* Colorize the maze.
* Standalone executable for any file system.
* Web embedded application.


##### Playing the game:
1. You will need to have your own Twitter API Key, Token, and Secrets.
* In the retrieve_data.py edit the file to either point at your own secrets.py file or enter your API information manually.
* Run the curses_game.py from the console.
 * If the console is not the correct size, it will resize to fit the game.
 * However, this can impact the ability of curses to render properly.
  * See _Known Issues_ below.
* Start a New Game by pressing '1' or 'n'.
* Use either the num-pad or arrow keys to traverse the maze.
* You can start a new game at any time by pressing 'n' or quit by pressing 'q'.

##### Known Issues:
* Terminal resizing:
 * Was tested on MacOS 10.12.3
 * If the screen was not sized properly prior to running curses_game.py the game may not display properly.
 * To solve this, quit the program and run it again. 
