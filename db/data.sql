insert into Users (uID, name, userName, profilePic, email, age, bio, isMod)
    values (1, 'crash kardashian', 'crashes', NULL, 'crash@yahoo.com', 9, 'Hi Im Crash', 1);

insert into Users (uID, name, userName, profilePic, email, age, bio, isMod)
    values (2, 'harvey kardashian', 'harveys', NULL, 'harvey@yahoo.com', 10, 'Hi Im Harvey', 0);

insert into Users (uID, name, userName, profilePic, email, age, bio, isMod)
    values (3, 'michael kardashian', 'michael', NULL, 'michael@yahoo.com', 11, 'Hi Im Michael', 1);

insert into Users (uID, name, userName, profilePic, email, age, bio, isMod)
    values (4, 'chris kardashain', 'chris', NULL, 'chris@yahoo.com', 12, NULL, 0);

insert into Media (mID, content, contentType)
    values (100, '/media/image1.jpg', 0);

insert into Media (mID, content, contentType)
    values (101, '/media/video.mp4', 1);

insert into Media (mID, content, contentType)
    values (102, '/media/audio.mp3', 2);

insert into Posts (pID, mID, uID, voteNo, title, description)
    values (201, 100, 1, 0, 'What is the deal with airline food?', 'It nasty 4 real');

insert into Posts (pID, mID, uID, voteNo, title, description)
    values (202, 101, 2, 100, 'Fire Breathing Rubber Duckies are cool', NULL);

insert into Posts (pID, mID, uID, voteNo, title, description)
    values (203, 102, 3, -1, 'Why the downvotes?', 'Rude');

insert into Posts (pID, mID, uID, voteNo)
    values (204, 100, 4, -100);

insert into Comments (cID, pID, uID, voteNo, content)
    values (301, 201, 2, 10, 'I fully agree');

insert into Comments (cID, pID, uID, voteNo, content)
    values (302, 202, 4, 200, 'Truer words have never been spoken');

insert into Conversations (conveID, participants1, participants2)
    values (401, 1, 2);

insert into Conversations (conveId, participants1, participants2)
    values (402, 4, 1);

insert into Messages (mesID, uID, conveID, content)
    values (501, 1, 401, 'What is Chris even doing, he seems confused');

insert into Messages (mesID, uID, conveID, content)
    values (502, 2, 401, 'Yeah, he is struggling for sure');

insert into Messages (mesID, uID, conveID, content)
    values (503, 4, 402, 'I heard you were talking smack');

