INDEX_SETTINGS = {
    "settings": {
        "analysis": {
            "analyzer": {
                "default": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "standard",
                        "lowercase",
                        "stop",
                        "kstem",
                        "ngram"
                    ]
                }
            },
            "filter": {
                "ngram": {
                    "type": "ngram",
                    "min_gram": 2,
                    "max_gram": 15
                }
            }
        }
    }
}
