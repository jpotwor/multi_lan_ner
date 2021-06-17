import spacy

def find_entities(intput, language):
  models = {
      'en': 'en_core_web_sm',
      'pl': 'pl_core_news_sm',
      'fr': 'fr_core_news_sm',
      'de': 'de_core_news_sm',
      'it': 'it_core_news_sm',
  }

  if language in models:
    nlp = spacy.load(models[language])
    res = []
    for ent in doc.ents:
      res.append({'text': ent.text, 'start_pos': ent.start_char, 'end_pos': ent.end_char, 'type': ent.label_})
      return res
  else:
    raise FileNotFoundError('model %s not found, please download' % language)


print(find_entities("Apple is looking at buying U.K. startup for $1 billion", 'en'))