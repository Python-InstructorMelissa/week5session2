from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.flight import Flight  # This line is needed for our join statement at the end


class Airline:
    db = 'aircorp'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.headquarters = data['headquarters']
        self.locations = data['locations']
        self.workers = data['workers']
        self.planes = data['planes']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']


    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM airline;'
        results = connectToMySQL(cls.db).query_db(query)
        airlines = []
        for row in results:
            airlines.append(cls(row))
        return airlines

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM airline WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO airline (name, headquarters, locations, workers, planes) VALUES (%(name)s, %(headquarters)s, %(locations)s, %(workers)s, %(planes)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE airline SET name=%(name)s, headquarters=%(headquarters)s, locations=%(locations)s, workers=%(workers)s, planes=%(planes)s WHERE id= %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM airline WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def allFlights(cls, data):
        # left join statement will go here
        # get 1 airline and all its flights
        pass