import re
import nltk
import unidecode


dico_path = "dico.txt"

# bien-\nvenu --> bienvenu
def remove_dash_for_linebreak(text):
	return(re.sub("\-\\n", "", text))


# le jour\nse lève --> le jour se lève
def remove_linebreak(text):
	return(re.sub("\\n", " ", text))


# remove extra whitespace
def remove_extra_whitespace(text):
	new_text = re.sub("\s+", " ", text)
	return(new_text)


# normalization
def normalization(text, case="lower"):
	"""
	Normalize text either in lower or upper case
	argument:
	case STRING 
		must be either upper or lower
	"""
	if case == "lower":
		return(text.lower())
	if case == "upper":
		return(text.upper())
	else:
		print("argument not recognize, must be upper or lower")


# remove accent
def remove_accent(text):
	return(unidecode.unidecode(text))


# remove punctuations
def remove_punctuations(text):
	"""remove punctuations and letters with accent. So il is
	better to first replace letters with accent with non accent letters
	and then apply this function"""
	p1 = re.compile("[^1-9A-Za-z ]+(?=\s|$)")
	p2 = re.compile("(?<=\s)[^1-9A-Za-z ]+")
	new_text = p1.sub("", text)
	new_text = p2.sub("", new_text)
	return(new_text)


# remove inclusive writing --> remove punctuation if word match
# a inclusive writing pattern
def remove_inclusive_writing(text):
	patterns = ["s", "e", "trice", "tte", "elle", "le", "ne", "ere",
				"euse", "rice", "ive"]
	match_pattern = re.compile(".*[^1-9A-Za-z](" + "|".join([p for p in patterns]) + ")$")
	new_words = []
	for w in text.split(" "):
		if match_pattern.match(w):
			new_words.append(re.sub("[^1-9A-Za-z]", "", w))
		else:
			new_words.append(w)
	return(" ".join(new_words))


# split apostrophe
def split_punctuation(text):
	""" remove apostroph. ex : l'oiseau --> l oiseau"""
	"""split dash "c'est-a-dire" --> c'est a dire"""
	return(re.sub("(?<=\w)[^1-9A-Za-z ]+(?=\w)", " ", text))


# just remove all digits	
def remove_digits(text):
	p = re.compile("[0-9]")
	return(p.sub("", text))


# remove stop words
def remove_stopwords(text, language="french"):
	#nltk.download('stopwords')
	stopwords = nltk.corpus.stopwords.words(language)
	add_words = ['a', 'afin', 'ai', 'aie', 'aient', 'aies', 'ait',
	 'alors', 'apres', 'as', 'au', 'aucun', 'auquel', 'auquelle', 'aura',
	'aurai', 'auraient', 'aurais', 'aurait', 'auras', 'aurez', 'auriez',
	'aurions', 'aurons', 'auront', 'aussi', 'autre', 'autrui', 'aux',
	'auxquel', 'auxquelle', 'avaient', 'avais', 'avait', 'avant', 'avec',
	'avez', 'aviez', 'avions', 'avons', 'ayant', 'ayante', 'ayantes',
	'ayants', 'ayez', 'ayons', 'bien', 'c', 'car', 'cas', 'ce', 'ceci', 'cela',
	'celle', 'celui', 'cent', 'centieme', 'certain', 'certaine', 'ces', 'cet',
	'cette', 'ceux', 'chacun', 'chacune', 'chaque', 'chez', 'chose', 'ci',
	'cinq', 'cinquante', 'cinquantieme', 'cinquieme', 'comme', 'condition',
	'contre', 'cote', 'd', 'dans', 'de', 'dehors', 'dela', 'depuis',
	'derriere', 'des', 'desquel', 'desquelle', 'dessous', 'dessus', 'deux',
	'deuxieme', 'devant', 'different', 'divers', 'dix', 'dixieme', 'donc',
	'dont', 'douze', 'douzieme', 'droite', 'du', 'elle', 'en', 'entre',
	'envers', 'environ', 'es', 'est', 'et', 'etaient', 'etais', 'etait',
	'etant', 'etante', 'etantes', 'etants', 'ete', 'etee', 'etees', 'etes',
	'etes', 'etiez', 'etions', 'eu', 'eue', 'eues', 'eumes', 'eurent', 'eus',
	'eusse', 'eussent', 'eusses', 'eussiez', 'eussions', 'eut', 'eut',
	'eutes', 'eux', 'excepte', 'face', 'fait', 'fumes', 'furent', 'fus',
	'fusse', 'fussent', 'fusses', 'fussiez', 'fussions', 'fut', 'fut', 'futes',
	'gauche', 'grace', 'hors', 'huit', 'huitieme', 'hyper', 'il', 'ils',
	'importe', 'j', 'je', 'jusque', 'jusqu’q', 'l', 'la', 'laquel', 'laquelle',
	'le', 'lequel', 'lequelle', 'les', 'lesquel', 'lesquelle', 'leur',
	'loin', 'lorsque', 'lui', 'm', 'ma', 'maint', 'mais', 'malgre', 'me',
	'meilleur', 'meme', 'meme', 'mes', 'mien', 'mienne', 'mille', 'milliard',
	'milliardieme', 'millieme', 'million', 'millionieme', 'moi', 'moins',
	'moment', 'mon', 'n', 'ne', 'neuf', 'neuvieme', 'ni', 'nos', 'notre', 
	'nous', 'nul', 'nulle', 'on', 'ont', 'onze', 'onzieme', 'or', 'ou', 'par',
	'parce', 'parmi', 'pas', 'pendant', 'personne', 'pire', 'plupart', 'plus',
	'plusieur', 'pour', 'pourvu', 'premier', 'premiere', 'pres', 'puisque',
	'qinze', 'qu', 'quand', 'quarantieme', 'quatorze', 'quatorzieme', 'quatre',
	'quatrieme', 'que', 'quel', 'quelconque', 'quelle', 'quelqu', 'quelque',
	'qui', 'quinzieme', 'quoi', 'quoique', 'qurante', 'rien', 's', 'sa',
	'sans', 'sauf', 'se', 'second', 'seconde', 'seize', 'seizieme', 'selon',
	'sept', 'septieme', 'sera', 'serai', 'seraient', 'serais', 'serait',
	'seras', 'serez', 'seriez', 'serions', 'serons', 'seront', 'ses', 'si',
	'sien', 'sienne', 'six', 'sixieme', 'soi', 'soient', 'sois', 'soit',
	'soixante', 'soixantieme', 'sommes', 'son', 'sont', 'sorte', 'sous',
	'soyez', 'soyons', 'suis', 'super', 'supposer', 'sur', 't', 'ta',
	'tandis', 'tant', 'te', 'tel', 'telle', 'tes', 'tien', 'tienne', 'toi',
	'toisieme', 'ton', 'tous', 'tout', 'toute', 'travers', 'treize',
	'treizieme', 'trentieme', 'trentre', 'trois', 'tu', 'un', 'une', 'unieme',
	'untel', 'vers', 'vingt', 'vingtieme', 'vos', 'votre', 'vous', 'y',
	"toutes", "elles", "etc", "doit", "alors", "selon", "afin", "trop",
	"https", "http", "ans"]
	stopwords += add_words
	stopwords = [unidecode.unidecode(w) for w in stopwords]
	return(" ".join([w for w in text.split(" ") if w not in stopwords]))
	

