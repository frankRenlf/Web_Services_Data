from app01.utils.BootstrapModelForm import BootstrapModelForm
from app01 import models


class AdminModelForm(BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["name", "password"]
