# Welcome to my project!

Hi! This is a project that analyzes and manages in a database via a CLI. Please enjoy!


# Install Requirements

 - Install [PostgreSQL](https://www.postgresql.org/).
 - Install latest version of [Python](https://www.python.org/). The CLI was developed in Python 3.9.
	 - If not already installed with Python,  please install Python package manager [PIP](https://pip.pypa.io/en/stable/installation/).
- Once these are installed, you'll need to install the necessary python libraries:
	- psycopg2: `pip install psycopg2`
	- prettytable: `pip install prettytable`

# Setup



## Understanding the File Structure

 - File directory:
	 - \CLI
		 - CLI. py
	- \Database
		- video_games_db.sql
	- \Manual_Setup
		- commands_to_setup_db.sql
		- \Dataset
			- Genre.csv
			- Publisher.csv
			- Developer.csv
			- Users.csv
			- Console_Generation.csv
			- Rating_Orgs.csv
			- Rating.csv
			- Platform.csv
			- Game.csv
			- Game_Developers.csv
			- Review.csv
			- Public_Reception.csv
			- Sales.csv	

## ERD (15 relations):
- ![image](/photos/ERD_Final.png)
## Setup the database

There are two options to get started with the database:
### Importing the database (Easiest
 1. Create a new database in PostgreSQL using either the command line or pgAdmin4
 2. Restore the new database with the file **video_games_db.sql**. Refer to the [pgAdmin4 documentation.](https://www.pgadmin.org/docs/pgadmin4/latest/restore_dialog.html) or [PostgreSQL documentation](https://www.postgresql.org/docs/8.0/backup.html#BACKUP-DUMP-RESTORE) for help restoring the database.
 3. Troubleshooting: It's possible that after restoring a database, the serial primary keys might need to be reset to their maximum value to allow the next added item to be set to the correct id. This can be fixed by running the following SQL commands (also found at the bottom of **commands_to_setup_db.sql**.

    ```SELECT setval('public.genres_genreid_seq', (SELECT  MAX(genreid) FROM public.genres) +  1);
    SELECT setval('public.publishers_publisherid_seq', (SELECT  MAX(publisherid) FROM public.publishers) +  1);
    SELECT setval('public.developers_developerid_seq', (SELECT  MAX(developerid) FROM public.developers) +  1);
    SELECT setval('public.regions_regionid_seq', (SELECT  MAX(regionid) FROM public.regions) +  1);
    SELECT setval('public.users_userid_seq', (SELECT  MAX(userid) FROM public.users) +  1);
    SELECT setval('public.console_generations_generationid_seq', (SELECT  MAX(generationid) FROM public.console_generations) +  1);
    SELECT setval('public.platforms_platformid_seq', (SELECT  MAX(platformid) FROM public.platforms) +  1);
    SELECT setval('public.games_gameid_seq', (SELECT  MAX(gameid) FROM public.games) +  1);
    SELECT setval('public.reviews_reviewid_seq', (SELECT  MAX(reviewid) FROM public.reviews) +  1);




### Manual setup from dataset (Hardest):

 1. Navigate to the **commands_to_setup_db.sql** file under the \Manual_Setup folder
 2. Execute the `CREATE TABLE` statements found inside the file
 3. Replace the correct path to the corresponding dataset file which are all found inside   \Manual_Setup\Dataset.
for example: the command `\copy Game_Developers FROM  '[INSERT PATH]\Game_Developers.csv'  WITH (FORMAT csv, HEADER true);` requires the correct path to function. In my local computer I have this command set like this `\copy Game_Developers FROM 'C:\Project\Manual_Setup\Dataset\Game_Developers.csv'  WITH (FORMAT csv, HEADER true);`
4. Execute the updated `\copy` commands to insert all the data from the dataset
5. **CRITICAL Before moving on to the CLI:** After all data is imported, ensure to run the `SELECT setval` commands to sync SERIAL primary keys properly.

    ```SELECT setval('public.genres_genreid_seq', (SELECT  MAX(genreid) FROM public.genres) +  1);
    SELECT setval('public.publishers_publisherid_seq', (SELECT  MAX(publisherid) FROM public.publishers) +  1);
    SELECT setval('public.developers_developerid_seq', (SELECT  MAX(developerid) FROM public.developers) +  1);
    SELECT setval('public.regions_regionid_seq', (SELECT  MAX(regionid) FROM public.regions) +  1);
    SELECT setval('public.users_userid_seq', (SELECT  MAX(userid) FROM public.users) +  1);
    SELECT setval('public.console_generations_generationid_seq', (SELECT  MAX(generationid) FROM public.console_generations) +  1);
    SELECT setval('public.platforms_platformid_seq', (SELECT  MAX(platformid) FROM public.platforms) +  1);
    SELECT setval('public.games_gameid_seq', (SELECT  MAX(gameid) FROM public.games) +  1);
    SELECT setval('public.reviews_reviewid_seq', (SELECT  MAX(reviewid) FROM public.reviews) +  1);

6. Test that all the data has been inserted correctly by Executing the `SELECT` commands.


## Setup the CLI

Edit **`CLI.py`**with the login details to the database.

    # ----------Database Config----------
    
    DATABASE  =  {
    
    'dbname':  'video_games_db', #Replace with name of your databsae
    
    'user':  'postgres', #postgres is default, replace if needed
    
    'password':  'PASSWORD', #Replace with password to your database
    
    'host':  'localhost', #Replace if not running locally
    
    'port':  '5432' #Update port. I use 5432 as my local default.
    
    }





# Guide to using the CLI
**This is guide to the CLI, if you are intrested in examples of queries being executed that is located at the bottom of the page**

## Main menu Overview 
Each option in the main menu will have a corresponding section in this guide:


    Main Menu:
    1. View Data
    2. User Management
    3. Game Management
    4. Review Management
    5. Sales Data
    6. Rating Information
    7. Analytics and Reports
    8. Search
    9. Developer and Publisher Relations
    10. Exit

##  1. View Data Overview 

Description: Explore and query various categories of data within the database such as viewing lists of genres, publishers, developers, and more.
Below is a Tree Style breakdown of each View Data Menu including each Sub Menu with its own controls and prompt inputs.

    View Data Menu:
    1. Genres
    2. Publishers
    3. Developers
    4. Platforms
		Platforms Sub Menu:
				    1. View all platforms
				    2. Filter by generation
						    prompt: Enter generation ID:
				    3. Back to View Data Menu
    5. Console Generations
    6. Games
	    Games Sub Menu:
		    1. View all games
					View all games Sub Menu:
						There are currently {GAME_NUM} games in the DB
						1. Load all {GAME_NUM} games
						2. View in pages of 1000
							View in pages of 1000 Sub Menu: (this shows as you iterate through the games)
								1. Show next 1000 Games
								2. Exit
						3. Back to View Games Menu
		    2. Filter by attributes
			    Filter by attributes Sub Menu:
				    Enter filter criteria:
				    Genre ID (leave blank if no filter):
				    Publisher ID (leave blank if no filter):
				    Year (leave blank if no filter):
    7. Back to View Data Menu
    8. Reviews
	    Review Sub Menu:
		    Enter Game ID to filter by (leave blank for no filter):
    9. Regions
    10. Back to Main Menu

##  2. User Management

Mange user data such as creating new users, updating existing users in the db and deleting users.

    User Management Menu:
    1. Create User
	    Create User Sub Menu:
		    Enter user name:
		    Enter region ID: 
    2. Update User Info
	    Update User Info Sub Menu:
		    Enter user ID to update:
		    Enter new name (leave blank to keep current):
		    Enter new region ID (leave blank to keep current):
    3. Delete User
		Delete User Sub Menu:
			Enter user ID to delete:
    4. Back to Main Menu
   

## 3. Game Management

Add new games, modify existing games, or delete games.
Game Management Menu:

    1. Add New Game
	    Add New Game Sub Menu:
		    Enter game name:
		    Enter game year:
		    Enter genre ID:
		    Enter publisher ID:
    2. Update Game Info
	    Update Game Info Sub Menu:
		    Enter game ID to update:
		    Enter new name (leave blank to keep current):
		    Enter new year (leave blank to keep current):
		    Enter new genre ID (leave blank to keep current):
		    Enter new publisher ID (leave blank to keep current):
		    Enter new rating ID (leave blank to keep current):
    3. Delete Game
		    Delete Game Sub Menu:
			    Enter game ID to delete:
    4. Back to Main Menu

## 4. Review Management

Mange various game reviews. Users can add, edit, and remove their reviews.

    Review Management Menu:
    1. Write Review
	    Write Review Sub Menu:
		    Enter your user ID:
		    Enter game ID to review:
		    Enter your comment(leave blank for no comment):
		    Would you recommend this game to a friend?:
			    1. Yes
			    2. No
			    3. Don't Know/No opinion
				Select an option:
    2. Edit Review
	    Edit Review Sub Menu:
		    Enter review ID to edit:
		    Enter new score (leave blank to keep current):
		    Enter new comment (leave blank to keep current):
		    Would you still recommend this game to a friend?:
			    1. Yes
			    2. No
			    3. No change
    3. Delete Review
	    Delete Review Sub Menu:
		    Enter review ID to delete:
    4. Back to Main Menu

## 5. Sales Data
View and analyze general sales data. If looking for more specific sales analyzing selection `7. Analytics and Reports` from the main menu.

    Sales Data Menu:
    1. View Sales by Game
	    View Sales by Game Sub menu:
		    Enter game ID to view sales:
    2. View Sales by Region
	    View Sales by Region Sub Menu:
		    Enter region ID to view sales:
    3. View Best selling games by Region
	    View Best selling games by Region Sub Menu:
		    Enter region ID to view best selling games:
    4. View Best selling games by Genre
	    View Best selling games by Genre Sub Menu:
		    Enter genre ID to view best selling games:
    5. View Best selling games by Rating
	    View Best selling games by Rating Sub Menu:
		    Enter rating ID to view best selling games:
    6. View Best selling Publishers
    7. View Best selling Developers
    8. Back to Main Menu

## 6. Rating Information
View information regarding the game ratings and the various organizations that provide these ratings.
Rating Information Menu:

    1. View Ratings
    2. View Rating Organizations
    3. Back to Main Menu

## 7. Analytics and Reports

Query reports based on game analytics such as top games, sales performance, or impact of critic scores on sales performance.
Analytics and Reports Menu:

    1. Top Rated Games
    2. Most Reviewed Games
    3. Sales Performance Report:
	    Sales Performance Report Sub Menu:
		    Enter the year for sales report (leave blank for all years):
		    Enter region ID for sales report (leave blank for all regions):
    4. Best Critic Scored Games vs Sales
    5. Best User Scored Games vs Sales
    6. Compare Scores and Examine Sales Impact
    7. Back to Main Menu

## 8. Search

Having trouble finding a specific developer id, game id, or publisher id, look no further than the search function. Search by name and find a corresponding id number.

    Search Menu:
    1. Search Games
	    Enter game name or year to search:
    2. Search Developers
	    Enter developer name to search:
    3. Search Publishers
	    Enter publisher name to search:
    4. Back to Main Menu

## 9. Developer and Publisher Relations
Explore games by publisher, games by developer, and systems by publisher.

    Developer and Publisher Relations Menu:
    1. Games by Developer
    	Enter developer ID:
    2. Games by Publisher
    	Enter publisher ID:
    3. Systems by Publisher:
    	Enter publisher ID:
    4. Back to Main Menu


# Queries by Menu
![main menu](/photos/main_menu.png)
#  1. View Data Overview 
- ![view data view](/photos/view_data_menu.png)
- ![image](/photos/vd1.png)
- ![image](/photos/vd2.png)
- ![image](/photos/vd3.png)
- ![image](/photos/vd4.png)
- ![image](/photos/img1.png)
- ![image](/photos/img2.png)
- ![image](/photos/img3.png)
- ![image](/photos/img4.png)
- ![image](/photos/img5.png)
- ![image](/photos/img6.png)
- ![image](/photos/img7.png)
- ![image](/photos/img9.png)
- ![image](/photos/img10.png)
- ![image](/photos/img11.png)
- ![image](/photos/img12.png)
- ![image](/photos/img13.png)
- ![image](/photos/img14.png)
- ![image](/photos/img15.png)
- ![image](/photos/img16.png)
- ![image](/photos/img17.png)
# 4. Review Management Menu
- ![image](/photos/img18.png)
- ![image](/photos/img19.png)
- ![image](/photos/img20.png)
- ![image](/photos/img21.png)
# 5. Sales Data Menu
- ![image](/photos/img22.png)
- ![image](/photos/img23.png)
- ![image](/photos/img25.png)
- ![image](/photos/img26.png)
- ![image](/photos/img27.png)
- ![image](/photos/img28.png)
- ![image](/photos/img31.png)
- ![image](/photos/img32.png)
- ![image](/photos/img34.png)
- ![image](/photos/img35.png)
# 6. Rating Information Menu
- ![image](/photos/img38.png)
- ![image](/photos/img39.png)
- ![image](/photos/img41.png)
# 7. Analytics and Reports Menu
- ![image](/photos/img42.png)
- ![image](/photos/img43.png)
- ![image](/photos/img44.png)
- ![image](/photos/img45.png)
- ![image](/photos/img46.png)
- ![image](/photos/img48.png)
# 8. Search
- ![image](/photos/img49.png)
- ![image](/photos/img50.png)
- ![image](/photos/img51.png)
- ![image](/photos/img52.png)
# 9. Developer Publisher Relations Menu
- ![image](/photos/img53.png)
- ![image](/photos/img55.png)
- ![image](/photos/img56.png)