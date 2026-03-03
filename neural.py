def neuron(inputs, weights, bias):
    # Calculate the weighted sum of inputs
    weighted_sum = 0
    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]
    # Add bias to the weighted sum
    output = weighted_sum + bias
    return max(0, output) # ReLU activation function

def main():
    pass

if __name__ == "__main__":
    main()