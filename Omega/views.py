from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, session, abort
from Omega.src.Backend.DAO.Matrix import MatrixDAO
from Omega.src.Backend.History import History
from Omega.src.FlaskPreparation.Add import add
from Omega.src.FlaskPreparation.divide import divide
from Omega.src.FlaskPreparation.multiply import multiply
from Omega.src.FlaskPreparation.power import power
from Omega.src.FlaskPreparation.scalar import multiplied_scalar
from Omega.src.FlaskPreparation.substract import substract
from Omega.src.MatrixOperation.LinearSystem.SystemInserting import insertLinearSystem
from Omega.src.Views.UI.MatrixUI import MatrixUI

from Omega import app, user


@app.route('/', methods=['GET', 'POST'])
def login():
    try:
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
    except Exception as e:
        return render_template('error.html', error=str(e))


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
    try:
        data = userHistory.getMatrixDataByUser(userID)
        print(data)
        # sort data_dict based on DateCreated field in reverse chronological order
        sorted_data = sorted(data.items(), key=lambda x: x[1]["DateCreated"], reverse=True)

        # render HTML template with sorted data
        return render_template('/matrixHistory.html', sorted_data=sorted_data)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/calc-matrix-history", methods=['GET', 'POST'])
def calcMatrixHistory():
    userHistory = History()
    userID = session.get('userID')
    try:
        data = userHistory.getCalcMatrixDataByUser(userID)
        # sort data_dict based on DateCreated field in reverse chronological order
        sorted_data = sorted((item for item in data.items() if item[1]["DateCreated"] is not None),
                             key=lambda x: x[1]["DateCreated"], reverse=True)
        # render HTML template with sorted data
        print(sorted_data)
        return render_template('/calcMatrixHistory.html', sorted_data=sorted_data)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/systems-history", methods=['GET', 'POST'])
def systemHistory():
    userHistory = History()
    userID = session.get('userID')
    try:
        data, equations, solutions = userHistory.linearSystemHistory(userID)

        return render_template('/systemHistory.html', data=data, equations=equations, solutions=solutions)
    except Exception as e:
        return render_template('error.html', error=str(e))


ui = MatrixUI()


@app.route("/home", methods=["GET", "POST"])
def home():
    try:
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
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/matrix/<operation>")
def matrix_operation(operation):
    templates = {
        "add": "add_matrix.html",
        "subtract": "subtract_matrix.html",
        "multiply": "multiply_matrix.html",
        "divide": "divide_matrix.html",
        "power": "power_matrix.html",
        "scalar": "scalar_matrix.html"
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
        try:
            session['added_matrix'], added_matrix = add(rows=rows, cols=cols, data=data, origin_matrix=matrix,
                                                        matrixID=matrixID)

            flash("Matrix added successfully", "success")
            return render_template("add_matrix.html", added_matrix=added_matrix)
        except Exception as e:
            return render_template('error.html', error=str(e))


@app.route("/subtract-matrix", methods=["POST"])
def subtract_matrix():
    if request.method == "POST":
        rows = int(request.form.get("rows"))
        cols = int(request.form.get("cols"))
        data = request.form.get("data")

        matrix = session.get('matrix')
        matrixID = session.get('matrixID')
        try:
            session['subtract_matrix'], subtracted_matrix = substract(rows, cols, data, matrix, matrixID)

            flash("Matrix added successfully", "success")
            return render_template("subtract_matrix.html", subtract_matrix=subtracted_matrix)
        except Exception as e:
            return render_template('error.html', error=str(e))


@app.route("/multiply_matrix", methods=["POST"])
def multiply_matrix():
    if request.method == "POST":
        rows = int(request.form.get("rows"))
        cols = int(request.form.get("cols"))
        data = request.form.get("data")

        matrix = session.get('matrix')
        matrixID = session.get("matrixID")
        try:
            session['subtract_matrix'], matrix_mul = multiply(rows, cols, data, matrix, matrixID)

            flash("Matrix added successfully", "success")
            return render_template("multiply_matrix.html", multiply_matrix=matrix_mul)
        except Exception as e:
            return render_template('error.html', error=str(e))


@app.route("/divide-matrix", methods=["POST"])
def divide_matrix():
    if request.method == "POST":
        try:
            divisor = int(request.form.get("divisor"))
            matrix = session.get('matrix')
            matrixID = session.get('matrixID')
            matrix_divided = divide(matrix, divisor, matrixID)
            flash("Matrix divided successfully", "success")
            return render_template("divide_matrix.html", divide_matrix=matrix_divided)
        except Exception as e:
            return render_template('error.html', error=str(e))


@app.route("/power-matrix", methods=["POST"])
def power_matrix():
    if request.method == "POST":
        try:
            exponent = int(request.form.get("exponent"))
            matrix = session.get('matrix')
            matrixID = session.get('matrixID')
            matrix_powered = power(matrix, exponent, matrixID)
            flash("Matrix powered successfully", "success")
            return render_template("power_matrix.html", matrix_powered=matrix_powered)
        except Exception as e:
            return render_template('error.html', error=str(e))


@app.route("/linear-system", methods=["GET", "POST"])
def linear_system():
    global solution
    userID = session.get('userID')
    if request.method == 'POST':
        equations_str = request.form['equations']
        try:
            solution = insertLinearSystem(equations_str, userID)
            return render_template('linear_equation.html', solution=solution)
        except Exception as e:
            return render_template('error.html', error=str(e))
    return render_template('linear_equation.html')


@app.route("/argmax", methods=["GET", "POST"])
def argmax():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        max_inx = matrix.argmax()
        max_val = matrix[max_inx[0]][max_inx[1]]
        return render_template('home.html', matrix=matrix, max_inx=max_inx, max_val=max_val)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/zeros", methods=["GET", "POST"])
def zeros():
    matrix = session.get("matrix")
    try:
        matrix = ui.deserialize_matrix(matrix)
        zero_matrix = matrix.zeros()
        session["matrix"] = ui.create_matrix(zero_matrix.rows, zero_matrix.cols,
                                             zero_matrix.matrix).serialize_matrix()
        return redirect(url_for('home'))
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/identity", methods=["GET", "POST"])
def identity():
    matrix = session.get("matrix")
    try:
        matrix = ui.deserialize_matrix(matrix)
        identity_matrix = matrix.identity(matrix.rows)
        session["matrix"] = ui.create_matrix(identity_matrix.rows, identity_matrix.cols,
                                             identity_matrix.matrix).serialize_matrix()
        return redirect(url_for('home'))
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/multiply-by-scalar", methods=["GET", "POST"])
def multiply_by_scalar():
    if request.method == "POST":
        scalar = int(request.form.get("scalar"))
        matrix = session.get('matrix')
        matrixID = session.get('matrixID')
        try:
            matrix_multiplied = multiplied_scalar(matrix, scalar, matrixID)
            flash("Matrix multiplied by scalar successfully", "success")
            return render_template("scalar_matrix.html", scalar_matrix=matrix_multiplied)
        except Exception as e:
            return render_template('error.html', error=str(e))
