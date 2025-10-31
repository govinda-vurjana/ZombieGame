# Zombie Shooter AI using Deep Reinforcement Learning

A project by [Govinda Vurjana](https://github.com/govinda-vurjana)

This project implements a Zombie Shooter game where an AI agent learns to play using Double Deep Q-Network (DDQN) reinforcement learning. The agent learns to navigate the environment, shoot zombies, and survive as long as possible.

## Project Structure

```
├── agent.py           # Implementation of the DDQN agent
├── buffer.py         # Experience replay buffer implementation
├── bullet.py         # Bullet game object implementation
├── characters.py     # Player and zombie character implementations
├── game.py           # Main game environment implementation
├── main.py          # Entry point for running the trained agent
├── model.py         # Neural network architecture (ZombieNet)
├── train.py         # Training script for the agent
├── util.py          # Utility functions
├── walls.py         # Wall objects implementation
├── images/          # Game assets
└── sounds/          # Game sound effects
```

## Technical Implementation

### Reinforcement Learning Architecture

The project uses Double Deep Q-Network (DDQN), an advanced variant of DQN that helps prevent overestimation of Q-values. Key components include:

#### Neural Network (ZombieNet)
- 4 Convolutional layers for processing visual input
- 3 Fully connected layers
- Outputs Q-values for each possible action
- Uses ReLU activation and dropout for regularization

#### Agent Implementation
- Uses two Q-networks to reduce overestimation bias
- Implements epsilon-greedy exploration strategy
- Experience replay buffer for storing transitions
- Soft and hard target network updates
- Adam optimizer for training

### Training Parameters

```python
episodes = 10000
batch_size = 64
learning_rate = 0.0001
epsilon = 1
min_epsilon = 0.1
epsilon_decay = 0.995
gamma = 0.99
```

### Game Environment

The game environment is implemented in `game.py` and provides:
- Custom PyGame-based environment
- RGB observation space
- Discrete action space
- Reward system based on zombie kills and survival

## Requirements

The project requires the following Python packages:
- PyTorch
- PyGame
- NumPy
- TensorBoard
- Pympler

## Training Process

To train the agent:
1. Run `train.py`
2. The script will:
   - Initialize the game environment
   - Create the DDQN agent
   - Train for the specified number of episodes
   - Save model checkpoints in the `models/` directory
   - Log training metrics to TensorBoard

## Model Architecture

The ZombieNet architecture:
1. **Convolutional Layers**:
   - Conv1: 1 → 8 channels, 4x4 kernel, stride 2
   - Conv2: 8 → 16 channels, 4x4 kernel, stride 2
   - Conv3: 16 → 32 channels, 3x3 kernel, stride 2
   - Conv4: 32 → 64 channels, 3x3 kernel, stride 2
   
2. **Fully Connected Layers**:
   - FC1: conv_output → hidden_dim
   - FC2: hidden_dim → hidden_dim
   - FC3: hidden_dim → hidden_dim
   - Output: hidden_dim → action_dim

## Running the Trained Agent

To run a trained agent:
1. Ensure model weights are present in the `models/` directory
2. Run `main.py`

## Monitoring Training

Training progress can be monitored using TensorBoard:
- Loss values for both Q-networks
- Episode rewards
- Epsilon value over time
- Other relevant metrics

## Future Improvements

Potential areas for enhancement:
1. Prioritized Experience Replay
2. Dueling DQN architecture
3. Multi-step learning
4. Noisy Networks for better exploration
5. Distributed training support

## Author

- **Govinda Vurjana** - [GitHub Profile](https://github.com/govinda-vurjana)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details