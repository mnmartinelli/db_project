import psycopg2
from prettytable import PrettyTable

# ----------Database Config----------
DATABASE = {
    'dbname': 'db',
    'user': 'postgres',
    'password': 'db',
    'host': 'localhost',
    'port': '5432'
}

#----------Connect to Database----------
def connect_to_db():
    try:
        return psycopg2.connect(**DATABASE)
    except psycopg2.Error as e:
        print(f"Unable to connect to the database: {str(e)}")
        exit(1)

#----------Query Database----------
def execute_query(query, params=None, fetch=False):
    conn = None
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(query, (params) if params else ())
        if fetch:
            return cur.fetchall()
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"An error occurred during query execution: {e}")
        return -1
    finally:
        if conn:
            conn.close()

#----------Format results----------
def display_results(results, headers):
    table = PrettyTable(field_names=headers)
    for row in results:
        table.add_row(row)
    print("\nResult:")
    print(table)


#########################################################################################################
##------------------------------------------------MENUS------------------------------------------------##
#########################################################################################################
#----------Main Menu Game Loop----------
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. View Data")
        print("2. User Management")
        print("3. Game Management")
        print("4. Review Management")
        print("5. Sales Data")
        print("6. Rating Information")
        print("7. Analytics and Reports")
        print("8. Search")
        print("9. Developer and Publisher Relations")
        print("10. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            view_data_menu()
        elif choice == '2':
            user_management_menu()
        elif choice == '3':
            game_management_menu()
        elif choice == '4':
            review_management_menu()
        elif choice == '5':
            sales_data_menu()
        elif choice == '6':
            rating_information_menu()
        elif choice == '7':
            analytics_and_reports_menu()
        elif choice == '8':
            search_menu()
        elif choice == '9':
            dev_pub_relations_menu()
        elif choice == '10':
            print("Exiting application.")
            break
        else:
            print("Invalid option, please try again.")

#----------1. View Data Menu----------
def view_data_menu():
    while True:
        print("\nView Data Menu:")
        print("1. Genres")
        print("2. Publishers")
        print("3. Developers")
        print("4. Platforms")
        print("5. Console Generations")
        print("6. Games")
        print("7. Reviews")
        print("8. Regions")
        print("9. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            view_genres()
        elif choice == '2':
            view_publishers()
        elif choice == '3':
            view_developers()
        elif choice == '4':
            view_platforms()
        elif choice == '5':
            view_generations()
        elif choice == '6':
            view_games()
        elif choice == '7':
            view_reviews()
        elif choice == '8':
            view_regions()
        elif choice == '9':
            break
        else:
            print("Invalid option, please try again.")

#----------2. User Management Menu----------
def user_management_menu():
    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Update User Info")
        print("3. Delete User")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            update_user_info()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")
 #----------3. Game Management Menu----------
def game_management_menu():
    while True:
        print("\nGame Management Menu:")
        print("1. Add New Game")
        print("2. Update Game Info")
        print("3. Delete Game")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_game()
        elif choice == '2':
            update_game_info()
        elif choice == '3':
            delete_game()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

#----------4. Review Management Menu----------
def review_management_menu():
    while True:
        print("\nReview Management Menu:")
        print("1. Write Review")
        print("2. Edit Review")
        print("3. Delete Review")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            write_review()
        elif choice == '2':
            edit_review()
        elif choice == '3':
            delete_review()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

#----------5. Sales Data Menu----------
def sales_data_menu():
    while True:
        print("\nSales Data Menu:")
        print("1. View Sales by Game")
        print("2. View Sales by Region")
        print("3. View Best selling games by Region")
        print("4. View Best selling games by Genre")
        print("5. View Best selling games by Rating")
        print("6. View Best selling Publishers")
        print("7. View Best selling Developers")
        print("8. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            view_sales_by_game()
        elif choice == '2':
            view_sales_by_region()
        elif choice == '3':
            view_best_selling_games_by_region()
        elif choice == '4':
            view_best_selling_games_by_genre()
        elif choice == '5':
            view_best_selling_games_by_rating()
        elif choice == '6':
            view_best_selling_publishers()
        elif choice == '7':
            view_best_selling_developers()
        elif choice == '8':
            break
        else:
            print("Invalid option, please try again.")
#----------6. Rating Information Menu----------
def rating_information_menu():
    while True:
        print("\nRating Information Menu:")
        print("1. View Ratings")
        print("2. View Rating Organizations")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            view_ratings()
        elif choice == '2':
            view_rating_organizations()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")

#----------7. Analytics and Reports Menu----------
def analytics_and_reports_menu():
    while True:
        print("\nAnalytics and Reports Menu:")
        print("1. Top Rated Games")
        print("2. Most Reviewed Games")
        print("3. Sales Performance Report")
        print("4. Best Critic Scored Games vs Sales")
        print("5. Best User Scored Games vs Sales")
        print("6. Compare Scores and Examine Sales Impact")
        print("7. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            top_rated_games()
        elif choice == '2':
            most_reviewed_games()
        elif choice == '3':
            sales_performance_report()
        elif choice == '4':
            best_critic_scored_games_vs_sales()
        elif choice == '5':    
            best_user_scored_games_vs_sales()
        elif choice == '6':
            compare_scores_and_examine_sales_impact()
        elif choice == '7':
            break
        else:
            print("Invalid option, please try again.")

#----------8. Search Menu----------
def search_menu():
    while True:
        print("\nSearch Menu:")
        print("1. Search Games")
        print("2. Search Developers")
        print("3. Search Publishers")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            search_games()
        elif choice == '2':
            search_developers()
        elif choice == '3':
            search_publishers()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

#----------9. Developer & Publisher Relations Menu----------
def dev_pub_relations_menu():
    while True:
        print("\nDeveloper and Publisher Relations Menu:")
        print("1. Games by Developer")
        print("2. Games by Publisher")
        print("3. Systems by Publisher")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            games_by_developer()
        elif choice == '2':
            games_by_publisher()
        elif choice == '3':
            systems_by_publisher()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

###################################################################################################################
##------------------------------------------------View Data Query------------------------------------------------##
###################################################################################################################
def best_critic_scored_games_vs_sales():
    query = """
    SELECT 
        g.name AS Game_Name, 
        pr.critic_score AS Critic_Score, 
        SUM(s.sales) AS Total_Sales
    FROM 
        public.games g
        JOIN public.public_reception pr ON g.gameid = pr.gameid
        JOIN public.sales s ON g.gameid = s.gameid
    WHERE 
        pr.critic_score IS NOT NULL
    GROUP BY 
        g.name, pr.critic_score
    ORDER BY 
        pr.critic_score DESC, Total_Sales DESC
    LIMIT 10;
    """
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Game Name", "Critic Score", "Total Sales"])
    else:
        print("An error occurred while fetching the results, please try again.")

#----------1. Genres----------
def view_genres():
    query = "SELECT genreid, genre_name FROM public.genres ORDER BY genreid;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["GenreID", "Genre Name"])
    else:
        print("An error occurred while trying to fetch result, please try again")

#----------2. Publishers----------
def view_publishers():
    query = "SELECT publisherid, pubname FROM public.publishers ORDER BY publisherid;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["PublisherID", "Publisher Name"])
    else:
        print("An error occurred while trying to fetch result, please try again")

#----------3. Developers----------
def view_developers():
    query = "SELECT developerid, devname FROM public.developers ORDER BY developerid;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["DeveloperID", "Developer Name"])
    else:
        print("An error occurred while trying to fetch result, please try again")

#----------4. Platforms----------
def view_platforms():
    while True:
        try:
            print("1. View all platforms")
            print("2. Filter by generation")
            print("3. Back to View Data Menu")
            choice = input("Select an option: ")
            if choice == '1':
                query = "SELECT platformid, platformname, generationid FROM public.platforms ORDER BY platformid;"
                results = execute_query(query, fetch=True)
                if results != -1:
                    display_results(results, ["PlatformID", "Platform Name", "Generation ID"])
                    return
                else:
                    print("An error occurred while trying to fetch result, please try again")
            elif choice == '2':
                view_generations() #show generation options, small table
                generation = input("Enter generation ID: ")
                if not generation.isdigit():
                    raise ValueError("Generation ID must be an integer number(1-9)")
                query = "SELECT platformid, platformname, generationid FROM public.platforms WHERE generationid = %s;"
                results = execute_query(query, (generation,), fetch=True)
                if results != -1:
                    display_results(results, ["PlatformID", "Platform Name", "Generation ID"])
                    return
                else:
                    print("An error occurred while trying to fetch result, please try again")
            elif choice == '3':
                break
            else:
                raise ValueError("Invalid option, please try again.")
        except Exception as e:
            print(f"Error in View Platforms: {e}")
#----------5. Generations----------
def view_generations():
    query = "SELECT generationid, start_year, end_year FROM public.Console_Generations ORDER BY generationid;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Generation ID", "Start Year", "Last Year"])
    else:
        print("An error occurred while trying to fetch result, please try again")

#----------6. Games----------
def view_games():
     while True:
        try:
            print("\n1. View all games")
            print("2. Filter by attributes")
            print("3. Back to View Data Menu")
            choice = input("Select an option: ")

            if choice == '1':
                while True:
                    query = """
                    SELECT COUNT(*) FROM public.games;
                    """
                    GAME_NUM = execute_query(query, fetch=True) #Number of games 
                    GAME_NUM = GAME_NUM[0][0]
                    print(f"\nThere are currently {GAME_NUM} games in the DB")
                    print(f"1. Load all {GAME_NUM} games")
                    print("2. View in pages of 1000")
                    print("3. Back to View Games Menu")
                    choice = input("Select an option: ")
                    if choice == '1':

                        query = """
                        SELECT g.gameid, g.name, g.year, gr.genre_name, p.pubname FROM public.games g
                        LEFT JOIN public.genres gr ON g.genreid = gr.genreid
                        LEFT JOIN public.publishers p ON g.publisherid = p.publisherid
                        ORDER BY g.name;
                        """
                        results = execute_query(query, fetch=True)
                        if results != -1:
                            display_results(results, ["Game ID", "Name", "Year", "Genre", "Publisher"])
                            return
                    elif choice == '2':
                        num = 0
                        while True:
                            query = f"""
                            SELECT g.gameid, g.name, g.year, gr.genre_name, p.pubname FROM public.games g
                            LEFT JOIN public.genres gr ON g.genreid = gr.genreid
                            LEFT JOIN public.publishers p ON g.publisherid = p.publisherid
                            ORDER BY g.name
                            LIMIT 1000 OFFSET {num};
                            """
                            num+=1000
                            results = execute_query(query, fetch=True)
                            if results != -1:
                                display_results(results, ["Game ID", "Name", "Year", "Genre", "Publisher"])
                            print("\n1. Show next 1000 Games")
                            print("2. Exit")
                            choice = input("Select an option: ")
                            if num > GAME_NUM:
                                return
                            if choice == '2':
                                return
                            elif choice == '1':
                                continue
                            else:
                                print("Invalid option, please try again.")
                                
                    elif choice == '3':
                        print("\n")
                        break
                    else:
                        print("Invalid option, please try again.")

            elif choice == '2':
                filter_games()
                return
            elif choice == '3':
                break
            else:
                raise ValueError("Invalid option, please try again.")
        except Exception as e:
            print(f"Error in Game Platforms: {e}")
    
    #----------6.2 Filter by attributes----------
def filter_games():
    while True:
        try:
            print("\nEnter filter criteria:")
            view_genres() #shows all genres 
            genre = input("Genre ID (leave blank if no filter): ")
            view_publishers() #shows all publishers
            publisher = input("Publisher ID (leave blank if no filter): ")
            year = input("Year (leave blank if no filter): ")

            conditions = []
            params = []

            if genre:
                conditions.append("g.genreid = %s")
                params.append(genre)
            if publisher:
                if not publisher.isdigit():
                    raise ValueError("Publisher ID must be an valid integer")
                conditions.append("g.publisherid = %s")
                params.append(publisher)
            if year:
                if not year.isdigit():
                    raise ValueError("Year must be a valid integer")
                conditions.append("g.year = %s")
                params.append(year)
            condition_str = " AND ".join(conditions) if conditions else "1=1" # Formats the WHERE condition for when cases fields are left blank
            query = f"""
                SELECT g.gameid, g.name, g.year, gr.genre_name, p.pubname 
                FROM public.games g
                LEFT JOIN public.genres gr ON g.genreid = gr.genreid
                LEFT JOIN public.publishers p ON g.publisherid = p.publisherid
                WHERE {condition_str}
                ORDER BY g.name;
            """
            results = execute_query(query, params, fetch=True)
            if results != -1:
                display_results(results, ["Game ID", "Name", "Year", "Genre", "Publisher"])
                return
            else:
                print("An error occurred while trying to fetch result, please try again")
        except Exception as e:
            print(f"Error in Game Platforms: {e}")
            return


#----------7. Reviews----------
def view_reviews():
    try:
        game_id = input("Enter Game ID to filter by (leave blank for no filter): ")
        if game_id:
            if not game_id.isdigit():
                raise ValueError("Game ID must be an valid integer")
            query = "SELECT * FROM public.reviews WHERE gameid = %s;"
            results = execute_query(query, (game_id,), fetch=True)
        else:
            query = "SELECT * FROM public.reviews;"
            results = execute_query(query, fetch=True)
        if results != -1:
            display_results(results, ["Review ID", "User ID", "Game ID", "Score", "Comment", "Recommend"])
        else:
            print("An error occurred while trying to fetch result, please try again")
    except Exception as e:
            print(f"Error in Game Platforms: {e}")
#----------8. Regions----------
def view_regions():
    query = "SELECT regionid, name FROM public.regions;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Region ID", "Region Name"])
    else:
        print("An error occurred while trying to fetch result, please try again")

