---
CartPole Balancing
---

## Problem
CartPole problem is the problem of balancing the CartPole. CartPole is the structure where a pole is attached to the cart and the cart is free to slide across the frictionless surface. By sliding the cart left or right, the CartPole is balanced.

## Objective
So, the objective of the CartPole is to keep it from falling or moving out of the range. Therefore, the failure conditions are:
- Magnitude of the angle of the pole with respect to the vertical exceeding some threshold.
- Distance of the CartPole from the center exceeding some threshold.

![Angle Limit Exceed](https://github.com/Sidhved/ML-Reserve/blob/main/CartPole%20Balancing/Resources/Angle.PNG)
![CartPole Moving Out of Screen](https://github.com/Sidhved/ML-Reserve/blob/main/CartPole%20Balancing/Resources/Distance.png)

## Terminology
- **Episode**: An episode is an instance of a game (or life of a game). If the game ends or life decreases, the episode ends. 
- **Step**: Step is the time or some discrete value which increases monotonically in an episode. With each change in the state of the game, the value of step increases until the game ends.
- **Environment**: The environment is the surrounding or setting on which the agent performs actions. Here, the CartPole environment is the CartPole and the setting on which CartPole operates.

## How to use
- Star and fork the repository
- Navigate to [/Model/CartPole.ipynb](https://github.com/Sidhved/ML-Reserve/blob/main/CartPole%20Balancing/Model/CartPole.ipynb)
(_Note: The simulation environment works best when cloned and operated on local devices. Might cause rendering issues in platforms like Google Colab_)

## Libraries
- [gym](https://gym.openai.com/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [collections](https://docs.python.org/3/library/collections.html)
- [keras.models, keras.layers, keras.optimizers](https://keras.io/)
- [random](https://docs.python.org/3/library/random.html)

## DQN Agent
- DQN stands for [Deep Q-Network](https://deepmind.com/research/open-source/dqn). In this project, we have created our own Q-Network instead of Tensorflow distribution.
- The Q-Network has a sequential model with 3 Dense layers.
- The Agent runs in an environment. Here, we define the environement using CartPole-v0 from the [gym](https://gym.openai.com/) library.
- After setting the hyperparameters with number of episodes = 1000, we will start training the network by remembering a tuple (state, action, reward, next_state, done).
- The updated weights are saved into [cp_model folder](https://github.com/Sidhved/ML-Reserve/tree/main/CartPole%20Balancing/cp_model) after every 50 episodes.

## Result
Starting off with Exploration Rate of 1.0, we ended up with a HighScore of 199 and Exploration Rate 0.01
