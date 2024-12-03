from polls.api.endpoints import question, choice
from demo.api.utils import AliasRouter

router = AliasRouter()

router.add_router("/question", question.router)
router.add_router("/choice", choice.router)
