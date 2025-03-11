# -- START OF YOUR CODERUNNER SUBMISSION CODE
import numpy as np
from scipy.optimize import linprog
from dhCheck_Task3 import dhCheckCorrectness

def Task3(x, y, z, x_initial, c, x_bound, se_bound, ml_bound):
    x = np.array(x).T
    y = np.array(y)
    z = np.array(z)
    x_initial = np.array(x_initial)
    c = np.array(c)
    x_bound = np.array(x_bound)
    n = len(x)
    X_design = np.hstack([np.ones((n, 1)), x])
    b, _, _, _ = np.linalg.lstsq(X_design, y, rcond=None)
    weights_b = b
    d, _, _, _ = np.linalg.lstsq(X_design, z, rcond=None)
    weights_d = d
    current_y = weights_b[0] + np.dot(weights_b[1:], x_initial)
    current_z = weights_d[0] + np.dot(weights_d[1:], x_initial)
    A_ub = np.vstack([weights_d[1:], -weights_b[1:]])
    b_ub = np.array([ml_bound - current_z, -(se_bound - current_y)])
    c_obj = c
    ub = np.maximum(0, x_bound - x_initial)
    bounds = [(0, ub_i) for ub_i in ub]
    result = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    x_add = result.x
    return (weights_b, weights_d, x_add)

# -- END OF YOUR CODERUNNER SUBMISSION CODE
