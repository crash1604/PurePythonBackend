from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import cgi
import string
import random
from controller import *

hostname="localhost"
serverport=8000

global userid
userid=1


	


class server(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path =='/':
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			output=HomeViewHandler()
			self.wfile.write(output.encode())
			
		if self.path=='/post/create/':
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			output=PostCreateForm()
			self.wfile.write(output.encode())		
			
		if self.path.startswith('/post/') and self.path[6:-1].isdigit() and self.path.endswith('/'):
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			print(self.path[6:-1])
			postID=self.path[6:-1]
			#need some place holder code to check if the post exists or not
			output=PostViewHandler(postID)
			self.wfile.write(output.encode())
			
		if self.path=='/search/':
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			print(self.path[6:-1])
			#need some place holder code to check if the post exists or not
			output=SearchViewHandler
			self.wfile.write(output.encode())
		
		if self.path.startswith('/search/results/') and self.path[-1:]=='/':
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			lookup= self.path[16:-1]
			output=SearchResultHandler(lookup)
			self.wfile.write(output.encode())
			
		if self.path.startswith('/user/') and self.path[6:-1].isdigit() and self.path.endswith('/'):
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			print(self.path[6:-1])
			#need some place holder code to check if the post exists or not
			output=''' <div>
			<h2> This is a User </h2>
			</div>
			'''
			self.wfile.write(output.encode())
			
		if self.path=='/messages/':
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			print(self.path[6:-1])
			#need some place holder code to check if the post exists or not
			output=''' <div>
			<h2> This page lists all the conversations</h2>
			</div>
			'''
			self.wfile.write(output.encode())
			
		if self.path.startswith('/messages/') and self.path[10:-1].isdigit() and self.path.endswith('/'):
			self.send_response(200)
			self.send_header('content-type','text/html')
			self.end_headers()
			print(self.path[10:-1])
			roomid=self.path[10:-1]
			#need some place holder code to check if the post exists or not
			output=''' <div>
			<h2> This is a Specific Conversation room </h2>
			<form method="POST" enctype="multipart/form-data" action="/messages/%s/">
			<input name="msgContent"type="text" placeholder="Send something awesome for others to view">
			<br>			
			<input type="submit" value="Send">
		</form>
			</div>
			''' % (self.path[10:-1])
			self.wfile.write(output.encode())
				
	def do_POST(self):
		if self.path=='/post/create/':
			ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
			pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
			#for demonstration purposes we have the user id hardcoded but irl that hardcoded value would be the userid
			if ctype=='multipart/form-data':
				fields=cgi.parse_multipart(self.rfile,pdict)
				new_caption = fields.get('caption')
				new_caption=str(new_caption)
				new_caption=new_caption[3:-2]				
				new_title = fields.get('postTitle')
				new_title=str(new_title)
				new_title=new_title[3:-2]
				new_file= fields.get('filename')
				file_type=str(fields.get('type'))
				fileformat=0
				if file_type[3:-2] == 'on':
					fileformat=1
				new_file=str(new_file)
				new_file=new_file[3:-2]
				mediaID= 100
				mediaID=MediaHandler(fileformat,new_file,userid)
				#ideally when a user is created, it would also make a repository with user's unique id and all the media is stored in it
				#in this line call a function to send data to db
				postID=PostCreateHandler(mediaID, userid, new_title, new_caption)
			redirect='/post/'+postID+'/'
			self.send_response(301)
			self.send_header('content-type','text/html')
			self.send_header('Location', redirect)
			self.end_headers()
		
		if self.path=='/search/':
			redirect='/search/results/'
			ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
			pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
			content_len= int(self.headers.get('Content-length'))
			pdict['CONTENT-LENGTH']=content_len
			if ctype=='multipart/form-data':
				fields=cgi.parse_multipart(self.rfile,pdict)
				results = fields.get('lookup')
				print(results)
				results=str(results)
				results=results[3:-2]
				results = results.replace(' ','-')
				redirect+=results+'/'
				#in this line call a function to send data to db
				print(results)
			self.send_response(301)
			self.send_header('content-type','text/html')
			self.send_header('Location', redirect)
			self.end_headers()

		if self.path.startswith('/messages/') and self.path[10:-1].isdigit() and self.path.endswith('/'):
			ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
			pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
			redirect=self.path
			if ctype=='multipart/form-data':
				fields=cgi.parse_multipart(self.rfile,pdict)
				new_caption = fields.get('msgContent')
				#in this line call a function to send data to db
				print(new_caption)
			self.send_response(301)
			self.send_header('content-type','text/html')
			self.send_header('Location', redirect)
			self.end_headers()

httpd = HTTPServer((hostname, serverport),server)
httpd.serve_forever()
