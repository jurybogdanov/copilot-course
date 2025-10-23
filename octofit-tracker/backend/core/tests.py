from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', score=10)
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.score, 10)

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', score=10)
        user = User.objects.create(name='Test User', email='test@example.com', team=team, stats={})
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, team)

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', score=10)
        user = User.objects.create(name='Test User', email='test@example.com', team=team, stats={})
        activity = Activity.objects.create(user=user, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.user, user)

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team', score=10)
        user = User.objects.create(name='Test User', email='test@example.com', team=team, stats={})
        workout = Workout.objects.create(name='Workout', description='Desc', difficulty='Easy', assigned_to=user)
        self.assertEqual(workout.name, 'Workout')
        self.assertEqual(workout.assigned_to, user)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', score=10)
        leaderboard = Leaderboard.objects.create(team=team, rank=1, score=10)
        self.assertEqual(leaderboard.team, team)
        self.assertEqual(leaderboard.rank, 1)
        self.assertEqual(leaderboard.score, 10)
