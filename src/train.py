from sb3_contrib import MaskablePPO
from sb3_contrib.common.maskable.evaluation import evaluate_policy
from sb3_contrib.common.maskable.utils import get_action_masks
from sapai_gym import SuperAutoPetsEnv
from sapai_gym.opponent_gen.opponent_generators import random_opp_generator, biggest_numbers_horizontal_opp_generator
from sapai_gym.ai import baselines
from sapai_gym import SuperAutoPetsEnv

def train_with_masks():
    def opponent_generator(num_turns):
    # Returns teams to fight against in the gym 
        opponents = biggest_numbers_horizontal_opp_generator(25)
        return opponents
    # opponents = biggest_numbers_horizontal_opp_generator(25)
    env = SuperAutoPetsEnv(opponent_generator, valid_actions_only=True)

    model = MaskablePPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_sapai_3_tensorboard/")
    # model.load("ppo_sapai_3")
    model.learn(total_timesteps=10000)
    model.save("ppo_sapai_3")
    evaluate_policy(model, env, n_eval_episodes=20, reward_threshold=1, warn=False)
    obs = env.reset()
    
    num_games = 0
    # while num_games < 100:
    #     # Predict outcome with model
    #     action_masks = get_action_masks(env)
    #     action, _states = model.predict(obs, action_masks=action_masks, deterministic=True)

    #     obs, reward, done, info = env.step(action)
    #     if done:
    #         num_games += 1
    #         obs = env.reset()
    print("done")
    env.close()

train_with_masks()