###################################################################################################################
##------------------------------------------------User Management------------------------------------------------##
###################################################################################################################

#----------1. Create User----------
def create_user():
    try:
        name = input("Enter user name: ").strip()
        if not name:
            raise ValueError("User name cannot be empty")
        view_regions()  # Show available regions
        region_id = input("Enter region ID: ").strip()
        if not region_id.isdigit():
            raise ValueError("Region ID must be a number.")
        if int(region_id) > 5 or int(region_id) <1:
            raise ValueError("Region ID must be a interger between 1 and 5.")
        query = "INSERT INTO public.users (name, regionid) VALUES (%s, %s);"
        execute_query(query, (name, region_id))
        #show results
        query = """
        SELECT Users.*, Regions.Name AS RegionName
        FROM Users
        JOIN Regions ON Users.RegionID = Regions.RegionID
        ORDER BY Users.UserID DESC
        LIMIT 1;
        """
        results = execute_query(query, fetch=True)
        if results != -1:
            display_results(results, ["User ID", "Name", "Region ID", "Region Name"])
        print("User created successfully")
    except Exception as e:
        print(f"Failed to create user: {e}")

#----------2. Update User Info----------
def update_user_info():
    try:
        user_id = input("Enter user ID to update: ").strip()
        if not user_id.isdigit():
            raise ValueError("User ID must be a number")

        new_name = input("Enter new name (leave blank to keep current): ").strip()
        new_region_id = input("Enter new region ID (leave blank to keep current): ").strip()
        if new_region_id and not new_region_id.isdigit():
            raise ValueError("Region ID must be a number.")

        query = "UPDATE public.users SET name = COALESCE(%s, name), regionid = COALESCE(%s, regionid) WHERE userid = %s;"
        results = execute_query(query, (new_name or None, new_region_id or None, user_id))
        
        if results != -1:
            print("User updated successfully")
        query = """
        SELECT Users.*, Regions.Name AS RegionName
        FROM Users
        JOIN Regions ON Users.RegionID = Regions.RegionID
        WHERE Users.UserId = %s;
        """
        results = execute_query(query, (user_id,), fetch=True)
        if results != -1:
            display_results(results, ["User ID", "Name", "Region ID", "Region Name"])
    except Exception as e:
        print(f"Error updating user: {e}")

