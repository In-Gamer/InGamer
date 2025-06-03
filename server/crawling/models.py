from django.db import models


class Match(models.Model):
  match_date = models.CharField(max_length=100)
  match_time = models.CharField(max_length=100)
  team_a = models.CharField(max_length=100)
  team_b = models.CharField(max_length=100)
  a_logo = models.URLField(max_length=200, default='logo_url')
  b_logo = models.URLField(max_length=200, default='logo_url')
  
  def __str__(self):
    return f"{self.team_a} vs {self.team_b} on {self.match_date} at {self.match_time}"