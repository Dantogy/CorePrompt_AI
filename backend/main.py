from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import generate_workout

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorkoutRequest(BaseModel):
    goal: str
    days_per_week: int
    weight_kg: float = 70.0
    height_cm: float = 170.0
    difficulty: str = "intermediate"  # beginner / intermediate / advanced

@app.post("/generate")
async def generate(request: WorkoutRequest):
    try:
        plan = generate_workout(
            goal=request.goal,
            days_per_week=request.days_per_week,
            weight_kg=request.weight_kg,
            height_cm=request.height_cm,
            difficulty=request.difficulty
        )

        return {"workout_plan": plan}

    except Exception as e:
        return {"workout_plan": f"Error generating workout: {e}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5005)