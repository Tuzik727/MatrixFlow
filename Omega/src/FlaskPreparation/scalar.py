from Omega.src.Backend.DAO.CalculatedMatrix import CalculatedMatrixDAO
from Omega.src.Views.UI.MatrixUI import MatrixUI


def multiplied_scalar(origin_matrix, scalar, matrixID):
    try:
        ui = MatrixUI()
        matrix = ui.deserialize_matrix(origin_matrix)
        matrix_multiplied = matrix * scalar
        calcMatrixDB = CalculatedMatrixDAO(matrix_multiplied, '*', matrixID)
        calcMatrixDB.insert_calculated_matrix()
        return matrix_multiplied
    except Exception as e:
        print("Error: ", str(e))
        return None, None
