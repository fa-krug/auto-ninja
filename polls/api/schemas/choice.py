from ninja import ModelSchema

from polls import models
from demo.api.utils import AliasMixin, InMeta, OutMeta, FilterModelSchema


class ChoiceIn(AliasMixin, ModelSchema):
    class Meta(InMeta):
        model = models.Choice


class ChoiceOut(AliasMixin, ModelSchema):
    class Meta(OutMeta):
        model = models.Choice


class ChoiceFilter(AliasMixin, FilterModelSchema):
    class Meta(InMeta):
        model = models.Choice
