from Omega.src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from Omega.src.Views.UI.MatrixUI import MatrixUI


def divide(origin_matrix, divisor, matrixID):
    try:
        ui = MatrixUI()
        matrix = ui.deserialize_matrix(origin_matrix)
        matrix_divided = matrix / divisor
        calcMatrixDB = CalculatedMatrixDAO(matrix_divided, '/', matrixID)
        calcMatrixDB.insert_calculated_matrix()
        return matrix_divided
    except Exception as e:
        print("Error: ", str(e))
        return None, None
