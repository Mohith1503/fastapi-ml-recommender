from fastapi import APIRouter,HTTPException
from app.recommender import recommend,user_movie
import logging

router=APIRouter()
logging.basicConfig(level=logging.INFO,force=True)
logger = logging.getLogger(__name__)

@router.get("/health")
def health_check():
    return {"status": "running" }

@router.get("/recommend")
def get_recommend(user_id :int):
    logger.info(f"request received for user {user_id}")
    if user_id not in user_movie.index:
        logger.error(f"user {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    results=recommend(user_id)
    logger.info(f"recommendations generated for user {user_id}")

    return{
        "status": "success",
        "user_id": user_id,
        "recommended_movies": results
    }