#----------3. Delete User----------
def delete_user():
    try:
        user_id = input("Enter user ID to delete: ")
        if not user_id.isdigit():
            raise ValueError("User ID must be a Integer")

        query = "DELETE FROM public.users WHERE userid = %s;"
        results = execute_query(query, (user_id,)) #comma after user_id is crucial when passing in single parameters
        if results != -1:
            print("User deleted successfully")
        else:
            print("An error occurred; deletion failed")
    except Exception as e:
        print(f"Error deleting user: {e}")



###################################################################################################################
##------------------------------------------------GAME Management------------------------------------------------##
###################################################################################################################
    
#----------1. Add New Game----------
def add_new_game():
    try:
        name = input("Enter game name: ").strip()
        if not name:
            raise ValueError("Game name cannot be empty")
        year = input("Enter game year: ").strip()
        if not year.isdigit():
            raise ValueError("Year must be a number")
        genre_id = input("Enter genre ID: ").strip()
        if not genre_id.isdigit():
            raise ValueError("Genre ID must be a number")
        publisher_id = input("Enter publisher ID: ").strip()
        if not publisher_id.isdigit():
            raise ValueError("Publisher ID must be a number.")
        rating_id = input("Enter rating ID (leave blank for no rating): ")
        results = -1 #Init
        if rating_id:
            query = "INSERT INTO public.games (name, year, genreid, publisherid, ratingid) VALUES (%s, %s, %s, %s, %s);"
            results = execute_query(query, (name, year, genre_id, publisher_id, rating_id))
        else:
            query = "INSERT INTO public.games (name, year, genreid, publisherid) VALUES (%s, %s, %s, %s);"
            results = execute_query(query, (name, year, genre_id, publisher_id))
        if results != -1:
            print("Game added successfully")
            query = """
            SELECT g.gameid, g.name, g.year, gr.genre_name, g.ratingID, p.pubname FROM public.games g
            LEFT JOIN public.genres gr ON g.genreid = gr.genreid
            LEFT JOIN public.publishers p ON g.publisherid = p.publisherid
            ORDER BY g.gameid DESC
            LIMIT 1;
            """
            results = execute_query(query, fetch=True)
            if results != -1:
                display_results(results, ["Game ID", "Name", "Year", "Genre", "Rating", "Publisher"])
        else:
            print("An error occurred while trying to fetch result, please try again")
    except Exception as e:
        print(f"Error adding new game: {e}")


