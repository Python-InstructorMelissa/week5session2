from app.config.mysqlconnection import connectToMySQL

class Course:
    db_name = "week5"
    result = connectToMySQL('week5')
    def __init__(self, data):
        self.id = data['id']
        self.courseName = data['courseName']
        self.courseDesc = data['courseDesc']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM courses;"
        results_from_db = connectToMySQL(cls.db_name).query_db(query)

        allCourses = []
        for row in results_from_db:
            course = cls(row)
            allCourses.append(course)
        # print(allCourses)
        # print(course.__dict__)
        return allCourses

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM courses WHERE id = %(id)s;"
        theResult = cls.result.query_db(query, data)
        return cls(theResult[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO courses (courseName, courseDesc) VALUES (%(courseName)s, %(courseDesc)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE courses SET courseName=%(courseName)s, courseDesc=%(courseDesc)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM courses WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)