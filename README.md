# Zombie Shooter AI using Deep Reinforcement Learning

A project by [Govinda Vurjana](https://github.com/govinda-vurjana)
<img width="1596" height="1064" alt="image" src="https://github.com/user-attachments/assets/ec584e61-18ca-48d7-8bd1-b8bb4b230336" />
<img width="1598" height="1064" alt="image" src="https://github.com/user-attachments/assets/1f7249f0-b7aa-46a0-bae6-6a3be023f68c" />



This project implements a Zombie Shooter game where an AI agent learns to play using Double Deep Q-Network (DDQN) reinforcement learning. The agent learns to navigate the environment, shoot zombies, and survive as long as possible. The environment is designed following OpenAI Gym interface principles, making it easy to understand and extend for reinforcement learning experiments.

## Quick Start

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended for faster training)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/govinda-vurjana/ZombieGame.git
cd ZombieGame
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Game

#### Training Mode
To start training a new agent:
```bash
python train.py
```

#### Playing Mode
To watch a trained agent play:
```bash
python main.py
```

### Configuration
- Adjust training parameters in `train.py`:
  - `episodes`: Number of training episodes
  - `batch_size`: Size of training batches
  - `learning_rate`: Learning rate for the neural network
  - `epsilon`: Initial exploration rate
  - `epsilon_decay`: Rate at which exploration decreases
  - `gamma`: Discount factor for future rewards

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

The game environment is implemented in `game.py` and follows OpenAI Gym interface conventions:

#### Environment Interface
- `reset()`: Initializes the environment and returns initial observation
- `step(action)`: Takes an action and returns (next_state, reward, done, info)
- `render()`: Displays the game state (automatically called in training)

#### Observation Space
- Type: Box(84, 84, 1)
- Represents: Grayscale image of the game state
- Processing: Resized and normalized for neural network input

#### Action Space
- Type: Discrete(6)
- Actions:
  - 0: Move Up
  - 1: Move Down
  - 2: Move Left
  - 3: Move Right
  - 4: Shoot
  - 5: No Action

#### Reward Structure
- Killing zombie: +10
- Getting hit: -5
- Survival time: +0.1 per timestep
- Game over: -20

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

## Project Components

### Neural Network Architecture
The `ZombieNet` class in `model.py` implements a CNN-based architecture:
```python
Input Image (84x84x1)
    │
    ▼
Conv1 (8 filters, 4x4, stride 2) + ReLU + MaxPool
    │
    ▼
Conv2 (16 filters, 4x4, stride 2) + ReLU
    │
    ▼
Conv3 (32 filters, 3x3, stride 2) + ReLU + MaxPool
    │
    ▼
Conv4 (64 filters, 3x3, stride 2) + ReLU
    │
    ▼
Fully Connected (1024 units) + ReLU + Dropout
    │
    ▼
Fully Connected (1024 units) + ReLU + Dropout
    │
    ▼
Output Layer (6 units)
```

### Double DQN Implementation
The agent uses Double DQN to prevent overestimation of Q-values:
- Two Q-networks (main and target) for action selection and evaluation
- Soft target network updates for stability
- Experience replay buffer for sample efficiency
- Epsilon-greedy exploration with decay

## Performance Monitoring

### TensorBoard Integration
Monitor training progress using TensorBoard:
```bash
tensorboard --logdir=runs
```

Metrics tracked:
- Episode rewards
- Q-value estimates
- Loss values
- Exploration rate
- Network gradients

### Saving and Loading Models
Models are automatically saved during training:
```python
# Save models
self.model_1.save_the_model(filename='models/dqn1.pt')
self.model_2.save_the_model(filename='models/dqn2.pt')

# Load models
self.model_1.load_the_model(filename='models/dqn1.pt')
self.model_2.load_the_model(filename='models/dqn2.pt')
```

## Future Improvements

Potential areas for enhancement:
1. Prioritized Experience Replay for better sample efficiency
2. Dueling DQN architecture for better value estimation
3. Multi-step learning for faster reward propagation
4. Noisy Networks for better exploration
5. Distributed training support
6. PPO or SAC implementation as alternatives to DQN
7. Human demonstrations for imitation learning
8. Curriculum learning with progressive difficulty

## Author

- **Govinda Vurjana** - [GitHub Profile](https://github.com/govinda-vurjana)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