#----------2. Update Game Info----------
def update_game_info():
    try:
        game_id = input("Enter game ID to update: ").strip()
        if not game_id.isdigit():
            raise ValueError("Game ID must be a number.")
        new_name = input("Enter new name (leave blank to keep current): ").strip()
        new_year = input("Enter new year (leave blank to keep current): ").strip()
        new_genre_id = input("Enter new genre ID (leave blank to keep current): ").strip()
        new_publisher_id = input("Enter new publisher ID (leave blank to keep current): ").strip()
        new_rating_id = input("Enter new rating ID (leave blank to keep current): ").strip()
        query = """
        UPDATE public.games SET 
        name = COALESCE(%s, name), 
        year = COALESCE(%s, year), 
        genreid = COALESCE(%s, genreid), 
        publisherid = COALESCE(%s, publisherid),
        ratingid = COALESCE(%s, ratingid)
        WHERE gameid = %s;
        """
        results =execute_query(query, (new_name or None, new_year or None, new_genre_id or None, new_publisher_id or None, new_rating_id or None, game_id))
        if results != -1:
            print("Game updated successfully")
            query = """
                SELECT g.gameid, g.name, g.year, gr.genre_name, g.ratingID, p.pubname FROM public.games g
                LEFT JOIN public.genres gr ON g.genreid = gr.genreid
                LEFT JOIN public.publishers p ON g.publisherid = p.publisherid
                WHERE g.gameid = %s;
            """
            results = execute_query(query, (game_id,), fetch=True)
            if results != -1:
                display_results(results, ["Game ID", "Name", "Year", "Genre", "Rating", "Publisher"])
        else:
            print("An error occurred while trying to fetch result, please try again")
    except Exception as e:
        print(f"Failed to update Game: {e}")

