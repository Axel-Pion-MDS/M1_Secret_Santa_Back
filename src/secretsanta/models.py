from cProfile import label
from django.db import models

from users.models import Member


class Santa(models.Model):
    label = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500)
    draw_date = models.DateTimeField()

    def __str__(self):
        return '{} - {} ({})'.format(self.pk, self.label, self.draw_date)


class SantaMember(models.Model):
    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        related_name='member_id',
    )
    target = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        related_name='target_id',
    )
    santa = models.ForeignKey(
        Santa,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{} - {} {} > {} {}'.format(self.pk, self.member.firstname, self.member.lastname, self.target.firstname, self.member.lastname)
