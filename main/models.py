from django.db import models

class Team(models.Model):
    pass

class Member(models.Model):
    name = models.CharField("Member Name", max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
