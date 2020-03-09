from django.db import models

CLOSED = 'closed'
OPENED = 'opened'
IN_PROGRESS = 'in_progress'

STATUS_CHOICES = (
    (CLOSED, CLOSED),
    (OPENED, OPENED),
    (IN_PROGRESS, IN_PROGRESS),
)


class Application(models.Model):
    status = models.CharField(choices=STATUS_CHOICES, default=OPENED, max_length=20)

    def __str__(self):
        return self.status
