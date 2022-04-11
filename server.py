from flask_app import app
from flask_app.controllers import subjects, cohorts # Add any new controller files to this line as you make and code them

if __name__ ==  "__main__":
    app.run(debug=True)