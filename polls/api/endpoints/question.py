from polls import models
from  polls.api import schemas
from demo.api import services
from demo.api.utils import AliasRouter
from ninja import Query

router = AliasRouter(tags=["Question"])


@router.get("/count", response=int)
def count(request):
    """Count all entries."""
    return models.Question.objects.count()


@router.get("", response=list[schemas.QuestionOut])
def list_all(request, filters: schemas.QuestionFilter = Query(...)):
    """List all entries."""
    return services.list_all(models.Question.objects.all(), filters)


@router.get("/{pk}", response=schemas.QuestionOut)
def get(request, pk: int):
    """Get an entry."""
    return services.get(models.Question, pk)


@router.post("", response=schemas.QuestionOut)
def create(request, payload: schemas.QuestionIn):
    """Create a new entry."""
    return services.create(models.Question, payload)


@router.put("/{pk}", response=schemas.QuestionOut)
def update(request, pk: int, payload: schemas.QuestionIn):
    """Edit an entry."""
    return services.update(models.Question, pk, payload)


@router.delete("/{pk}", response={204: None})
def delete(request, pk: int):
    """Delete an entry."""
    return services.delete(models.Question, pk)
