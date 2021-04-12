import pymysql

hostname='wwwstu.csci.viu.ca'
username='csci375d'
passphrase='KUaYLoZv'
db='csci375d'


def getUsername(userID):
	connection =pymysql.connect(hostname,username, passphrase,db) 
	with connection.cursor() as cursor:
		sql='SELECT userName FROM Users WHERE uID=%s;'
		cursor.execute(sql,userID) 
		row=cursor.fetchone()
	print('fetching the post')
	connection.close()
	return row[0]

def setPost(mediaID,userID,title,description):
    connection= pymysql.connect(hostname,
                            username,
                            passphrase,
                            db,
                        )

    with connection.cursor() as cursor:
        sql= "insert into Posts (mID, uID, voteNo, title, description) values (%d, %d, 0, '%s', '%s')" %(mediaID,userID,title,description)
        #prepared query
        cursor.execute(sql)
        connection.commit()
    print('successful post insert')
    cursor.execute("SELECT pID FROM Posts WHERE mID= %s and uID = %s",(mediaID,UserID))
    row=cursor.fetchone()
    connection.close()
    return row
    

def getAllPosts():
    connection= pymysql.connect(hostname,
                            username,
                            passphrase,
                            db
                        )

    with connection.cursor() as cursor:
        sql ='SELECT * FROM Posts;'
        cursor.execute(sql)
        rows = cursor.fetchall()
    print('generating all the output')
    connection.close()
    return rows

def getPost(postID):
    connection =pymysql.connect(hostname,username, passphrase,db)
    with connection.cursor() as cursor:
        sql='SELECT * FROM Posts WHERE pID=%s;'
        cursor.execute(sql,postID) 
        row=cursor.fetchone()
    print('fetching the post')
    connection.close()
    return row

def setMedia(fileType,uri):
    connection =pymysql.connect(hostname,username,passphrase,db)
    with connection.cursor() as cursor:
        sql='insert into Media (content, contentType) values (%s, %s,%s);'
        cursor.execute(sql,(cfileType,uri))
    print('insert successful')
    cursor.execute("SELECT mID FROM Posts WHERE url= %s",uri)
    row=cursor.fetchone()
    connection.close()
    return row
    
def getMedia(mediaID):
	connection =pymysql.connect(hostname,username, passphrase,db)
	with connection.cursor() as cursor:
		sql='SELECT * FROM Media WHERE mID=%s;'
		cursor.execute(sql,mediaID)
		row=cursor.fetchone()
	print('fetching the post')
	connection.close()
	return row
    
def setComment(postID, userID,commentContent):
	connection =pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql='insert into Comments (content, contentType, url) values (%s, %s,%s);'
		cursor.execute(sql,(postID, userID,commentContent))
		print('insert successful')
	cursor.execute("SELECT cID FROM Posts WHERE pID= %s and uID = %s",(postID,UserID))
	row=cursor.fetchone()
	connection.close()
	return row
    
def getComments(postID):
	connection= pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql ='SELECT * FROM Comments where pID=%s;'
		cursor.execute(sql,postID)
		rows = cursor.fetchall()
	print('generating all the output')
	connection.close()
	return rows
    
    
def setConversations(user1,user2,):
	connection =pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql='insert into Conversations (participants1, participants2) values (%s, %s);'
		cursor.execute(sql,(user1,user2))
		print('insert successful')
	cursor.execute("SELECT conveID FROM Posts WHERE participants1= %s and participants2 = %s",(user1,user2))
	row=cursor.fetchone()
	connection.close()
	return row
   
def getConversatioList(user):
	connection= pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql ='SELECT * FROM Conversation where participants1=%s or participants2=%s;'
		cursor.execute(sql,(user,user))
		rows = cursor.fetchall()
	print('generating all the output')
	connection.close()
	return rows
    
def sendMessages(userID,conversationID, message):
	connection =pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql='insert into Messages (uID, conveID, content) values (%s, %s, %s);'
		cursor.execute(sql,(userID,conversationID, message))
	print('insert successful')
	connection.close()

def getMessages(conversationID, userID):
	connection= pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql ='SELECT * FROM Messages where conveID=%s and uID=%s;'
		cursor.execute(sql,(conversationID,user))
		rows = cursor.fetchall()
	print('generating all the output')
	connection.close()
	return rows
	
def getUser(userID):
	connection= pymysql.connect(hostname,username,passphrase,db)
	with connection.cursor() as cursor:
		sql ='SELECT * FROM  Users where uID=%s;'
		cursor.execute(sql,(userID))
		rows = cursor.fetchall()
	print('generating all the output')
	connection.close()
	return rows



