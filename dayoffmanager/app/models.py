from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
  ADMIN = 'ADMIN'
  LEADER = 'LEADER'
  EMPLOYEE = 'EMPLOYEE'
  ROLES = (
    (ADMIN, 'admin'),
    (LEADER, 'leader'),
    (EMPLOYEE, 'employee'),
  )
  user_name = models.CharField(max_length=15)
  name = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  role = models.CharField(
    max_length=20,
    choices=ROLES,
    default=EMPLOYEE,
  )
  available_day_off = models.DecimalField(max_digits=3, decimal_places=1)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

class Request(models.Model):
  PENDING = 'PENDING'
  ACCEPT = 'ACCEPT'
  REJECT = 'REJECT'
  CANCELLED = 'CANCELLED'
  STATUSES = (
    (PENDING, 'pending'),
    (ACCEPT, 'accept'),
    (REJECT, 'reject'),
    (CANCELLED, 'cancelled'),
  )

  user = models.ForeignKey(
    'User',
    on_delete=models.CASCADE,
    related_name='requests'
  )
  number_day_off = models.DecimalField(max_digits=3, decimal_places=1)
  status = models.CharField(
    max_length=20,
    choices=STATUSES,
    default=PENDING,
  )
  request_user = models.ForeignKey(
    'User',
    on_delete=models.CASCADE,
    related_name='asked_requests'
  )
  reason = models.TextField()
  requested_user_note = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  updated_date = models.DateTimeField(default=timezone.now)
