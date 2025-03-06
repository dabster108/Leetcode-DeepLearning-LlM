# 🧠 Deep Learning

Deep learning is a subfield of machine learning that uses neural networks with many layers to model complex patterns in data.

## How it Works
- Inspired by the structure of the human brain (neurons)
- Uses multiple layers of interconnected nodes

## Key Concepts
- **Neural Networks**
- **Activation Functions**
- **Backpropagation**
- **Convolutional Layers (CNNs)** – For image data
- **Recurrent Layers (RNNs)** – For sequence data

## Applications
- Image recognition
- Speech recognition
- Natural language processing
- Natural language understanding 



Basic Deep Learning Terminologies:
Neurons: The basic units of a neural network, inspired by the human brain. Each neuron receives inputs, processes them using weights, and then passes the result to other neurons.

Layers: Neural networks are built in layers:

Input layer: Receives the input data.

Hidden layer(s): Layers between the input and output layers where computations take place.

Output layer: Produces the final output of the network.

Activation Function: A mathematical function that determines the output of a neuron based on its input. Common activation functions include:

ReLU (Rectified Linear Unit): f(x) = max(0, x)

Sigmoid: f(x) = 1 / (1 + exp(-x))

Tanh: f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))

Weights: Parameters in a neural network that determine the strength of connections between neurons. These values are updated during training.

Bias: An additional parameter in each neuron that helps the model fit the data better. It allows the activation function to shift.

Forward Propagation: The process of passing inputs through the network to get the output.

Backward Propagation: The process of adjusting weights and biases based on the error of the model's predictions, to minimize the loss function.

Loss Function: A function that calculates the error between the predicted output and the actual output. Common loss functions include:

Mean Squared Error (MSE): Used for regression tasks.

Cross-Entropy Loss: Used for classification tasks.

Optimizer: A method used to minimize the loss function by updating the weights and biases. Common optimizers include:

Gradient Descent

Adam (adaptive gradient method)

Epoch: One complete pass through the entire training dataset.