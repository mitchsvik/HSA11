"""Search for a word in ES index"""
import sys

import elasticsearch


def search_word(es_client, search_word):
    search_word = search_word.upper()
    if len(search_word) < 7:
        search_query = {
            "query": {
                "match": {
                    "word.autocomplete": search_word
                }
            }
        }
    else:
        search_query = {
            "query": {
                "bool": {
                    "must": [
                        { "match": {
                            "word.autocomplete": { "query": search_word }}
                        },
                        {"script": {
                                "script": {
                                    "source": "doc['word.keyword'].value.length() >= 7"
                                }
                            }
                        }
                    ]
                }
            }
        }

    resp = es_client.search(index='hsa11_dictionary', body=search_query)
    hits = resp['hits']['hits']
    for hit in hits:
        print(hit['_source']['word'], end='')


if __name__ == '__main__':
    es = elasticsearch.Elasticsearch(hosts='http://0.0.0.0:9200')
    argv = sys.argv[1:]

    if not argv:
        raise Exception('Search word is required')

    search_word(es, argv[0])
