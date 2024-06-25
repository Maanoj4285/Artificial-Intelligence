import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.bias1 = np.zeros((1, self.hidden_size))

        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        self.bias2 = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        # Layer 1 (input to hidden)
        self.hidden_sum = np.dot(inputs, self.weights1) + self.bias1
        self.activated_hidden = self.sigmoid(self.hidden_sum)

        # Layer 2 (hidden to output)
        self.output_sum = np.dot(self.activated_hidden, self.weights2) + self.bias2
        self.activated_output = self.sigmoid(self.output_sum)

        return self.activated_output


# Example usage:
if __name__ == "__main__":
    input_size = 3
    hidden_size = 4
    output_size = 2

    # Create a neural network
    nn = NeuralNetwork(input_size, hidden_size, output_size)

    # Example input
    inputs = np.array([[0.1, 0.2, 0.3]])

    # Perform forward pass
    predicted_output = nn.forward(inputs)

    print("Input:", inputs)
    print("Predicted Output:", predicted_output)
