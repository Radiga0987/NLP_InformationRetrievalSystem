from util import *

import nltk
from nltk.corpus import words
from nltk.metrics.distance  import edit_distance
nltk.download('words')

class SpellCheck():

    def __init__(self):
        pass

    # def correct_spellings(self, text):
    #     correct_words = words.words()

    #     if isinstance(text, list):
    #         new_text = []
    #         for sent in text:
    #             if isinstance(sent, list):
    #                 new_sent = []
    #                 for token in sent:
    #                     if isinstance(token, str):
    #                         temp = [(edit_distance(token, w),w) for w in correct_words if w[0]==token[0]]
    #                         corrected_word = sorted(temp, key = lambda val:val[0])[0][1]
    #                         new_sent.append(corrected_word)
    #                     else:
    #                         print("Error: Expected string token, received a " + str(type(token)))
    #                         return []

    #                 new_text.append(new_sent)
                
    #             else:
    #                 print("Error: Expected sentence as a list, received a " + str(type(sent)))
    #                 return []

    #         spell_corrected_text = new_text
		
    #     else:
    #         print("Error: Expected document as list, received a " + str(type(text)))
    #         return []

    #     return spell_corrected_text

    def correct_spellings(self, text):
        correct_words = words.words()

        if isinstance(text, list):
            new_text = []
            for sent in text:
                if isinstance(sent, list):
                    new_sent = []
                    for token in sent:
                        if isinstance(token, str):
                            if token in words.words():
                                new_sent.append(token)
                                print("lololololllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
                            else:
                                temp = [(edit_distance(token, w),w) for w in correct_words if w[0]==token[0]]
                                if len(temp) > 0:
                                    corrected_word = sorted(temp, key = lambda val:val[0])[0][1]
                                    new_sent.append(corrected_word)
                                    print(token,corrected_word)
                                else:
                                    new_sent.append(token)
                        else:
                            print("Error: Expected string token, received a " + str(type(token)))
                            return []

                    new_text.append(new_sent)
                
                else:
                    print("Error: Expected sentence as a list, received a " + str(type(sent)))
                    return []

            spell_corrected_text = new_text
		
        else:
            print("Error: Expected document as list, received a " + str(type(text)))
            return []

        return spell_corrected_text


if __name__=='__main__':
	# Testing
	sc = SpellCheck()
	print(sc.correct_spellings([['aeroplan', 'behavier', 'radii','peice','cars', 'suitcases', 'ar','ogive']]))  # car, suitcas, radii