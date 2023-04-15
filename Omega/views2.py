from flask import session, render_template

from Omega import app
from Omega.views import ui


@app.route("/display-matrix", methods=["GET"])
def display_matrix():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        return render_template("matrix.html", matrix=matrix)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/display-shape", methods=["GET"])
def display_shape():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        shape = matrix.shape()
        shape_str = f"{shape[0]} rows by {shape[1]} columns"
        return render_template("home.html", matrix=matrix, shape_str=shape_str)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/display-rank", methods=["GET"])
def display_rank():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        rank = ui.matrix_rank(matrix)

        return render_template("home.html", matrix=matrix, rank=rank)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/display-determinant", methods=["GET"])
def display_determinant():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        determinant = ui.matrix_determinant(matrix)

        return render_template("home.html", matrix=matrix, determinate=determinant)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/display-inverse", methods=["GET"])
def display_inverse():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        matrix = matrix.inverse()

        return render_template("matrix.html", matrix=matrix)
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route("/display-transpose", methods=["GET"])
def display_transpose():
    matrix = session.get('matrix')
    try:
        matrix = ui.deserialize_matrix(matrix)
        matrix = matrix.transpose()

        return render_template("matrix.html", matrix=matrix)
    except Exception as e:
        return render_template('error.html', error=str(e))
