import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,6,8,10,12,14,16,18,20])

def linear_regression(x, weight, bias):
    return weight * x + bias

# MSE
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Gradient of the loss function
def compute_gradients(x, y, weight, bias):
    # Predictions
    y_pred = linear_regression(x, weight, bias)
    
    # Gradients
    d_weight = -2 * np.mean(x * (y - y_pred))  
    d_bias = -2 * np.mean(y - y_pred)        
    
    return d_weight, d_bias

# Update the model parameters 
def gradient_descent(x, y, weight, bias, learning_rate, num_iterations):
    losses = []
    for i in range(num_iterations):
        # Compute gradients
        d_weight, d_bias = compute_gradients(x, y, weight, bias)
        
        # Update parameters
        weight -= learning_rate * d_weight
        bias -= learning_rate * d_bias
        
        # Compute loss
        loss = mse_loss(y, linear_regression(x, weight, bias))
        losses.append(loss)
        
        # Plot the fit 
        plt.figure()
        plt.scatter(x, y)
        plt.plot(x, linear_regression(x, weight, bias), color='green')
        plt.title(f'Iteration {i+1}, Loss: {loss:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    return weight, bias, losses

# Plot the fit after every iteration using GD
learning_rate = 0.01
num_iterations = 10
initial_weight = 0  
initial_bias = 0  

# Perform GD
final_weight, final_bias, losses = gradient_descent(x, y, initial_weight, initial_bias, learning_rate, num_iterations)

# Plot loss curve
plt.figure()
plt.plot(range(num_iterations), losses)
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.show()

print("Final parameters :")
print("Weight :", final_weight)
print("Bias :", final_bias)
