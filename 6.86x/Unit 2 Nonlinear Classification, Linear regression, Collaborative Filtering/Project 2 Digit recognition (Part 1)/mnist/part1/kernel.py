import numpy as np

### Functions for you to fill in ###

# pragma: coderesponse template


def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    return (X @ Y.T + c)**p


# pragma: coderesponse end

# pragma: coderesponse template

def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    # for every data point, compute its norm, then compute the distance
    distance = np.sum(X**2, 1).reshape(X.shape[0], 1) + np.sum(Y**2, 1) - 2 * X @ Y.T
    return np.exp(-gamma * distance)

# pragma: coderesponse end


def augment_feature_vector(X):
    column_of_ones = np.zeros([len(X), 1]) + 1
    return np.hstack((column_of_ones, X))


def kn_prob(kernel, x_example, X, alpha, temp_parameter, **kwargs):
    kn = kernel(x_example, X, **kwargs)
    mat_tmp = alpha @ kn / temp_parameter
    c = mat_tmp.max(0)
    softmax_func = np.e ** (mat_tmp - c) / np.sum(np.e ** (mat_tmp - c), 0)
    return softmax_func


def kn_cost(kernel, x_example, X, Y, alpha, lambda_factor, temp_parameter, **kwargs):
    n_data = X.shape[0]
    k_para = alpha.shape[0]
    correct = np.zeros([k_para, n_data])
    for i in range(n_data): # iterate through all data
        correct[Y[i]][i] = 1 # set the 'label' th row in i col to 1
    clipped_probs = np.clip(kn_prob(kernel, x_example, X, alpha, temp_parameter, **kwargs), 1e-15, 1-1e-15)
    loss = -1 / n_data * np.sum(correct * np.log(clipped_probs))
    regularization = lambda_factor/2 * np.sum(alpha**2)
    return loss + regularization


def run_gradient_descent_iteration(kernel, x_example, X, Y, alpha, eta, lambda_factor, temp_parameter, **kwargs):
    n_data = X.shape[0]
    k_para = alpha.shape[0]
    # get the matrix with correct entry = 1 and others = 0
    correct = np.zeros([k_para, n_data])
    for i in range(n_data): # iterate through all data
        correct[Y[i]][i] = 1 # set the 'label'th row in i col to 1
    clipped_probs = np.clip(kn_prob(kernel, X, X, alpha, temp_parameter, **kwargs), 1e-15, 1-1e-15)
    kn = kernel(x_example, X, **kwargs)
    grad = -1 / (n_data * temp_parameter) * (correct - clipped_probs) @ kn + lambda_factor * alpha
    return alpha - eta * grad

# pragma: coderesponse end


def kn_softmax_regression(kernel, X, Y, temp_parameter, eta, lambda_factor, k, num_iterations, **kwargs):
    X = augment_feature_vector(X)
    alpha = np.zeros([k, X.shape[1]])
    cost_function_progression = []
    for i in range(num_iterations):
        cost_function_progression.append(kn_cost(kernel, X, X, Y, alpha, lambda_factor, temp_parameter, **kwargs))
        alpha = run_gradient_descent_iteration(kernel, X, X, Y, alpha, eta, lambda_factor, temp_parameter, **kwargs)
    return alpha, cost_function_progression

