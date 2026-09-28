from pydantic import BaseModel, Field

class LearningResponse(BaseModel):
	answer: str
	difficulty: int = Field(
    	ge=1,
    	le=10,
    	description="Difficulty of the topic, where 1 is beginner and 10 is expert"
	)
	key_points: list[str]
	topics: list[str]
	follow_up_question: str
