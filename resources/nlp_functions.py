'''
All text wrangling functions are included in this file
'''

import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import traceback
import Levenshtein



class entity:
    '''
    Generic entity class - book / song / idea
    '''
    def __init__(self):
        self.entity_name = ''
        self.creator_name = '' #author/artist



def extract_keywords_from_text(input_text):
    '''
    Returns token in input text that are present in keyword list / Or not in custom stopword list
    '''

    stop = set(stopwords.words('english'))
    return [i for i in input_text.lower().split() if i not in stop]


def extract_names_from_string(input_text):
    '''
    Extracts book name and author name from string.
    Returns a list of strings / tuple where each tuple is a book, author pair.
    '''

    '''
    #This block is to extract text inside quotes

    if "'" in input_text:
        input_text = input_text.replace("'", '"')
        name_list = re.findall('"([^"]*)"', input_text)
        print(len(name_list))       
        if len(name_list) == 0:
            print('entered if')
            #Remove apostrophe
            #input_text = input_text.replace("'",'')
            #input_text = input_text.translate(str.maketrans({"'":None}))
            print(input_text)
        else:
            print('entered else')
            return name_list

    if '"' in input_text:       
        return re.findall('"([^"]*)"', input_text)
    '''


    if 'by' in input_text:
        book_name = input_text.split('by')[0].strip()
        author_name = input_text.split('by')[1].strip() 
        
        if '.' in author_name:
            x_pos = author_name.find('.') #position of full_stop
            author_name = author_name[:x_pos]
        
        #return [(book_name, author_name)]
        data = {
        'book_name' : book_name,
        'author_name' : author_name
        }   

        return data

    if '-' in input_text:
        book_name = input_text.split('-')[0].strip()
        author_name = input_text.split('-')[1].strip() 
        
        if '.' in author_name:
            x_pos = author_name.find('.') #position of full_stop
            author_name = author_name[:x_pos]
        
        #return [(book_name, author_name)]

        data = {
        'book_name' : book_name,
        'author_name' : author_name
        }   

        return data

    '''
    else:
        return 'No if condition matched'
    '''


'''
String Comparison functions
'''


def TokenComparison(a, b):
    '''
    Compares two lists position wise and returns tuples of mismatch values
    '''
    #print([(i,j) for i, j in zip(a, b) if i != j])
    return [(i,j) for i, j in zip(a, b) if i != j]


def Compare_mismatch_tokens(token_tuple):
    '''
    Compares two tokens and returns Levenshtein distance between them
    '''
    #print(Levenshtein.distance(token_tuple[0], token_tuple[1]))
    return Levenshtein.distance(token_tuple[0], token_tuple[1])


def string_comparison(a, b):
    #a -> market network name (usually smaller than b)
    #b -> scraped result name (usually longer than a)

    '''
    Improvement over Advanced_ExactStringComparison : 

    Replace frequent mismatch tokens.

    Accommodate compound word differences.
    '''

    try:
        '''
        stop_words = ['', 'limited', 'private', 'ltd', 'pvt', 'and', '&', 'p', 'pvtltd']
        '''
        stop_words = []

        '''
        #replace words dictionary
        replace_dict = {
        'co' : 'company',
        'engg' : 'engineering', 
        'corp' : 'corporation',
        'i' : 'india'
        }
        '''
        replace_dict = {

        }

        #convert to lower case and strip

        a = a.lower().strip()
        b = b.lower().strip()


        #replace '.' and "," with 'space'
        a = a.replace(".", " ").replace(","," ").replace("("," ").replace(")"," ").replace("-"," ")
        b = b.replace(".", " ").replace(","," ").replace("("," ").replace(")"," ").replace("-"," ")
        
        source_name = a.split(' ') 
        source_name_tokens = [str(x) for x in source_name if str(x) not in stop_words]
        source_name_tokens = [replace_dict.get(str(x)) if str(x) in replace_dict else str(x) for x in source_name_tokens]
        source_name = " ".join(source_name_tokens)
        #print(source_name_tokens)
        
        result_name = b.split(' ')
        result_name_tokens = [str(x) for x in result_name if str(x) not in stop_words]
        result_name_tokens = [replace_dict.get(str(x)) if str(x) in replace_dict else str(x) for x in result_name_tokens]
        result_name = " ".join(result_name_tokens)
        #print(result_name_tokens)
        
        if source_name == result_name:
            #return True
            #return "Match : Exact string match"
            return "Match"
        else:
            #Going for advanced validation
            if len(source_name_tokens) == len(result_name_tokens):
                mismatch_tokens = TokenComparison(source_name_tokens, result_name_tokens)
                #print(mismatch_tokens)
                if len(mismatch_tokens) == 1:
                    if Compare_mismatch_tokens(mismatch_tokens[0]) == 1:
                        #return True
                        #return "Match : Single character difference"
                        return "Match"
                    else:
                        #return False
                        #return "Mismatch : Multiple character difference"
                        pass
                else:
                    #return False
                    #return "Mismatch : More than one mismatch tokens"
                    pass
            else:
                #return False
                #return "Mismatch : String lengths differ"
                pass

        ### Proceeding to compound word match
        source_name = "".join(source_name_tokens)
        result_name = "".join(result_name_tokens)

        if source_name == result_name:
            #return True
            #return "Match : Compound word match"
            return "Match"
        else:
            return "Mismatch"

    except Exception as e:
        #return 'Error' #error code
        return traceback.format_exc()
