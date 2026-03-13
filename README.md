## Setup & Installation

### 1. Requirements
- **Python 3.11** (Required for compatibility with llama-cpp-python and torch)
- **Git** (For repository management)

### 2. Clone the Repository
```bash
git clone [https://github.com/Dantogy/CorePrompt_AI.git](https://github.com/Dantogy/CorePrompt_AI.git)
cd CorePrompt_AI
```

### 3. Model Setup
- Create a models/ folder in the project root.

- Download mistral-7b-instruct-v0.2.Q4_K_M.gguf.

- Place it in models/.

### 4. Environment Setup

# Create environment with specific Python version
python -m venv myenv

# Activate
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt