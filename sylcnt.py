from nltk.corpus import cmudict
import re
d = cmudict.dict()
pat = re.compile(r"/[aiouy]+e*|e(?!d$|ly).|[td]ed|le$/g")
def nsyl(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except:
        return [0]
def gsyl(word):
    return len(pat.findall(word))
