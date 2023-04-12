from datetime import datetime
import requests
from flask import render_template, request, flash, redirect, url_for, Flask, session, abort
from src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from src.Backend.DAO.Matrix import MatrixDAO
from src.Backend.DAO.Users import UserDAO
from src.Backend.History import History
from src.FlaskPreparation.Add import add
from src.FlaskPreparation.divide import divide
from src.FlaskPreparation.multiply import multiply
from src.FlaskPreparation.power import power
from src.FlaskPreparation.substract import substract
from src.MatrixOperation.LinearSystem.SystemInserting import insertLinearSystem
from src.Views.UI.MatrixUI import MatrixUI

app = Flask(__name__)
app.secret_key = '5tmw6m9672'
app.config['SESSION_TYPE'] = 'filesystem'
s = requests.Session()
user = UserDAO()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user.get_user_by_username(username)
        user.get_user_by_username(username)
        if user is not None and user.password == password:
            session['username'] = username
            user.logged = True
            session['userID'] = user.get_userID()
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        email = request.form.get("email")
        if password != confirm_password:
            error = 'Passwords do not match. Please try again.'
        else:
            date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.insert_user(username, password, email, date_created)
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    user.logged = False
    return redirect(url_for('login'))


@app.route("/history", methods=['GET', 'POST'])
def history():
    return render_template('/history.html')


@app.route("/matrix-history", methods=['GET', 'POST'])
def matrixHistory():
    userHistory = History()
    userID = session.get('userID')
    data = userHistory.getMatrixDataByUser(userID)

    # sort data_dict based on DateCreated field in reverse chronological order
    sorted_data = sorted(data.items(), key=lambda x: x[1]["DateCreated"], reverse=True)

    # render HTML template with sorted data
    return render_template('/matrixHistory.html', sorted_data=sorted_data)


@app.route("/calc-matrix-history", methods=['GET', 'POST'])
def calcMatrixHistory():
    userHistory = History()
    userID = session.get('userID')
    data = userHistory.getCalcMatrixDataByUser(userID)
    # sort data_dict based on DateCreated field in reverse chronological order
    sorted_data = sorted((item for item in data.items() if item[1]["DateCreated"] is not None),
                         key=lambda x: x[1]["DateCreated"], reverse=True)
    # render HTML template with sorted data
    return render_template('/calcMatrixHistory.html', sorted_data=sorted_data)


@app.route("/systems-history", methods=['GET', 'POST'])
def systemHistory():
    userHistory = History()
    userID = session.get('userID')
    data, equations, solutions = userHistory.linearSystemHistory(userID)

    return render_template('/systemHistory.html', data=data, equations=equations, solutions=solutions)


ui = MatrixUI()


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input
        rows = request.form.get("rows")
        cols = request.form.get("cols")
        data = request.form.get("data")

        # Validate user input
        if not rows.isdigit() or not cols.isdigit():
            flash("Invalid input: Rows and columns must be positive integers", "error")
        else:
            rows = int(rows)
            cols = int(cols)
            matrix_data = [[int(val) for val in row.split()] for row in data.split('\n')]
            if any(len(row) != cols for row in matrix_data):
                flash("Invalid input: Each row must have the same number of values", "error")
            else:
                # Create and insert matrix into database
                created_matrix = ui.create_matrix(rows, cols, matrix_data)
                userID = session.get("userID")
                matrixDB = MatrixDAO(created_matrix, userID)
                matrixDB.insert_matrix()
                session['matrixID'] = matrixDB.matrixID
                session['matrix'] = created_matrix.serialize_matrix()
                # Return a message and redirect to home page
                flash("Matrix created successfully", "success")

    matrix = session.get("matrix")
    return render_template("/home.html", matrix=matrix)


@app.route("/matrix/<operation>")
def matrix_operation(operation):
    templates = {
        "add": "add_matrix.html",
        "subtract": "subtract_matrix.html",
        "multiply": "multiply_matrix.html",
        "divide": "divide_matrix.html",
        "power": "power_matrix.html",
    }
    if operation in templates:
        return render_template(templates[operation])
    else:
        abort(404)


@app.route("/add-matrix", methods=["POST"])
def add_matrix():
    if request.method == "POST":
        rows = int(request.form.get("rows"))
        cols = int(request.form.get("cols"))
        data = request.form.get("data")

        matrixID = session.get('matrixID')
        matrix = session.get('matrix')
        session['added_matrix'], added_matrix = add(rows=rows, cols=cols, data=data, origin_matrix=matrix,
                                                    matrixID=matrixID)

        flash("Matrix added successfully", "success")
        return render_template("add_matrix.html", added_matrix=added_matrix)


