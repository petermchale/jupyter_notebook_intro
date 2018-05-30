import numpy as np 
import matplotlib.pyplot as plt 


def reshape_1d_array(x): # helper function
    return x.reshape(len(x),1)


def generate_data(f, n=10, std=10): 
    x = np.random.uniform(0,5,n)
    y = f(x) + np.random.normal(0,std,len(x))
    x = reshape_1d_array(x) 
    y = reshape_1d_array(y)   
    return x, y


def plot_data_and_two_curves(f, compute_sum_of_squares, compute_theta, n=1000, std=10):
    x_examples, y_examples = generate_data(f, n, std)
    thetas = compute_theta(x_examples, y_examples)
    h = lambda x: thetas[0] + thetas[1]*x + thetas[2]*x**2
    xs = np.linspace(0,5,100)

    plt.figure().set_size_inches(10,5)
    plt.scatter(x_examples, y_examples) # data
    plt.plot(xs, f(xs), 'green', linewidth=3) # true curve
    plt.plot(xs, h(xs), 'red', linewidth=3) # fitted curve
    plt.legend(['f', 'h'],fontsize=16)
    
    compute_sum_of_squares(x_examples, y_examples, f, 'f')
    compute_sum_of_squares(x_examples, y_examples, h, 'h')

