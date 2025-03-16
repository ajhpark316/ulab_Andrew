import torch
import numpy as np

def hidden_function():
    # Generating data similar to data.py but adding more noise/obscurity
    x_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
    y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
    X, Y = np.meshgrid(x_data, y_data)
    
    # Modified pattern with additional noise
    pattern = np.sin(X) + np.cos(Y) + np.random.normal(0, 0.2, X.shape)
    
    # Defining the dataset dimensions
    N, D_in, H, D_out = 1000, 2, 50, 1
    
    # Creating the input data
    x = torch.randn(N, D_in) * 3.1415
    y = (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1)
    
    # Adding stronger noise for obscurity
    noise = torch.randn(N, D_out) * 0.3
    y += noise
    
    x_values = x.numpy()[:, 0]
    y_values = x.numpy()[:, 1]
    color_values = y.numpy().flatten()
    
    return x, y, x_values, y_values, color_values

# Call these values
x, y, x_values, y_values, color_values = hidden_function()