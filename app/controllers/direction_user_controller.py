from controllers.base_db_controller import BaseDBController
from models.direction_user_model import DirectionUser


class DirectionUserController(BaseDBController):
    def __init__(self, model):
        self.model = model
        #super().__init__(model=self.model)

direction_user_controller = DirectionUserController(
    model=DirectionUser
)
