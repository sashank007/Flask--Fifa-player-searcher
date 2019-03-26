from app import db
from app.search import add_to_index, remove_from_index, query_index

class SearchableMixin(object):
    @classmethod
    def search(cls, expression , to_search):
        __doctype__=cls.__tablename__
        if cls.__tablename__=='fifa':
            __doctype__='fifa_players'
        ids, total = query_index(cls.__tablename__, __doctype__,expression , to_search)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

class City(SearchableMixin, db.Model):
    __searchable__ = ['name']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(120))
    restaurants = db.relationship('Restaurant' , backref='restaurant' , lazy='dynamic')

    def __repr__(self):
        return '<City {}>'.format(self.name)    

class Restaurant(SearchableMixin,db.Model):
    __searchable__ = ['name']
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    state=db.Column(db.String(120))
    city_name =  db.Column(db.String(140), db.ForeignKey('city.id'))


    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)

class Fifa(SearchableMixin,db.Model):
    __searchable__ = ['id', 'name' , 'age' ,'photo', 'nationality' , 'flag','overall','potential', 'club']
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(64))
    age=db.Column(db.Integer)
    photo = db.Column(db.String(140))
    nationality=db.Column(db.String(140))
    flag=db.Column(db.String(140))
    overall =  db.Column(db.Integer)
    potential=db.Column(db.Integer)
    club  = db.Column(db.String(120))

    def __repr__(self):
        return '<Club {}>'.format(self.name)

