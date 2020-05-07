import requests
from bs4 import BeautifulSoup as bs
from . import nlp_functions


class goodreadsClass:
	def __init__(self, book_name):
		self.data = get_data_from_book_name()
		self.title_match = nlp_functions.string_comparison(gr_data.get("title",""), book_name)


def get_data_from_book_name(book_name, key='wXPAWZT7nxpEXt4v478Q'):
	'''
	Does what the function name says
	'''
	try:
		url = "https://www.goodreads.com/search/index.xml?key={}&q={}".format(key, book_name)

		r = requests.get(url , timeout=20)

		soup = bs(r.content, "lxml")

		data = {
		'search_book_name' : book_name,
		'title_id' : soup.find('work').find('best_book').find('id').text,
		'title' : soup.find('work').find('best_book').find('title').text,
		'author_id' : soup.find('work').find('author').find('id').text,
		'author_name' : soup.find('work').find('author').find('name').text
		}

		#return soup.find('work').find('id').text
		return data
	except:
		return {}



	

