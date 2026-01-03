from fastapi import APIRouter, Depends
from app.modules.users.schemas import UserSchema
from .service import UserService, get_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[UserSchema])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()
