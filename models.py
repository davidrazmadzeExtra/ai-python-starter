from pydantic import BaseModel, Field

class LearningResponse(BaseModel):
	answer: str
	difficulty: int = Field(
		description="Difficulty of the topic from 1 to 10, where 1 is beginner and 10 is expert"
	)
	key_points: list[str]
	topics: list[str]
	follow_up_question: str
