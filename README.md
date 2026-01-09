[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SirRody/AI-GameAgent---RL/blob/main/demo.ipynb)
# 🎮 AI Game Agent: Mastering Text-Based Adventures with Reinforcement Learning

## 📋 Project Overview

This project explores how artificial intelligence can learn to play text-based adventure games—similar to classic games like Zork—using three different reinforcement learning approaches. Just as a human player reads descriptions and types commands, these AI agents learn optimal strategies through trial and error, navigating virtual rooms and completing quests to maximize their rewards.

Imagine teaching a computer to understand game instructions like "You are in a living room" and respond with commands like "go north" or "eat apple" to solve puzzles. That's exactly what this project demonstrates!

## 📁 Files

- agent_dqn.py - Deep Q-Network implementation
- agent_linear.py - Linear function approximation Q-learning
- agent_tabular_ql.py - Tabular Q-learning implementation
- framework.py - Game framework and environment
- utils.py - Utility functions for feature extraction
- game.tsv - Game data file

## 📦 Requirements

- Python 3.x
- PyTorch
- NumPy
- Matplotlib

## 🎯 The Problem

Text-based games present a unique challenge for AI: they combine **natural language understanding** with **sequential decision-making**. Unlike board games with clear rules, text adventures require:
- Understanding descriptive language
- Making decisions with partial information
- Planning multi-step strategies
- Learning from sparse, delayed rewards

Traditional game AI uses hand-coded rules, but reinforcement learning allows agents to learn optimal behavior purely from experience—just like humans learn to play games!

## 🏗️ Project Structure

```
📁 AI-GameAgent---RL/
│
├── 🧠 AI Agents
│   ├── agent_tabular_ql.py    - Classic Q-learning with lookup tables
│   ├── agent_linear.py        - Linear function approximation
│   └── agent_dqn.py           - Deep Q-Network (neural network)
│
├── 🎮 Game Environment
│   ├── framework.py           - Game simulation engine
│   ├── game.tsv              - Game data and descriptions
│   └── utils.py              - Text processing utilities
│
└── 📄 Configuration
    ├── requirements.txt       - Python dependencies
    └── README.md             - This documentation
```

## ⚔️ Challenges Faced

1. **State Representation**: Converting text descriptions ("This room has a couch") into numerical features
2. **Exploration vs Exploitation**: Balancing trying new actions vs sticking with known good ones
3. **Sparse Rewards**: The agent only gets positive feedback when completing quests
4. **Partial Observability**: Rooms appear differently each time, requiring generalization
5. **Credit Assignment**: Determining which actions led to eventual success

## 📊 Performance Summary

| **Agent Type** | **Avg. Episodic Reward** | **Theoretical Optimum** | **Performance** |
|----------------|--------------------------|-------------------------|-----------------|
| **Tabular Q-learning** | 0.498 | 0.5538 | 90% of optimum |
| **Linear Approximation** | 0.374 | 0.5538 | 67% of optimum |
| **Deep Q-Network (DQN)** | **0.503** | 0.5538 | **91% of optimum** |

**Key Insights:**
- **DQN performed best**, showing neural networks' ability to generalize
- **Tabular methods** worked surprisingly well for this state space
- **Linear approximation** struggled with the complexity of text features
- All agents significantly outperformed random play (≈0.0 reward)

## 🌍 Real-World Applications

1. **Intelligent Chatbots**: Natural language dialogue systems that learn optimal conversation paths
2. **Game AI**: Non-player characters that learn strategies and adapt to player behavior
3. **Robotics**: Teaching robots to understand verbal instructions and plan actions
4. **Recommendation Systems**: Learning user preferences through sequential interactions
5. **Self-Driving Cars**: Decision-making in complex, partially observable environments
6. **Healthcare Assistants**: Medical chatbots that learn optimal diagnostic questioning
7. **Educational Tutors**: Adaptive learning systems that personalize teaching strategies
8. **Customer Service Automation**: AI agents that learn to resolve issues through natural conversation

## 🏁 Conclusion

This project successfully demonstrates that reinforcement learning agents can master text-based environments, with the Deep Q-Network achieving **91% of theoretical optimal performance**. The progression from tabular methods to neural networks shows how AI can handle increasingly complex state representations.

The work bridges natural language processing and decision-making—a crucial step toward AI that can understand instructions and act in text-based worlds, with applications ranging from customer service automation to intelligent tutoring systems.

---

## 👨‍💻 Author

**Rodrick** - Data Science & Machine Learning Enthusiast

A passionate developer exploring the intersection of reinforcement learning and natural language processing. This project represents hands-on experience with implementing cutting-edge AI algorithms to solve interactive decision-making problems.

*"Teaching AI to play games is about more than entertainment—it's about creating systems that can understand instructions, make decisions, and learn from experience."*

---




