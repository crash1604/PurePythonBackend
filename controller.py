from db import *
import os
import random
import string



#this section will contain some meta data which will remain mostly constant through out
global head
global content
global body

head='''<html><head></head><body><div>'''

body=''' </div></body></html>'''



#section ends

def NameGenerator():
	filename=''.join(random.choice(string.digits) for i in range (10))
	return './Users/678/'+filename

	
def HomeViewHandler():
	rows=getAllPosts()
	content=''' <h1>Home page of VIUIT</h1> <br><h2>Daily feed</h2><a href="/post/create/">new post</a>'''
	for row in rows:
		content +='''
		<div>
		<a href="/post/%d/"><h3>%s</h3></a>
		<p>%s</p>
		''' %(row[0],row[4],row[5])
		media=getMedia({row[1]})
		if media[2]==1:
			content+='''
			<img src="%s" alt="img">
		
			''' %(media[1])
		username=getUsername({row[2]})
		content +='''<p>%s <span>%s</span></p>			
		</div>		
		''' %(username,row[6])
	output= head+content+body
	return output

def PostCreateForm():
	content='''
		<h2>Create a New Post</h2>
		<form method="POST" enctype="multipart/form-data" action="/post/create/">
			<input type="radio" name="type" id="picture" value="1">
			<label for="picture">Picture</label>
			<input name="postTitle" type="text"><br>
			<input name="caption"type="text" placeholder="Add some interesting captions">
			<br>	
			<input name="filename" type="file">	
			<br>	
			<input type="submit" value="Post">
		</form>
		'''
	output= head+content+body
	return output

def MediaHandler(filetype, filecontent,userID):
	fn=NameGenerator()
	dirname='./Users'+str(userID)+'/'+str(fn)+'.jpeg'
	filelocal=open(dirname,'w')
	filelocal.write(filecontent)
	mediaID=setMedia(filetype, dirname)
	return mediaID
		

def PostCreateHandler(mediaID,userID,title,description):
	#this function is pretty much alllocation
	postID=setPost(mediaID,userID,title,description)
	return postID

def PostViewHandler(postID):
	row=getPost(postID)
	content ='''
		<div>
		<a href="/post/%d/"><h3>%s</h3></a>
		<p>%s</p>
		''' %(row[0],row[4],row[5])
	media=getMedia({row[1]})
	if media[2]==1:
		content+='''
			<img src="%s" alt="img">
		
	''' %(media[1])
	username=getUsername({row[2]})
	content +='''<p>%s <span>%s</span></p>			
	</div>		
	''' %(username,row[6])
	output= head+content+body
	return output
	
def SearchViewHandler():
	content=''' <div>
			<form method="POST" enctype="multipart/form-data" action="/search/">
			<input name="lookup"type="text" placeholder="VIU something interesting">
			<br>			
			<input type="submit" value="Search">
		</form>
			</div>
			'''
	output= head+content+body
	return output
	
def SearchResultHandler(target):
	content=''' <div>
			<h1>Search Results</h1>
			</div>
			'''
	output= head+content+body
	return output
	
def UserViewHandler(userID):
	row=getUser(userID)
	content='''
	<div>
	<h1>%s</h1>
	<h2>%s</h2>
	<p>%s</p>
	<h4> Moderator status: %s</h4>
	</div>
	'''	%(row[1],row[2],row[6],row[7],row[8])
	output= head+content+body
	return output
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	