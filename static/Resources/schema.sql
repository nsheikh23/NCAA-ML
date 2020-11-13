CREATE TABLE NBAdraft (
    Pick INTEGER,
    Player VARCHAR,
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

CREATE TABLE NFL (
    DraftYear INTEGER,
    Rnd INTEGER,
    Pick INTEGER,
    Tm VARCHAR,
    Player VARCHAR,
    Age INTEGER,
    To INTEGER,
    AP1 INTEGER,
    PB INTEGER,
    St INTEGER,
    CarAV INTEGER,
    DrAV INTEGER,
    G INTEGER,
    Cmp INTEGER,
    Att15 INTEGER,
    Yds16 INTEGER,
    TD17 INTEGER,
    Int18 INTEGER,
    Att19 INTEGER,
    Yds20 INTEGER,
    TD21 INTEGER,
    Rec INTEGER,
    Yds23 INTEGER,
    TD24 INTEGER,
    Solo INTEGER,
    Int26 INTEGER,
    Sk FLOAT,
    School VARCHAR
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
