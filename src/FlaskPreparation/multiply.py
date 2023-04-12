from src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from src.Views.UI.MatrixUI import MatrixUI


def multiply(rows, cols, data, origin_matrix, matrixID):
    try:
        ui = MatrixUI()
        matrix_data = [[int(val) for val in row.split()] for row in data.split('\n')]
        matrix_m = ui.create_matrix(rows=rows, cols=cols, matrix_data=matrix_data)
        session_matrix = matrix_m.serialize_matrix()
        matrix = ui.deserialize_matrix(origin_matrix)
        multiplied_matrix = matrix @ matrix_m
        calcMatrixDB = CalculatedMatrixDAO(multiplied_matrix, '@', matrixID)
        calcMatrixDB.insert_calculated_matrix()
        return session_matrix, multiplied_matrix
    except Exception as e:
        print("Error: ", str(e))
        return None, None
