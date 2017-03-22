import numpy as np
#INFO = [Name, Age, ...]
INFO = np.array([None, None, None, None, None, None, None])
GREETING = np.array(['hello', 'hi', 'hey', 'sup', 'yo'])
NOUN = np.array([])
PRONOUN = np.array(['I', 'you', 'it'])
VERB = np.array([])
BEVERB = np.array(['be', 'am', 'is', 'are'])
ADJ = np.array([])
ADV = np.array([])
PREP = np.array([])
# CONJ = np.array([])
# INTERJ = np.array([])
ARTICLE = np.array(['a', 'an', 'the'])
INTERRO = np.array(['what', 'who', 'where', 'when', 'why', 'how'])
OTHER = ['aaaaa']

np.save("dataset/info", INFO)
np.save("dataset/greeting", GREETING)
np.save("dataset/pronoun", PRONOUN)
np.save("dataset/beverb", BEVERB)
np.save("dataset/article", ARTICLE)
np.save("dataset/interro", INTERRO)
np.save("dataset/other", OTHER)
