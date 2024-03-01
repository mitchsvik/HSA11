# HSA11
Index & Autocomplete

This example contains elasticsearch claster with 3 container and kibana container

### Autocomplete dictionary

To prepare autocomple we need to process a dictionary of common words `common_words.txt` with `python dictionary_init.py`


### Autocomplete

To make autocomplete that can leverage typos and errors, this example utilizes [Edge n-gram tokenizer](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-edgengram-tokenizer.html) with a set up of min length 1 and max length 20


### Search

To search for a word in the index call command `search.py <word>`

```
python search.py scholar
scholar
scholarship
school
scheme
schedule
scared
scream
screen
script
scandal

```
