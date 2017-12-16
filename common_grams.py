import re
import sqlite3

word_tokenizer = re.compile('[\w|#|\'|.|\"]*[\w|\'|\"]+', re.IGNORECASE)

stop_words = set(["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"])

def tokenize_document(document):
  token_list = word_tokenizer.findall(document)
  return list(map(lambda token: token.lower(), token_list))

def find_ngrams(input_list, n):
  return list(zip(*[input_list[i:] for i in range(n)]))

def get_descriptions():
    conn = sqlite3.connect('routes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM routes')
    protection = []
    for x in c.fetchall():
      protection.append(x[2].replace("SR", "standard rack"))

    return protection


def get_trigrams(gram_count, remove_stop_words):
  gram_list = {}
  for x in get_descriptions():
    tokens = tokenize_document(x)
    if remove_stop_words:
      for idx,item in enumerate(tokens):
        if item in stop_words:
          del tokens[idx:]

    tri_grams = find_ngrams(tokens, gram_count)
    for y in tri_grams:
      if y in gram_list:
        count = gram_list.get(y)
        gram_list[y] = count+1
      else:
        gram_list[y] = 1
  
  return gram_list
  

def find_most_common_trigrams(gram_count, remove_stop_words):
  key = lambda x: (x[1],x[0])
  count = 0
  for key, value in sorted(get_trigrams(gram_count, remove_stop_words).items(), key=key):
    print(key, value)
    count += 1

  print(count)


  






  