#----------3. Delete Game----------    
def delete_game():
    try:
        game_id = input("Enter game ID to delete: ").strip()
        if not game_id.isdigit():
            raise ValueError("Game ID must be a number")
        query = "DELETE FROM public.games WHERE gameid = %s;"
        results = execute_query(query, (game_id,))
        if results != -1:
            print("Game deleted successfully")
        else:
            print("An error occurred while trying to fetch result, please try again")
    except Exception as e:
        print(f"Failed to delete Game: {e}")
    


###################################################################################################################
##------------------------------------------------Review Management------------------------------------------------##
###################################################################################################################

#----------1. Write Review----------  
def write_review():
    try:
        user_id = input("Enter your user ID: ").strip()
        if not user_id.isdigit():
            raise ValueError("User ID must be a number.")
        game_id = input("Enter game ID to review: ").strip()
        if not game_id.isdigit():
            raise ValueError("Game ID must be a number.")
        score = input("Enter your score (1.0-5.0): ").strip()
        if float(score)>5.0 or float(score) <1.0:
            raise ValueError("Score be a float number (1.0-5.0).")
        comment = input("Enter your comment(leave blank for no comment): ").strip()
        print("Would you recommend this game to a friend?:")
        print("1. Yes")
        print("2. No")
        print("3. Don't Know/No opinion")
        recommend = input("Select an option: ").strip()
        if int(recommend)==1:
            recommend="True"
        elif int(recommend)==2:
            recommend="False"
        elif int(recommend)==3:
            recommend=None
        else:
            raise ValueError("Invalid option for Recommend, please try again.")
        results = -1 #Init
        if recommend:
            query = "INSERT INTO public.reviews (userid, gameid, score, comment, recommend) VALUES (%s, %s, %s, %s, %s);"
            results = execute_query(query, (user_id, game_id, score, comment, recommend))
            if results != -1:
                print("Review added successfully.")
            else:
                print("An error occurred while fetching result, please try again")
        else:
            query = "INSERT INTO public.reviews (userid, gameid, score, comment) VALUES (%s, %s, %s, %s);"
            results = execute_query(query, (user_id, game_id, score, comment))
            if results != -1:
                print("Review added successfully.")
            else:
                print("An error occurred while fetching result, please try again")
        if results !=-1:
            query = "SELECT * FROM public.reviews WHERE gameid = %s AND userid = %s ORDER BY reviewid DESC LIMIT 1;"
            results = execute_query(query, (game_id,user_id), fetch=True)
            if results != -1:
                display_results(results, ["Review ID", "User ID", "Game ID", "Score", "Comment", "Recommend"])
            else:
                print("An error occurred while trying to fetch result, please try again")
    except Exception as e:
        print(f"Failed to write review: {e}")
