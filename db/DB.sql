create table Users(
	uID INT NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(80) NOT NULL ,
	userName VARCHAR(16) NOT NULL,
	profilePic TEXT(512),
	email VARCHAR(320) NOT NULL,
	age INT,
	bio VARCHAR(500),
	joinedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	isMod BOOL NOT NULL,
	PRIMARY KEY (uID)
);

create table Media(
	mID INT NOT NULL UNIQUE AUTO_INCREMENT,
	content TEXT(512) NOT NULL,
	contentType INT NOT NULL,
	PRIMARY KEY (mID)
);

create table Posts(
	pID INT NOT NULL UNIQUE AUTO_INCREMENT,
	mID INT NOT NULL,
	uID INT NOT NULL,
	voteNo INT NOT NULL,
	title VARCHAR(64) NOT NULL,
	description VARCHAR(512),
	timePosted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (pID),
	FOREIGN KEY (uID) REFERENCES Users(uID),
	FOREIGN KEY (mID) REFERENCES Media(mID)
);

create table Comments(
	cID INT NOT NULL UNIQUE AUTO_INCREMENT,
	pID INT NOT NULL,
	uID INT NOT NULL,
	voteNo INT NOT NULL,
	content VARCHAR(240) NOT NULL,	
	FOREIGN KEY (pID) REFERENCES Posts(pID),
	FOREIGN KEY (uID) REFERENCES Users(uID)
);
create table Conversations (
	conveID INT NOT NULL UNIQUE AUTO_INCREMENT,
	timeCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	participants1 INT NOT NULL,
	participants2 INT NOT NULL,
	PRIMARY KEY (conveID),
	FOREIGN KEY (participants1) REFERENCES Users(uID),
	FOREIGN KEY (participants2) REFERENCES Users(uID)
);

create table Messages (
	mesID INT NOT NULL UNIQUE AUTO_INCREMENT,
	uID INT NOT NULL,
	conveID INT NOT NULL,
	timePosted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	content VARCHAR(240),
	PRIMARY KEY (mesID),
	FOREIGN KEY (uID) REFERENCES Users(uID),
	FOREIGN KEY (conveID) REFERENCES Conversations(conveID)
);

