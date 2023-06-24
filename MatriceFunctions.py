import numpy as np

def covariance_matrix(x_values, y_values):
    # Create a 2D array from x_values and y_values
    data = np.vstack((x_values, y_values))
    
    # Calculate the covariance matrix
    cov_matrix = np.cov(data)
    
    return cov_matrix


def covariance_matrix2(x_values, y_values, z_values):
    # Create a 2D array from x_values, y_values, and z_values
    data = np.vstack((x_values, y_values, z_values))
    
    # Calculate the covariance matrix
    cov_matrix = np.cov(data)
    
    return cov_matrix




import numpy as np

def find_eigenvalue_matrix(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    eigenvalue_matrix = np.diag(eigenvalues)
    return eigenvalue_matrix



def find_eigenvectors(matrix):
    _, eigenvectors = np.linalg.eig(matrix)
    return eigenvectors
    
    
print("Covariance bulmak alanı")
print("")  

# Example usage
x_values = [0.69,-1.31,0.39,0.09,1.29,0.49,0.19,-0.81,-0.31,-0.71]
y_values = [0.49,-1.21,0.99,0.29,1.09,0.79,-0.31,-0.81,-0.31,-1.01]
z_values = [0.49,-1.21,0.99,0.29,1.09,0.79,-0.31,-0.81,-0.31,-1.01]
cov_matrix = covariance_matrix2(x_values, y_values,z_values)
print(cov_matrix)

print("")
print("")  


print("Eigen bulma alanı")
print("")  
# Example matrix
matrix = np.array([[0.6165, 0.6154], [0.6154, 0.7165]])

# Find eigenvalue matrix
eigenvalue_matrix = find_eigenvalue_matrix(matrix)
result = find_eigenvectors(matrix)

print("Eigen values")
print("Eigenvalue matrix:")
print(eigenvalue_matrix)


print("")
print("")
print("Eigen vectors")
print(result)