#----------2. Edit Review----------  
def edit_review():
    try:
        review_id = input("Enter review ID to edit: ").strip()
        if not review_id.isdigit():
            raise ValueError("Review ID must be a number.")
        new_score = input("Enter new score (leave blank to keep current): ").strip()
        new_comment = input("Enter new comment (leave blank to keep current): ").strip()
        print("Would you still recommend this game to a friend?:")
        print("1. Yes")
        print("2. No")
        print("3. No change")
        new_recommend = input("Select an option: ").strip()
        if int(new_recommend)==1:
            new_recommend="True"
        elif int(new_recommend)==2:
            new_recommend="False"
        elif int(new_recommend)==3:
            new_recommend=None
        else:
            raise ValueError("Invalid option for Recommend, please try again.")
        results = -1; #init
        if new_recommend:
            query = "UPDATE public.reviews SET score = COALESCE(%s, score), comment = COALESCE(%s, comment), recommend = COALESCE(%s, recommend) WHERE reviewid = %s;"
            results = execute_query(query, (new_score or None, new_comment or None, new_recommend, review_id))
        else:
            query = "UPDATE public.reviews SET score = COALESCE(%s, score), comment = COALESCE(%s, comment) WHERE reviewid = %s;"
            results = execute_query(query, (new_score or None, new_comment or None, review_id))
        
        if results != -1:
            print("Review updated successfully.")
            query = "SELECT * FROM public.reviews WHERE reviewid = %s;"
            results = execute_query(query, (review_id,), fetch=True)
            if results != -1:
                display_results(results, ["Review ID", "User ID", "Game ID", "Score", "Comment", "Recommend"])
            else:
                print("An error occurred while trying to fetch result, please try again")
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Failed to edit review: {e}")

#----------3. Delete Review----------  
def delete_review():
    try:
        review_id = input("Enter review ID to delete: ").strip()
        if not review_id.isdigit():
            raise ValueError("Review ID must be a number.")
        query = "DELETE FROM public.reviews WHERE reviewid = %s;"
        results =execute_query(query, (review_id,))
        if results != -1:
            print("Review deleted successfully.")
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Failed to delete review: {e}")



