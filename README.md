# multi_lan_ner
Multi language named entity recognition based on spacy.

## Installation
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download pl_core_news_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm
python -m spacy download it_core_news_sm

## Usage

```python
from multi_lan_ner import find_entities

entities = find_entities("As I had only one hour to write this on my old Dell computer, I am aware there is space for improvement.", 'en')
```

## Contributing
As I had only one hour for this I am aware there is space for improvement.
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
