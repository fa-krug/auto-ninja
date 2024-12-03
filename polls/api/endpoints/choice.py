from polls import models
from  polls.api import schemas
from demo.api import services
from demo.api.utils import AliasRouter
from ninja import Query

router = AliasRouter(tags=["Choice"])


@router.get("/count", response=int)
def count(request):
    """Count all entries."""
    return models.Choice.objects.count()


@router.get("", response=list[schemas.ChoiceOut])
def list_all(request, filters: schemas.ChoiceFilter = Query(...)):
    """List all entries."""
    return services.list_all(models.Choice.objects.all(), filters)


@router.get("/{pk}", response=schemas.ChoiceOut)
def get(request, pk: int):
    """Get an entry."""
    return services.get(models.Choice, pk)


@router.post("", response=schemas.ChoiceOut)
def create(request, payload: schemas.ChoiceIn):
    """Create a new entry."""
    return services.create(models.Choice, payload)


@router.put("/{pk}", response=schemas.ChoiceOut)
def update(request, pk: int, payload: schemas.ChoiceIn):
    """Edit an entry."""
    return services.update(models.Choice, pk, payload)


@router.delete("/{pk}", response={204: None})
def delete(request, pk: int):
    """Delete an entry."""
    return services.delete(models.Choice, pk)