# remove short words. We can set the limit length
def remove_short_words(text, length=2):
	return(" ".join([w for w in text.split(" ") if len(w)>length]))


# stemming
def stemming(text, language="french"):
	ss = nltk.SnowballStemmer(language)
	return(" ".join([ss.stem(w) for w in text.split(" ")]))


# lemmatization
def lemmatize(text):
	#nltk.download('wordnet')
	wn = nltk.WordNetLemmatizer()
	return(" ".join([wn.lemmatize(w) for w in text.split(" ")]))


# tokenization
def tokenization(text):
	#nltk.download('punkt')
	new_text = nltk.tokenize.word_tokenize(text)
	return(new_text)


# enfants --> enfant. search in a word dictionnary if the word
# except the last letter is matched if pattern like .+s$ or .+x$
# is matched. As we want to keep the contexte, we can't apply a re.findall
# and a transformation
def plural_to_singular(text):
	# as lookbehind requires fixed-width pattern we have to rewrite
	# (?<=\s|^)\w+(?=\s|$) as (?<!\S)\w+(?!\S) or just (?<!\S)\w+(?=\s|$)
	# patterns = [re.compile("(?<!\S)\w+" + p + "(?=\s|$)") for p in ["s", "x"]]
	try:
		with open(dico_path, "r") as f:
			dico = f.read().split(" ")
	except:
		dico = []
	match_pattern = re.compile(".+[sx]$")
	patterns = [re.compile(".+s$"), re.compile(".+x$")]
	new_words = []
	for w in text.split(" "):
		if match_pattern.match(w):
			for p in patterns:
				if p.match(w):
					#print("match plurial pattern for {}".format(w))
					if w[:-1] in dico:
						#print("remove the plurial of {}".format(w))
						new_words.append(w[:-1])
					else:
						#print("didn't remove the plurial of {}".format(w))
						new_words.append(w)
					break
				else:
					pass
		else:
			new_words.append(w)
	return(" ".join(new_words))



# libérée --> libéré. search in a word dictionnary if the word
# except the last letter except if pattern "ee$" is matched. So it
# works after having removed accent
def feminine_to_masculine(text):
	try:
		with open(dico_path, "r") as f:
			dico = f.read().split(" ")
	except:
		dico = []
	patterns = [("ee", "e"), ("ere", "er"), ("euse", "eur"), ("ive", "if"),
			("trice", "teur"), ("esse", "e"), ("ouse", "oux"), ("elle", "el"),
			("anne", "an"), ("ienne", "ien"), ("ionne", "ion"), ("te", "t"),
			("euse","eux"), ("euses","eux"), ("eille", "eil"), ("enne", "en")]
	match_pattern = re.compile(".+(" + "|".join([p[0] for p in patterns]) + ")$")
	new_words = []
	for w in text.split(" "):
		if match_pattern.match(w):
			for p in patterns:
				if re.match(".+" + p[0] + "$", w):
					masc_word = re.search("(.+)" + p[0] + "$", w).group(1) + p[1]
					if masc_word in dico:
						new_words.append(masc_word)
					else:
						new_words.append(w)
					break
				else:
					pass
		else:
			new_words.append(w)
	return(" ".join(new_words))


# PIPELINE
# clean a text
def text_cleaner(text, stemm=False):
	text = remove_dash_for_linebreak(text)
	#text = remove_linebreak(text)
	text = remove_extra_whitespace(text) # already remove linebreaks
	text = normalization(text, case="lower")
	text = remove_accent(text)
	text = remove_punctuations(text)
	text = remove_inclusive_writing(text)
	text = split_punctuation(text)
	text = remove_digits(text)
	text = remove_short_words(text)
	text = remove_stopwords(text, language="french")
	#text = stemming(text)
	text = plural_to_singular(text)
	text = feminine_to_masculine(text)
	if stemm:
		text = stemming(text)
	return(text)



# EXAMPLE
def example():
	with open("example.txt", "r") as f:
		text = f.read()
	res = text_cleaner(text)
	print("Before :")
	print(text)
	print("After :")
	print(res)
	return(res)

#example()
