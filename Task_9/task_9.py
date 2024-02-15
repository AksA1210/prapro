import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,6,8,10,12,14,16,18,20])

# Step 1: Define the linear regression model
def linear_regression(x, w, b):
    return w * x + b

# Step 2: Define the loss function (Mean Squared Error)
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Step 3: Compute the gradient of the loss function
def compute_gradients(x, y, w, b):
    # Predictions
    y_pred = linear_regression(x, w, b)
    
    # Gradients
    dw = -2 * np.mean(x * (y - y_pred))  # Gradient with respect to weight
    db = -2 * np.mean(y - y_pred)        # Gradient with respect to bias
    
    return dw, db

# Step 4: Update the model parameters using gradient descent
def gradient_descent(x, y, w, b, learning_rate, num_iterations):
    losses = []
    for i in range(num_iterations):
        # Compute gradients
        dw, db = compute_gradients(x, y, w, b)
        
        # Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db
        
        # Compute current loss
        loss = mse_loss(y, linear_regression(x, w, b))
        losses.append(loss)
        
        # Plot the fit after every iteration
        plt.figure()
        plt.scatter(x, y)
        plt.plot(x, linear_regression(x, w, b), color='red')
        plt.title(f'Iteration {i+1}, Loss: {loss:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    return w, b, losses

# Step 5: Plot the fit after every iteration using gradient descent
learning_rate = 0.01
num_iterations = 10
initial_w = 0  # Initial weight
initial_b = 0  # Initial bias

# Perform gradient descent
final_w, final_b, losses = gradient_descent(x, y, initial_w, initial_b, learning_rate, num_iterations)

# Plot the loss curve
plt.figure()
plt.plot(range(num_iterations), losses)
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.show()

# Print final parameters
print("Final parameters:")
print("Weight:", final_w)
print("Bias:", final_b)
