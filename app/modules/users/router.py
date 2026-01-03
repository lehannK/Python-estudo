from fastapi import APIRouter, Depends, HTTPException
from app.modules.users.schemas import CreateUserSchema, UserSchema
from .service import UserService, get_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[UserSchema])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()


@router.post("/", response_model=UserSchema)
def create_user(
    user: CreateUserSchema,
    service: UserService = Depends(get_user_service),
):
    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
