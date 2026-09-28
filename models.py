from pydantic import BaseModel

class LearningResponse(BaseModel):
	answer: str
	key_points: list[str]
	topics: list[str]
	follow_up_question: str
