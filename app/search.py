from flask import current_app

def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id,
                                    body=payload)

def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)

def query_index(index,doc_type, query , search_field):
    if not current_app.elasticsearch:
        return  'current app elastic search not configured'
    search = current_app.elasticsearch.search(
        index=index, doc_type=doc_type,
        body={'query': {'match': {search_field: query}}})
    player_details = [(hit['_source']) for hit in search['hits']['hits']]
    all_players = search['hits']['hits']
    return player_details, search['hits']['total']
    
    
