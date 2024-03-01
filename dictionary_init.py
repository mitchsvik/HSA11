"""Init elasticsearch dictionary"""

import elasticsearch


DICTIONARY = './common_words.txt'

index_body = {
    "settings": {
        "analysis": {
            "analyzer": {
                "custom_analyzer": {
                    "type": "custom",
                    "tokenizer": "ngram_tokenizer",
                    "filter": ["uppercase"]
                }
            },
            "tokenizer": {
                "ngram_tokenizer": {
                    "type": "edge_ngram",
                    "min_gram": 1,
                    "max_gram": 20,
                    "token_chars": ["letter", "digit"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "word": {
                "type": "text",
                "fields": {
                    "autocomplete": {
                        "type": "text",
                        "analyzer": "custom_analyzer"
                    },
                    "keyword": {
                        "type": "keyword"
                    }
                }
            }
        }
    }
}


es = elasticsearch.Elasticsearch(hosts='http://0.0.0.0:9200')

with open(DICTIONARY, 'r') as dictionary:
    es.indices.create(index='hsa11_dictionary', body=index_body)
    for line in dictionary:
        es.index(index='hsa11_dictionary', body={'word': line})
