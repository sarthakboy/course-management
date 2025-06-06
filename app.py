from flask import Flask, request, jsonify
from model import db, User, Course
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({'message': 'Invalid credentials'}), 401
    if user.role == 'admin':
        return jsonify({'message': 'Login successful', 'redirect': '/addcourse'}), 200
    else:
        return jsonify({'message': 'Login successful', 'redirect': '/course/enroll'}), 200

@app.route('/course/add', methods=['POST'])
def add_course():
    data = request.get_json()
    name = data.get('name')
    duration = data.get('duration')
    description = data.get('description')
    new_course = Course(name=name, duration=duration, description=description)
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course added successfully'}), 201

@app.route('/course/enroll', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name, 'duration': course.duration, 'description': course.description} for course in courses]), 200

if __name__ == '__main__':
    app.run(debug=True)
