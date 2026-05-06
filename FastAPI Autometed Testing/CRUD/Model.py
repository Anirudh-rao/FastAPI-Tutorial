from pydantic import BaseModel

class Review(BaseModel):
    movie : str
    num_stars: int
    text:str


class DbReview(BaseModel):
    movie: str
    num_stars : int
    text : str
    review_id : int