--#1 Genres
CREATE TABLE Genres (
    GenreID SERIAL PRIMARY KEY,
    Genre_Name VARCHAR(255) NOT NULL
);

--#1.1 Insert Data:
\copy Genres FROM 'C:\Users\micha\Desktop\DB_2\Genre.csv' WITH (FORMAT csv, HEADER true);

--#1.2 SELECT Data:
SELECT *
FROM Genres
LIMIT 5;

--#2 Publishers
CREATE TABLE Publishers (
    PublisherID SERIAL PRIMARY KEY,
    PubName VARCHAR(255) NOT NULL
);
--#2.1 Insert Data:
\copy Publishers FROM 'C:\Users\micha\Desktop\DB_2\Publisher.csv' WITH (FORMAT csv, HEADER true);
--#2.2 SELECT Data:
SELECT *
FROM Publishers
LIMIT 5;


--#3 Developers
CREATE TABLE Developers (
    DeveloperID SERIAL PRIMARY KEY,
    DevName VARCHAR(255) NOT NULL
);
--#3.1 Insert Data:
\copy Developers FROM 'C:\Users\micha\Desktop\DB_2\Developer.csv' WITH (FORMAT csv, HEADER true);
--#3.2 SELECT Data:
SELECT *
FROM Developers
LIMIT 5;


--#4 Regions
CREATE TABLE Regions (
    RegionID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);
--#4.1 Insert Data:
\copy Regions FROM 'C:\Users\micha\Desktop\DB_2\Region.csv' WITH (FORMAT csv, HEADER true);
--#4.2 SELECT Data:
SELECT *
FROM Regions
LIMIT 5;


--#5 Users
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    RegionID INT REFERENCES Regions(RegionID)
);

--#5.1 Insert Data:
\copy Users FROM 'C:\Users\micha\Desktop\DB_2\Users.csv' WITH (FORMAT csv, HEADER true);
--#5.2 SELECT Data:
SELECT *
FROM Users
LIMIT 5;


--#6 Console_Generations
CREATE TABLE Console_Generations (
    GenerationID SERIAL PRIMARY KEY,
    Start_Year INT NOT NULL,
    End_Year INT
);
--#6.1 Insert Data:
\copy Console_Generations FROM 'C:\Users\micha\Desktop\DB_2\Console_Generation.csv' WITH (FORMAT csv, HEADER true);
--#6.2 SELECT Data:
SELECT *
FROM Console_Generations
LIMIT 5;


--#7 Rating_Orgs
CREATE TABLE Rating_Orgs (
    RatingOrgID VARCHAR(255) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Year_Established INT NOT NULL,
    RegionID INT REFERENCES Regions(RegionID)
);
--#7.1 Insert Data:
\copy Rating_Orgs FROM 'C:\Users\micha\Desktop\DB_2\Rating_Orgs.csv' WITH (FORMAT csv, HEADER true);
--#7.2 SELECT Data:
SELECT *
FROM Rating_Orgs
LIMIT 5;


--#8 Ratings
CREATE TABLE Ratings (
    RatingOrgID VARCHAR(255) REFERENCES Rating_Orgs(RatingOrgID),
    RatingID VARCHAR(255) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Descriptions TEXT
);
--#8.1 Insert Data:
\copy Ratings FROM 'C:\Users\micha\Desktop\DB_2\Rating.csv' WITH (FORMAT csv, HEADER true);
--#8.2 SELECT Data:
SELECT *
FROM Ratings
LIMIT 5;


--#9 Platforms
CREATE TABLE Platforms (
    PlatformID SERIAL PRIMARY KEY,
    PlatformName VARCHAR(255) NOT NULL,
    GenerationID INT REFERENCES Console_Generations(GenerationID),
    Full_Title VARCHAR(255) NOT NULL,
    Year_Launched INT NOT NULL,
    PublisherID INT REFERENCES Publishers(PublisherID)
);
--#9.1 Insert Data:
\copy Platforms FROM 'C:\Users\micha\Desktop\DB_2\Platform.csv' WITH (FORMAT csv, HEADER true);
--#9.2 SELECT Data:
SELECT *
FROM Platforms
LIMIT 5;


