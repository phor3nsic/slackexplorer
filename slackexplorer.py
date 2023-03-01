import requests
import re
import json
from lib import regex
from time import sleep
import argparse

s = requests.Session()
API = "https://slack.com/api/"
banner = """

   ____     __    __    ____           __                
  / __/__ _/ /___/ /__ / __/_ __ ___  / /__  _______ ____
 _\ \/ _ `/ / __/  '_// _/ \ \ // _ \/ / _ \/ __/ -_) __/
/___/\_,_/_/\__/_/\_\/___//_\_\/ .__/_/\___/_/  \__/_/   
                              /_/                        
by: @phor3nsic_br
"""

def check_auth(token, cookie = None):
	if cookie != None:
		s.headers.update({'Cookie':cookie})
	req = s.post(API+"auth.test?token="+token)
	if req.status_code == 200:
		return req.json()

def dump_users(token):

	url = API+'users.list?token='+token
	
	req = s.post(url)
	
	if req.status_code == 200:
		return req.json()

def check_conversation(token, cursor = None, responses = None):
	cont = 0

	if responses == None:
		responses = []
		
	
	url = API+'conversations.list?token='+token
	if cursor != None:
		url = url+f'&cursor={cursor}' 
	req = s.post(url)

	if req.status_code == 200:
		responses.append(req.json())

	if req.json()['response_metadata']['next_cursor']:
		sleep(1)
		cont += 1
		if cont <= MAX:
			return check_conversation(token, req.json()['response_metadata']['next_cursor'], responses)
	return responses

def navigate_chat(token, chat_id, cursor = None, responses = None):
	count = 0
	if responses == None:
		responses = []
		
	
	url = API+f'conversations.history?token={token}&channel={chat_id}'
	if cursor != None:
		url = url+f'&cursor={cursor}'
	req = s.post(url)
	if req.status_code == 200:
		responses.append(req.json())

	if req.json()['has_more'] == True:
		sleep(1)
		count += 1
		if count <= MAX:
			return navigate_chat(token, chat_id, req.json()['response_metadata']['next_cursor'], responses)
	return responses

def output_save(file_name, text):
	with open(file_name, 'a+') as f:
		f.write(text+'\n')

def check_keys_on_chat(chat_text, expression, name):
	match = re.search(expression, chat_text)
	if match:
		n_print('[!] ' + name + ' : "' + match.group() + '"' )

def n_print(text):
	print(text)
	if OUTPUT != None:
		output_save(OUTPUT, text) if OUTPUT else n_print()

if __name__ == "__main__":
	OUTPUT = None
	MAX = 1000
	n_print(banner)
	parser = argparse.ArgumentParser()
	parser.add_argument('token', help='Token of slack')
	parser.add_argument('-c','--cookie', help='Cookie of token ex: xoxc-')
	parser.add_argument('-o','--output', help='Output save')
	parser.add_argument('-r', '--recursion', help='Maximum recursion Default: 1000 (Maximum of python)')
	args = parser.parse_args()
	
	token = args.token
	if args.output:
		OUTPUT = args.output
	
	if args.recursion:
		MAX = args.recursion
		
	auth_data = check_auth(token, args.cookie)
	user = auth_data['user']
	team = auth_data['team']
	team_id = auth_data['team_id']
	user_id = auth_data['user_id']
	team_url = auth_data['url']

	n_print(f'[i] User: {user} id: {user_id}')
	n_print(f'[i] Team: {team} id: {team_id} url: {team_url}')
	n_print('='*30)
	n_print('DUMP USERS')
	
	users = dump_users(token)['members']

	for user in users:
		try:
			email = user['profile']['email']
		except:
			email = ''
		name = user['profile']['real_name']
		n_print(f'[+] name: {name},   email: {email}')

	n_print(f'[i] Total users: {str(len(users))}')
	n_print('='*30)
	n_print('FIND KEYS ON CHATS')

	response_chats = check_conversation(token)
	for data in response_chats:
		chats = data['channels']
		for chat in chats:
			sleep(1)
			chat_id = chat['id']
			responses = navigate_chat(token, chat_id)
			for response in responses:
				history = response['messages']
				for message in history:
					for expression in regex.regex:
						check_keys_on_chat(message['text'], regex.regex[expression], expression )