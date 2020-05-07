'''
Wrapper for accessing reddit api
'''

import praw
import nltk.data


def get_data_from_post(input_url):
	'''
	returns dictionary containing post title and list of post comments
	'''

	reddit = praw.Reddit(user_agent='Comment Extraction (by /u/bing2912)',
	                     client_id='8GnbCVc5SmQXgQ', client_secret="AaX1o4t6X99U409ZR06DLXd5o-4"
	                     #,username='USERNAME', password='PASSWORD'
	                    )

	submission = reddit.submission(url = input_url)

	comments = []
	#saving top 20 comments
	'''
	Extracts top level comments from a reddit thread
	'''
	for comment in submission.comments[:20]:
		comments.append(comment.body)

	data = {
	"title" : submission.title,
	"selftext" : submission.selftext,
	"comments" : comments
	}

	return data



def extract_book_from_comment(text):
	'''
	input : comment string
	output : python dictionary in below format
	{
	'book' : extracted book name,
	'author' : extracted author name
	} 
	'''

	#split the comment into sentences
	#lines = text.splitlines() #primitive method
	tokenizer = nltk.data.load('nltk:tokenizers/punkt/PY3/english.pickle')
	print(tokenizer.tokenize(text)) 

	#extract books out of each sentence.
	
	