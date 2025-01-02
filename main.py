import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn as nn
import torch.optim as optim

# Project 1: Simple Neural Network from Scratch
class BasicNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
       
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.hidden = self.sigmoid(np.dot(X, self.weights1))
        self.output = self.sigmoid(np.dot(self.hidden, self.weights2))
        return self.output
    
    def train(self, X, y, epochs=10000):
        for _ in range(epochs):
            # Forward propagation
            output = self.forward(X)
            
            # Backpropagation
            output_error = y - output
            output_delta = output_error * self.sigmoid_derivative(output)
            
            hidden_error = output_delta.dot(self.weights2.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden)
            
            # Update weights
            self.weights2 += self.hidden.T.dot(output_delta)
            self.weights1 += X.T.dot(hidden_delta)

# Project 2: Sentiment Analysis with Transformers
class SentimentAnalysisProject:
    def __init__(self):
     
        self.sentiment_pipeline = pipeline("sentiment-analysis")
    
    def analyze_sentiments(self, texts):
     
        return [self.sentiment_pipeline(text)[0] for text in texts]
    
    def custom_dataset_analysis(self):
        """Example with custom dataset"""
        sample_reviews = [
            "This product is amazing and works perfectly!",
            "Terrible experience, would not recommend.",
            "It's okay, nothing special but does the job.",
            
"good bad but good bad good bad"
        ]
        
        results = self.analyze_sentiments(sample_reviews)
        for review, result in zip(sample_reviews, results):
            print(f"Review: {review}")
            print(f"Sentiment: {result['label']}")
            print(f"Confidence: {result['score']:.2%}\n")

# Project 3: Image Classification Simulation
class SimpleImageClassifier:
    def __init__(self):
       
        self.model = nn.Sequential(
            nn.Linear(784, 128),  # Input layer (28x28 flattened image)
            nn.ReLU(),
            nn.Linear(128, 10)    # 10 classes output
        )
        self.loss_fn = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters())
    
    def generate_dummy_data(self):
   
        X = torch.randn(100, 784)  # 100 images, 28x28 flattened
        y = torch.randint(0, 10, (100,))  # 10 classes
        return X, y
    
    def train_simulation(self, epochs=50):
        X, y = self.generate_dummy_data()
        
        for epoch in range(epochs):
            # Forward pass
            outputs = self.model(X)
            loss = self.loss_fn(outputs, y)
            
            # Backward pass and optimize
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Project 4: Text Generation Playground
class TextGenerationDemo:
    def __init__(self):
     
        self.generator = pipeline('text-generation', 
                                  model='distilgpt2')
    
    def generate_text(self, prompt, max_length=100):
        """Generate text based on a prompt"""
        generated_text = self.generator(
            prompt, 
            max_length=max_length, 
            num_return_sequences=1
        )[0]['generated_text']
        return generated_text

# Demonstration Function
def run_ai_workshop_projects():
    print("🚀 AI Workshop: Practical Projects Demonstration\n")
    
    # Neural Network Basics
    print("Project 1: Basic Neural Network")
    nn_data = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
    X = nn_data[:, :2]
    y = nn_data[:, -1].reshape(-1, 1)
    
    # basic_nn = BasicNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    # basic_nn.train(X, y)
    # print("Neural Network trained successfully!\n")
    
    # Sentiment Analysis
    print("Project 2: Sentiment Analysis")
    sentiment_project = SentimentAnalysisProject()
    sentiment_project.custom_dataset_analysis()
    
    # Image Classification Simulation
    # print("Project 3: Image Classification Simulation")
    # image_classifier = SimpleImageClassifier()
    # image_classifier.train_simulation()
    
    # Text Generation
    # print("\nProject 4: Text Generation")
    # text_generator = TextGenerationDemo()
    # generated_text = text_generator.generate_text("In the world of India,")
    # print("Generated Text:", generated_text)

# Run the demonstration
run_ai_workshop_projects()