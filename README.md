# Traffic Warden ANN

**Traffic Warden ANN** is a minimalist Artificial Neural Network (ANN) simulation designed to automate traffic light transitions. It uses a single-layer perceptron model with a ReLU (Rectified Linear Unit) activation function to decide whether a traffic signal should turn green or stay red based on real-time inputs.

## The Advantage: Why ANN for Traffic?

Unlike traditional hard-coded timers, this neural approach allows for a dynamic decision-making process. By adjusting weights and biases, the "warden" can be tuned to prioritize different traffic conditions, such as clearing high-density lanes or reducing long wait times.

* **Mathematical Precision**: The system calculates a weighted sum of inputs ($x_i \cdot w_i$) plus a bias ($z$) to determine the output.
* **Non-Linear Logic**: Implements the ReLU activation function, which ensures the output is non-negative ($max(0, output)$), providing a clear threshold for binary "Stop" or "Go" decisions.
* **Zero Dependencies (Core)**: The primary engine is built using pure Python, making it extremely lightweight and portable for embedded traffic controllers.
* **Visual Validation**: Includes integrated plotting capabilities to map out the AI's "thought process" across thousands of potential traffic scenarios.



## Project Structure

The project consists of three specialized modules:

1.  **`neural.py`**: The core engine containing the `neuron` function and ReLU activation logic.
2.  **`main.py`**: A command-line controller for testing specific scenarios, such as 10 cars waiting for 5 minutes.
3.  **`matamain.py`**: A visualization tool that uses `matplotlib` to plot a 2D decision boundary.

## Quick Start

### 1. Run a Single Scenario
Execute the main script to see how the neuron processes specific car counts and wait times:

```python
# logic: (car_count * 0.8) + (time_waited * 0.6) - 5
python main.py
2. Visualize the Decision Boundary

To see the full logic map (where the light turns green vs. red), run the mapping script:

Bash
python matamain.py
How it Works (The Math)
The decision is based on three adjustable parameters defined in the controller:

Inputs (x 
1
​	
 ,x 
2
​	
 ): The number of cars and the time waited.

Weights (w 
1
​	
 ,w 
2
​	
 ): The importance assigned to each factor (currently 0.8 for cars and 0.6 for time).

Bias (z): The threshold that must be overcome to trigger a green light (currently -5).

Input	Variable	Current Weight
Car Count	x 
1
​	
 	0.8
Time Waited	x 
2
​	
 	0.6
Bias/Threshold	z	-5.0
The final output is determined by:

Output=max(0,(x 
1
​	
 ⋅w 
1
​	
 +x 
2
​	
 ⋅w 
2
​	
 )+z)
If the output is greater than 0, the system signals a GREEN LIGHT; otherwise, it remains RED.

Developed as a lightweight demonstration of Artificial Neural Networks in infrastructure management.
