from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Modification

class ModificationForm(ModelForm):
    class Meta:
        model = Modification
        fields = "__all__"