###################################################################################################################
##------------------------------------------------Review Management------------------------------------------------##
###################################################################################################################
#----------1. View Sales by Game----------  
def view_sales_by_game():
    try:
        game_id = input("Enter game ID to view sales: ").strip()
        if not game_id.isdigit():
            raise ValueError("Game ID must be a number.")
        query = "SELECT regionid, sales FROM public.sales WHERE gameid = %s;"
        results = execute_query(query, (game_id,), fetch=True)
        if results != -1:
            display_results(results, ["Region ID", "Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing sales by game: {e}")
#----------2. View Sales by Region----------  
def view_sales_by_region():
    try:
        region_id = input("Enter region ID to view sales: ").strip()
        if not region_id.isdigit():
            raise ValueError("Region ID must be a number.")
        query = "SELECT gameid, sales FROM public.sales WHERE regionid = %s;"
        results = execute_query(query, (region_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing sales by region: {e}")

#----------3. View Best selling games by Region---------- 
def view_best_selling_games_by_region():
    try:
        region_id = input("Enter region ID to view best selling games: ").strip()
        query = """
            SELECT s.gameid, g.name, s.sales 
            FROM public.sales s 
            JOIN public.games g ON s.gameid = g.gameid 
            WHERE s.regionid = %s 
            ORDER BY s.sales DESC 
            LIMIT 10;
        """
        results = execute_query(query, (region_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Game Name", "Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing best selling games by region: {e}")

#----------4. View Best selling games by Genre---------- 
def view_best_selling_games_by_genre():
    try:
        genre_id = input("Enter genre ID to view best selling games: ").strip()
        query = """
            SELECT s.gameid, g.name, s.sales 
            FROM public.sales s 
            JOIN public.games g ON s.gameid = g.gameid 
            WHERE g.genreid = %s 
            ORDER BY s.sales DESC 
            LIMIT 10;
        """
        results = execute_query(query, (genre_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Game Name", "Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing best selling games by genre: {e}")

#----------5. View Best selling games by Rating----------
def view_best_selling_games_by_rating():
    try:
        rating_id = input("Enter rating ID to view best selling games: ").strip()
        query = """
            SELECT s.gameid, g.name, s.sales 
            FROM public.sales s 
            JOIN public.games g ON s.gameid = g.gameid 
            WHERE g.ratingid = %s 
            ORDER BY s.sales DESC 
            LIMIT 10;
        """
        results = execute_query(query, (rating_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Game Name", "Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing best selling games by rating: {e}")

#----------6. View Best selling publishers---------
def view_best_selling_publishers():
    try:
        query = """
        SELECT p.pubname, SUM(s.sales) AS total_sales
        FROM public.sales s
        JOIN public.games g ON s.gameid = g.gameid
        JOIN public.publishers p ON g.publisherid = p.publisherid
        GROUP BY p.pubname
        ORDER BY total_sales DESC
        LIMIT 10;
        """
        results = execute_query(query, fetch=True)
        if results and results != -1:
            display_results(results, ["Publisher Name", "Total Sales"])
        else:
            print("An error occurred while fetching the results, please try again.")
    except Exception as e:
        print(f"Error viewing best selling publishers: {e}")

    

#----------7. View Best selling developers---------
def view_best_selling_developers():
    try:
        query = """
            SELECT d.developerid, d.devname, SUM(s.sales) AS total_sales
            FROM public.sales s
            JOIN public.games g ON s.gameid = g.gameid
            JOIN public.game_developers gd ON g.gameid = gd.gameid
            JOIN public.developers d ON gd.developerid = d.developerid
            GROUP BY d.developerid, d.devname
            ORDER BY total_sales DESC
            LIMIT 10;
        """
        results = execute_query(query, fetch=True)
        if results != -1:
            display_results(results, ["Developer ID", "Developer Name", "Total Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Error viewing best selling developers: {e}")

###################################################################################################################
##------------------------------------------------Rating Management----------------------------------------------##
###################################################################################################################

#----------1. View Review----------  
def view_ratings():
    rating_org_id = input("Enter rating organization ID to filter by (leave blank for no filter): ").strip()
    if rating_org_id:
        query = "SELECT ratingid, title, descriptions FROM public.ratings WHERE ratingorgid = %s;"
        results = execute_query(query, (rating_org_id,), fetch=True)
    else:
        query = "SELECT ratingid, title, descriptions FROM public.ratings;"
        results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Rating ID", "Title", "Description"])
    else:
        print("An error occurred while fetching result, please try again")

#----------2. ViewRating Organizations Review----------  
def view_rating_organizations():
    query = "SELECT ratingorgid, title, year_established FROM public.rating_orgs;"
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Rating Org ID", "Title", "Year Established"])
    else:
        print("An error occurred while fetching result, please try again")



###################################################################################################################
##------------------------------------------------Analytics and Reports------------------------------------------##
###################################################################################################################

#----------1. Top Rated Games---------- 
def top_rated_games():
    query = """
    SELECT g.name, AVG(r.score) as avg_score
    FROM public.games g
    JOIN public.reviews r ON g.gameid = r.gameid
    GROUP BY g.name
    ORDER BY avg_score DESC
    LIMIT 10;
    """
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Game Name", "Average Score"])
    else:
        print("An error occurred while fetching result, please try again")


#----------2. Most Reviewed Games---------- 
def most_reviewed_games():
    query = """
    SELECT g.name, COUNT(r.reviewid) as review_count
    FROM public.games g
    JOIN public.reviews r ON g.gameid = r.gameid
    GROUP BY g.name
    ORDER BY review_count DESC
    LIMIT 10;
    """
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Game Name", "Review Count"])
    else:
        print("An error occurred while fetching result, please try again")

#----------3. Sales Performance Report---------- 
def sales_performance_report():
    try:
        year = input("Enter the year for sales report (leave blank for all years): ").strip()
        if not year.isdigit():
            raise ValueError("Year must be a valid integer")
        region_id = input("Enter region ID for sales report (leave blank for all regions): ").strip()
        if not region_id.isdigit():
                raise ValueError("Region ID must be a number.")
        if int(region_id) > 5 or int(region_id) <1:
            raise ValueError("Region ID must be a interger between 1 and 5.")
        query = """
        SELECT g.name, SUM(s.sales) as total_sales
        FROM public.sales s
        JOIN public.games g ON s.gameid = g.gameid
        WHERE (%s IS NULL OR g.year = %s) AND (%s IS NULL OR s.regionid = %s)
        GROUP BY g.name
        ORDER BY total_sales DESC;
        """
        params = (year, year, region_id, region_id)
        results = execute_query(query, params, fetch=True)
        if results != -1:
            display_results(results, ["Game Name", "Total Sales"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"Failed to find sales figures: {e}")

#----------4. Best Critic Scored games Vs Sales---------- 
def best_critic_scored_games_vs_sales():
    try:
        query = """
        SELECT 
            g.name AS Game_Name, 
            pr.critic_score AS Critic_Score, 
            SUM(s.sales) AS Total_Sales
        FROM 
            public.games g
            JOIN public.public_reception pr ON g.gameid = pr.gameid
            JOIN public.sales s ON g.gameid = s.gameid
        WHERE 
            pr.critic_score IS NOT NULL
        GROUP BY 
            g.name, pr.critic_score
        ORDER BY 
            pr.critic_score DESC, Total_Sales DESC
        LIMIT 10;
        """
        results = execute_query(query, fetch=True)
        if results != -1:
            display_results(results, ["Game Name", "Critic Score", "Total Sales"])
        else:
            print("An error occurred while fetching the results, please try again.")
    except Exception as e:
        print(f"Failed to find sales figures: {e}")

#----------5. Best User Scored Games vs Sales---------- 
def best_user_scored_games_vs_sales():
    query = """
    SELECT 
        g.name AS Game_Name, 
        pr.consumer_score AS User_Score, 
        SUM(s.sales) AS Total_Sales
    FROM 
        public.games g
        JOIN public.public_reception pr ON g.gameid = pr.gameid
        JOIN public.sales s ON g.gameid = s.gameid
    WHERE 
        pr.consumer_score IS NOT NULL
    GROUP BY 
        g.name, pr.consumer_score
    ORDER BY 
        pr.consumer_score DESC, Total_Sales DESC
    LIMIT 10;
    """
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Game Name", "User Score", "Total Sales"])
    else:
        print("An error occurred while fetching the results, please try again.")

#----------6. Compare Scores and Examine Sales Impact--------- 
def compare_scores_and_examine_sales_impact():
    query = """
    SELECT 
        g.name AS Game_Name, 
        pr.critic_score AS Critic_Score, 
        pr.consumer_score AS User_Score, 
        ABS(pr.critic_score - pr.consumer_score) AS Score_Discrepancy,
        SUM(s.sales) AS Total_Sales
    FROM 
        public.games g
        JOIN public.public_reception pr ON g.gameid = pr.gameid
        JOIN public.sales s ON g.gameid = s.gameid
    WHERE 
        pr.critic_score IS NOT NULL AND pr.consumer_score IS NOT NULL
    GROUP BY 
        g.name, pr.critic_score, pr.consumer_score
    ORDER BY 
        Score_Discrepancy DESC, Total_Sales DESC
    LIMIT 10;
    """
    results = execute_query(query, fetch=True)
    if results != -1:
        display_results(results, ["Game Name", "Critic Score", "User Score", "Score Discrepancy", "Total Sales"])
    else:
        print("An error occurred while fetching the results, please try again.")

###################################################################################################################
##------------------------------------------------Search Menu----------------------------------------------------##
###################################################################################################################

#----------1. Search Games---------- 
def search_games():
    term = input("Enter game name or year to search: ").strip()
    query = "SELECT gameid, name, year FROM public.games WHERE name ILIKE %s OR CAST(year AS TEXT) ILIKE %s;"
    results = execute_query(query, ('%' + term + '%', '%' + term + '%'), fetch=True)
    if results != -1:
        display_results(results, ["Game ID", "Name", "Year"])
    else:
        print("An error occurred while fetching result, please try again")
        
#----------2. Search Developers---------- 
def search_developers():
    term = input("Enter developer name to search: ").strip()
    query = "SELECT developerid, devname FROM public.developers WHERE devname ILIKE %s;"
    results = execute_query(query, ('%' + term + '%',), fetch=True)
    if results != -1:
        display_results(results, ["Developer ID", "Developer Name"])
    else:
        print("An error occurred while fetching result, please try again")

#----------3. Search Publishers---------- 
def search_publishers():
    term = input("Enter publisher name to search: ").strip()
    query = "SELECT publisherid, pubname FROM public.publishers WHERE pubname ILIKE %s;"
    results = execute_query(query, ('%' + term + '%',), fetch=True)
    if results != -1:
        display_results(results, ["Publisher ID", "Publisher Name"])
    else:
        print("An error occurred while fetching result, please try again")



###################################################################################################################
##------------------------------------------------Developer & Publisher Relations Menu----------------------------------------------------##
###################################################################################################################

#----------1. Games by Developer---------- 
def games_by_developer():
    try:
        developer_id = input("Enter developer ID: ").strip()
        if not developer_id.isdigit():
            raise ValueError("Developer ID must be a number")
        query = """
        SELECT g.gameid, g.name FROM public.games g
        JOIN public.game_developers gd ON g.gameid = gd.gameid
        WHERE gd.developerid = %s;
        """
        results = execute_query(query, (developer_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Game Name"])
    except Exception as e:
        print(f"ERROR: {e}")

#----------2. Games by Publisher---------- 
def games_by_publisher():
    try:
        publisher_id = input("Enter publisher ID: ").strip()
        if not publisher_id.isdigit():
            raise ValueError("Publisher ID must be a number")
        query = """
        SELECT gameid, name FROM public.games
        WHERE publisherid = %s;
        """
        results = execute_query(query, (publisher_id,), fetch=True)
        if results != -1:
            display_results(results, ["Game ID", "Game Name"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"ERROR: {e}")

#----------3. Systems by Publisher---------- 
def systems_by_publisher():
    try:
        publisher_id = input("Enter publisher ID: ").strip()
        if not publisher_id.isdigit():
            raise ValueError("Publisher ID must be a number")
        query = """
        SELECT platformid, platformname, year_launched FROM public.platforms
        WHERE publisherid = %s;
        """
        results = execute_query(query, (publisher_id,), fetch=True)
        if results != -1:
            display_results(results, ["Platform ID", "Platform Name", "Year Launched"])
        else:
            print("An error occurred while fetching result, please try again")
    except Exception as e:
        print(f"ERROR: {e}")

#----------Main Menu Call----------
if __name__ == "__main__":
    main_menu()
