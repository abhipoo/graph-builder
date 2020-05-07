from resources import goodreads
from resources import nlp_functions
from resources import reddit
from resources import database_functions


test_url = 'https://www.reddit.com/r/booksuggestions/comments/f1hf3f/what_are_some_books_with_plot_that_offer/'

data = reddit.get_data_from_post(test_url)

keywords = nlp_functions.extract_keywords_from_text(data.get('title') + "," + data.get('selftext'))

list_of_books = []

for comment in data.get('comments'):
	entity_list = nlp_functions.extract_names_from_string(comment) #list of book and author names extracted
	if entity_list:
		for entity in entity_list:
			if isinstance(entity, tuple):
				list_of_books.append(entity[0])
			else:
				list_of_books.append(entity)
	
	

print(keywords)

print()

print(list_of_books)


##goodreads


validated_books = []

for book in list_of_books:
	gr_data = goodreads.get_data_from_book_name(book)
	if nlp_functions.string_comparison(gr_data.get("title",""), book) == "Match":
		validated_books.append(book)

print(validated_books)


#format the final data output to be saved in mongo.





