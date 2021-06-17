def find_entities(input_phrase, language):
  models = {
      'en': 'en_core_web_sm',
      'pl': 'pl_core_news_sm',
      'fr': 'fr_core_news_sm',
      'de': 'de_core_news_sm',
      'it': 'it_core_news_sm',
  }

  if language in models:
    nlp = spacy.load(models[language])
    doc = nlp(input_phrase)
    res = []
    for ent in doc.ents:
      res.append({'text': ent.text, 'start_pos': ent.start_char, 'end_pos': ent.end_char, 'type': ent.label_})
    return res
  else:
    raise FileNotFoundError('model %s not found, please download' % language)

if __name__ == "__main__":
    print(find_entities("As I had only one hour to write this on my old Dell computer, I am aware there is space for improvement.", 'en'))