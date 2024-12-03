from ninja import ModelSchema

from polls import models
from demo.api.utils import AliasMixin, InMeta, OutMeta, FilterModelSchema


class QuestionIn(AliasMixin, ModelSchema):
    class Meta(InMeta):
        model = models.Question


class QuestionOut(AliasMixin, ModelSchema):
    class Meta(OutMeta):
        model = models.Question


class QuestionFilter(AliasMixin, FilterModelSchema):
    class Meta(InMeta):
        model = models.Question
