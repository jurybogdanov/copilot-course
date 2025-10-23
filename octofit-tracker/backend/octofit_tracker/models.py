from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    stats = models.JSONField(default=dict)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.type} - {self.user.name}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='workouts')
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries')
    rank = models.IntegerField()
    score = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"
