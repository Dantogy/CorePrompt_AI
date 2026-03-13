from llama_cpp import Llama

# Load Mistral Instruct model
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=8,
)

ALL_DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

DAY_MAPPING = {
    1: ["Monday"],
    2: ["Monday","Thursday"],
    3: ["Monday","Wednesday","Friday"],
    4: ["Monday","Tuesday","Thursday","Friday"],
    5: ["Monday","Tuesday","Thursday","Friday","Saturday"],
    6: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
}

# Muscle splits per number of training days
SPLITS = {
    1: ["Full Body"],
    2: ["Upper","Lower"],
    3: ["Push","Pull","Legs"],
    4: ["Upper","Lower","Upper","Lower"],
    5: ["Push","Pull","Legs","Upper","Lower"],
    6: ["Push","Pull","Legs","Push","Pull","Legs"],
}

# Optional muscle group labels
MUSCLE_LABELS = {
    "Push": "Push Day (Chest, Shoulders, Triceps)",
    "Pull": "Pull Day (Back, Biceps)",
    "Legs": "Leg Day (Quads, Hamstrings, Glutes, Calves)",
    "Upper": "Upper Body",
    "Lower": "Lower Body",
    "Full Body": "Full Body"
}

def generate_day_workout(day, muscle_focus, goal, weight_kg, height_cm, difficulty="Intermediate"):
    """
    Generate a single day's workout, respecting muscle group and difficulty.
    """
    prompt = f"""
Generate a {difficulty.lower()} {muscle_focus} workout for {day}.

Goal: {goal}
Weight: {weight_kg} kg
Height: {height_cm} cm

Rules:
- 5-6 exercises
- Format all exercises consistently: Exercise Name (sets, reps, rest in seconds)
- Focus on {muscle_focus} muscles only
- Include only exercises suitable for {difficulty.lower()} level
- No explanations, no markdown
- Example: Bench Press (4, 8-10, 90s)
"""

    response = llm.create_chat_completion(
        messages=[
            {"role":"system","content":"You are an expert fitness coach who writes beginner/intermediate/advanced gym programs."},
            {"role":"user","content":prompt},
        ],
        temperature=0.5,
        top_p=0.9,
        repeat_penalty=1.1,
        max_tokens=500,
    )

    return response["choices"][0]["message"]["content"].strip()


def generate_workout(goal: str, days_per_week: int, weight_kg: float, height_cm: float, difficulty="Intermediate") -> str:
    """
    Generate full 7-day workout plan with deterministic splits and difficulty filtering.
    """
    days_per_week = min(days_per_week, 6)
    training_days = DAY_MAPPING.get(days_per_week, ["Monday"])
    split = SPLITS.get(days_per_week, ["Full Body"] * days_per_week)

    full_plan = ""
    split_index = 0

    for day in ALL_DAYS:
        if day in training_days:
            muscle_focus = split[split_index]
            label = MUSCLE_LABELS.get(muscle_focus, muscle_focus)
            full_plan += f"{day} — {label}\n"
            workout = generate_day_workout(day, muscle_focus, goal, weight_kg, height_cm, difficulty)
            full_plan += workout + "\n\n"
            split_index += 1
        else:
            full_plan += f"{day} — Rest Day\n\n"

    return full_plan.strip()