@app.route("/subtract-matrix", methods=["POST"])
def subtract_matrix():
    if request.method == "POST":
        rows = int(request.form.get("rows"))
        cols = int(request.form.get("cols"))
        data = request.form.get("data")

        matrix = session.get('matrix')
        matrixID = session.get('matrixID')

        session['subtract_matrix'], subtracted_matrix = substract(rows, cols, data, matrix, matrixID)

        flash("Matrix added successfully", "success")
        return render_template("subtract_matrix.html", subtract_matrix=subtracted_matrix)


@app.route("/multiply_matrix", methods=["POST"])
def multiply_matrix():
    if request.method == "POST":
        rows = int(request.form.get("rows"))
        cols = int(request.form.get("cols"))
        data = request.form.get("data")

        matrix = session.get('matrix')
        matrixID = session.get("matrixID")
        session['subtract_matrix'], matrix_mul = multiply(rows, cols, data, matrix, matrixID)

        flash("Matrix added successfully", "success")
        return render_template("multiply_matrix.html", multiply_matrix=matrix_mul)


@app.route("/divide-matrix", methods=["POST"])
def divide_matrix():
    if request.method == "POST":
        divisor = int(request.form.get("divisor"))
        matrix = session.get('matrix')
        matrixID = session.get('matrixID')
        matrix_divided = divide(matrix, divisor, matrixID)
        flash("Matrix divided successfully", "success")
        return render_template("divide_matrix.html", divide_matrix=matrix_divided)


@app.route("/power-matrix", methods=["POST"])
def power_matrix():
    if request.method == "POST":
        exponent = int(request.form.get("exponent"))
        matrix = session.get('matrix')
        matrixID = session.get('matrixID')
        matrix_powered = power(matrix, exponent, matrixID)
        flash("Matrix powered successfully", "success")
        return render_template("power_matrix.html", matrix_powered=matrix_powered)


@app.route("/display-matrix", methods=["GET"])
def display_matrix():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
    return render_template("matrix.html", matrix=matrix)


@app.route("/display-shape", methods=["GET"])
def display_shape():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        shape = matrix.shape()
        shape_str = f"{shape[0]} rows by {shape[1]} columns"
    else:
        shape_str = "Matrix not found"
    return render_template("home.html", matrix=matrix, shape_str=shape_str)


@app.route("/display-rank", methods=["GET"])
def display_rank():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        rank = ui.matrix_rank(matrix)
    else:
        rank = "Matrix not found"
    return render_template("home.html", matrix=matrix, rank=rank)


@app.route("/display-determinant", methods=["GET"])
def display_determinant():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        determinant = ui.matrix_determinant(matrix)
    else:
        determinant = "Matrix not found"
    return render_template("home.html", matrix=matrix, determinate=determinant)


@app.route("/display-inverse", methods=["GET"])
def display_inverse():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        matrix = matrix.inverse()
    else:
        matrix = "Matrix not found"
    return render_template("matrix.html", matrix=matrix)


@app.route("/display-transpose", methods=["GET"])
def display_transpose():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        matrix = matrix.transpose()
    else:
        matrix = "Matrix not found"
    return render_template("matrix.html", matrix=matrix)


@app.route("/linear-system", methods=["GET", "POST"])
def linear_system():
    global solution
    userID = session.get('userID')
    if request.method == 'POST':
        equations_str = request.form['equations']
        solution = insertLinearSystem(equations_str, userID)
        return render_template('linear_equation.html', solution=solution)
    return render_template('linear_equation.html')


@app.route("/argmax", methods=["GET", "POST"])
def argmax():
    matrix = session.get('matrix')
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        max_inx = matrix.argmax()
        max_val = matrix[max_inx[0]][max_inx[1]]
    else:
        max_inx = "Matrix not found"
        max_val = "None"
    return render_template('home.html', matrix=matrix, max_inx=max_inx, max_val=max_val)


@app.route("/zeros", methods=["GET", "POST"])
def zeros():
    matrix = session.get("matrix")
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        zero_matrix = matrix.zeros()
        session["matrix"] = ui.create_matrix(zero_matrix.rows, zero_matrix.cols, zero_matrix.matrix).serialize_matrix()
    return redirect(url_for('home'))


@app.route("/identity", methods=["GET", "POST"])
def identity():
    matrix = session.get("matrix")
    if matrix is not None:
        matrix = ui.deserialize_matrix(matrix)
        identity_matrix = matrix.identity()
        session["matrix"] = ui.create_matrix(identity_matrix.rows, identity_matrix.cols,
                                             identity_matrix.matrix).serialize_matrix()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
