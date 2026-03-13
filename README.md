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

- Create a models/ folder in the backend/ folder.

- Download mistral-7b-instruct-v0.2.Q4_K_M.gguf.
```bash
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/blob/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf
```

- Place it in models/.

### 4. Environment Setup

- Create environment with specific Python version

```bash
  python -m venv myenv
```

- Activate

```bash
  myenv\Scripts\activate
```

- Install dependencies

```bash
  pip install -r requirements.txt
```

## 🚀 How to Run & Use

### 1. Start the Engine (Backend)

Navigate to the root directory, ensure your virtual environment is active, and run:

```bash
uvicorn main:app --reload --port 5005
```

The API will be live at http://127.0.0.1:5005. You can view the automated docs at /docs.

### 2. Launch the Interface (Frontend)

Open frontend/index.html in your browser.

Recommended: Use the VS Code Live Server extension to prevent CORS issues and ensure the Tailwind styles render correctly.

### 3. Generating a Workout

- **Enter Biometrics:** Input your weight and height (used for calorie/intensity scaling).

- **Select Goal:** Choose from "Strength," "Hypertrophy," or "Endurance."

- **Choose Frequency:** Select how many days you want to train (1-7 days).

- **Generate:** Click the button and wait ~10-15 seconds for the local Mistral-7B model to stream the workout plan.
