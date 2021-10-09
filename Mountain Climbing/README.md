---
Mountain Climbing using DQN
---

## Problem
A car is on a one-dimensional track, positioned between two mountains. The goal is to drive up the mountain on the right (reaching the flag). 

## Objective
The car’s engine is not strong enough to climb the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum. Thus we create a reward system in such a way that the car runs back and forth to generate enough momentum to reach the flag.

![Success Gif](https://github.com/Sidhved/ML-Reserve/blob/main/Mountain%20Climbing/resource/mountain_car.gif)

## Terminology
- **Episode:** An episode is an instance of a game (or life of a game). If the game ends or life decreases, the episode ends.
- **Step:** Step is the time or some discrete value which increases monotonically in an episode. With each change in the state of the game, the value of step increases until the game ends.
- **Environment:** The environment is the surrounding or setting on which the agent performs actions. Here, the CartPole environment is the CartPole and the setting on which CartPole operates.

## How to use
- Star and Fork the Repository
- In the clone repo, navigate to ./MountainClimbing/model/[MountainClimbing.ipynb](https://github.com/Sidhved/ML-Reserve/blob/main/Mountain%20Climbing/Model/MountainClimbing.ipynb)(Note: The simulation environment works best when cloned and operated on local devices. Might cause rendering issues in platforms like Google Colab)
- Follow the code and execute it in the order mentioned (Heads-up: Num_Episodes is set to 100 and max_steps is set to 300. This may take time to complete execution. Alter it to suit your needs)

## Libraries
- [gym](https://gym.openai.com/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [collections](https://docs.python.org/3/library/collections.html)
- [keras.models, keras.layers, keras.optimizers](https://keras.io/)
- [random](https://docs.python.org/3/library/random.html)

## DQN Agent and Reward System 
- DQN stands for [Deep Q-Network](https://deepmind.com/research/open-source/dqn). In this project, we have created our own Q-Network instead of Tensorflow distribution.
- The Q-Network has a sequential model with 3 Dense layers.
- The Agent runs in an environment. Here, we define the environement using MountainCar-v0 from the [gym](https://gym.openai.com/) library.
- After setting the hyperparameters with number of episodes = 100, we will start training the network by remembering a tuple (state, action, reward, next_state, done).
- After each episode, a score is calculated on basis of loss incurred. The score determines the next action of the agent. It helps with the feedback mechanism constructed on basis of coordinates on the environment plane.

## Results
- The car was able to reach the goal multiple times (episode 60, 71, 74, 79)
- It can be also observed as peaking values in the score plot as show below

![Score Plot](https://github.com/Sidhved/ML-Reserve/blob/main/Mountain%20Climbing/resource/mc.png)
