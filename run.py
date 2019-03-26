from app import app, db, cli
from app.search import add_to_index , remove_from_index , query_index
from app.models import City, Restaurant , Fifa

cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Restaurant': Restaurant, 'City': City , 'Fifa' : Fifa}
# if __name__=='__main__':
#     app.run(host='0.0.0.0', port=80)
