from django.db import models

class PingResult(models.Model):
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=10)  # "active" veya "inactive"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.status}"
