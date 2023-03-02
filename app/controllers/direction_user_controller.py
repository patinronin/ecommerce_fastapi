from controllers.base_db_controller import BaseDBController
from schemas.direction_schema import (
    DirectionUser,
    DirectionCreate,
    DirectionUserUpdate
)

class DirectionUserController(BaseDBController):
    pass


direction_user_controller = DirectionUserController(
    model=DirectionUser,
    model_create=DirectionCreate,
    model_update=DirectionUserUpdate
)
