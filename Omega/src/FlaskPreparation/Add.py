from Omega.src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from Omega.src.Views.UI.MatrixUI import MatrixUI


def add(rows, cols, data, origin_matrix, matrixID):
    try:
        ui = MatrixUI()
        matrix_data = [[int(val) for val in row.split()] for row in data.split('\n')]
        matrix_add = ui.create_matrix(rows=rows, cols=cols, matrix_data=matrix_data)
        session_matrix = matrix_add.serialize_matrix()
        matrix = ui.deserialize_matrix(origin_matrix)
        added_matrix = matrix + matrix_add
        calcMatrixDB = CalculatedMatrixDAO(added_matrix, '+', matrixID)
        calcMatrixDB.insert_calculated_matrix()
        return session_matrix, added_matrix
    except Exception as e:
        print("Error: ", str(e))
        return None, None
