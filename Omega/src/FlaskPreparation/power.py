from Omega.src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from Omega.src.Views.UI.MatrixUI import MatrixUI


def power(origin_matrix, exponent, matrixID):
    try:
        ui = MatrixUI()
        matrix = ui.deserialize_matrix(origin_matrix)
        matrix_powered = matrix.pow(exponent)
        calcMatrixDB = CalculatedMatrixDAO(matrix_powered, '^', matrixID)
        calcMatrixDB.insert_calculated_matrix()
        return matrix_powered
    except Exception as e:
        print("Error: ", str(e))
        return None, None
