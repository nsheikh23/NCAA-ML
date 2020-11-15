CREATE TABLE NBAdraft (
    Pick INTEGER,
    Name VARCHAR,
    Conference VARCHAR,
    College VARCHAR
);

CREATE TABLE BballStats (
    Player VARCHAR,
    Team VARCHAR,
    GP INTEGER,
    MPG FLOAT,
    FGM FLOAT,
    FGA FLOAT,
    FG_pct FLOAT,
    ThreePM FLOAT,
    ThreePA FLOAT,
    Three_pct FLOAT,
    FTM FLOAT,
    FTA FLOAT,
    FT_pct FLOAT,
    TOV FLOAT,
    PF FLOAT,
    ORB FLOAT,
    DRB FLOAT,
    RPG FLOAT,
    APG FLOAT,
    SPG FLOAT,
    BPG FLOAT,
    PPG FLOAT
);

CREATE TABLE Basketball (
    Player VARCHAR,
    Team VARCHAR,
    GP INTEGER,
    MPG FLOAT,
    FGM FLOAT,
    FGA FLOAT,
    FG_pct FLOAT,
    ThreePM FLOAT,
    ThreePA FLOAT,
    Three_pct FLOAT,
    FTM FLOAT,
    FTA FLOAT,
    FT_pct FLOAT,
    TOV FLOAT,
    PF FLOAT,
    ORB FLOAT,
    DRB FLOAT,
    RPG FLOAT,
    APG FLOAT,
    SPG FLOAT,
    BPG FLOAT,
    PPG FLOAT,
    Pick INTEGER,
    Conference VARCHAR,
    College VARCHAR,
    CollegeBudgetFile VARCHAR,
    Latitude FLOAT,
    Longitude FLOAT,
    Expense INTEGER,
    Revenue INTEGER
)

CREATE TABLE Football (
    DraftYear INTEGER,
    Rnd INTEGER,
    Pick INTEGER,
    Team VARCHAR,
    Player VARCHAR,
    GradeFileID VARCHAR,
    Position VARCHAR,
    College VARCHAR,
    CollegeBudgetFileName VARCHAR,
    Conference VARCHAR,
    Latitude FLOAT,
    Longitude FLOAT,
    Expense INTEGER,
    Revenue INTEGER
);

CREATE TABLE schools (
    School VARCHAR,
    Latitude VARCHAR,
    Longitude VARCHAR,
    State VARCHAR,
    Revenue VARCHAR,
    Expense VARCHAR,
    Sports VARCHAR
);