--#10 Games
CREATE TABLE Games (
    GameID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Year INT NOT NULL,
    GenreID INT REFERENCES Genres(GenreID),
    PublisherID INT REFERENCES Publishers(PublisherID),
    RatingID VARCHAR(255) REFERENCES Ratings(RatingID)
);
--#10.1 Insert Data:
\copy Games FROM 'C:\Users\micha\Desktop\DB_2\Game.csv' WITH (FORMAT csv, HEADER true);
--#10.2 SELECT Data:
SELECT *
FROM Games
LIMIT 5;


--#11 Game_Developers
CREATE TABLE Game_Developers (
    GameID INT REFERENCES Games(GameID),
    DeveloperID INT REFERENCES Developers(DeveloperID),
    PRIMARY KEY (GameID, DeveloperID)
);
--#11.1 Insert Data:
\copy Game_Developers FROM 'C:\Users\micha\Desktop\DB_2\Game_Developers.csv' WITH (FORMAT csv, HEADER true);
--#11.2 SELECT Data:
SELECT *
FROM Game_Developers
LIMIT 5;


--#12 Reviews
CREATE TABLE Reviews (
    ReviewID SERIAL PRIMARY KEY,
    UserID INT REFERENCES Users(UserID),
    GameID INT REFERENCES Games(GameID),
    Score FLOAT CHECK (Score >= 0 AND Score <=5) NOT NULL,
    Comment TEXT,
    Recommend BOOLEAN
);
--#12.1 Insert Data:
\copy Reviews FROM 'C:\Users\micha\Desktop\DB_2\Review.csv' WITH (FORMAT csv, HEADER true);
--#12.2 SELECT Data:
SELECT *
FROM Reviews
LIMIT 5;


--#13 Reviews
CREATE TABLE Public_Reception (
    GameID INT PRIMARY KEY REFERENCES Games(GameID),
    Critic_Score FLOAT,
    Critic_Count INT,
    Consumer_Score FLOAT,
    Consumer_Count INT
);
--#13.1 Insert Data:
\copy Reviews FROM 'C:\Users\micha\Desktop\DB_2\Review.csv' WITH (FORMAT csv, HEADER true);
--#13.2 SELECT Data:
SELECT *
FROM Public_Reception
LIMIT 5;


--#14 Sales
CREATE TABLE Sales (
    GameID INT REFERENCES Games(GameID),
    RegionID INT REFERENCES Regions(RegionID),
    Sales FLOAT NOT NULL,
    PRIMARY KEY (GameID, RegionID)
);
--#14.1 Insert Data:
\copy Sales FROM 'C:\Users\micha\Desktop\DB_2\Sales.csv' WITH (FORMAT csv, HEADER true);
--#14.2 SELECT Data:
SELECT *
FROM Sales
LIMIT 5;


--# MAKE SURE TO RUN THESE COMMANDS!!!!
SELECT setval('public.genres_genreid_seq', (SELECT MAX(genreid) FROM public.genres) + 1);
SELECT setval('public.publishers_publisherid_seq', (SELECT MAX(publisherid) FROM public.publishers) + 1);
SELECT setval('public.developers_developerid_seq', (SELECT MAX(developerid) FROM public.developers) + 1);
SELECT setval('public.regions_regionid_seq', (SELECT MAX(regionid) FROM public.regions) + 1);
SELECT setval('public.users_userid_seq', (SELECT MAX(userid) FROM public.users) + 1);
SELECT setval('public.console_generations_generationid_seq', (SELECT MAX(generationid) FROM public.console_generations) + 1);
SELECT setval('public.platforms_platformid_seq', (SELECT MAX(platformid) FROM public.platforms) + 1);
SELECT setval('public.games_gameid_seq', (SELECT MAX(gameid) FROM public.games) + 1);
SELECT setval('public.reviews_reviewid_seq', (SELECT MAX(reviewid) FROM public.reviews) + 1);
