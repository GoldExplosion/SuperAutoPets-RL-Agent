# Super Auto Pets RL Agent
Gaming Using RL is my Final Year Project. This project is about building a Super Auto Pets Agent using **sapai** engine, **sapai-gym** open gym environment and **stable baselines 3** for Reinforcement Learning Model. The Agent has 3 modules: 

1. Computer Vision 
2. Reinforcement Learning Model
3. Model2Game interface

## 1. Computer Vision 
In this module, we extract state information(The Shop Pets and Food) from the game screenshot. This is done using *Single Image Template Matching* but the needle image and haystack image are of the same dimensions(we search the needle image in the haystack image). The implementation is in the image_detection.py

## 2. Reinforcement Learning Model
The RL Model is a MaskablePPO implementation using stable baselines 3. This model is run for 60,000 interations. It is a very weak model compared to humans. Its all time high wins is 2/10. 

## 3. Model2Game interface
The Model2Game interface is used to convert the output of the model to mouse movements and clicks. This is implemented using pyautogui.

# Training Metrics

## Average Mean Reward
![Average Mean Reward](assets\avg_mean_reward.png)
## Average Number of Actions Per Game
![Average Number of Actions](assets\no_of_actions.png)