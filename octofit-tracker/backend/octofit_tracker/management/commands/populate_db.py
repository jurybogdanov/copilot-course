from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', score=100)
        dc = Team.objects.create(name='DC', score=90)

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, stats={"strength": 90, "speed": 70})
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel, stats={"strength": 85, "speed": 65})
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc, stats={"strength": 80, "speed": 60})
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc, stats={"strength": 95, "speed": 80})

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)
        Activity.objects.create(user=superman, type='Swimming', duration=60)
        Activity.objects.create(user=captain, type='Running', duration=25)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes', difficulty='Medium', assigned_to=ironman)
        Workout.objects.create(name='Strength Training', description='Strength for superheroes', difficulty='Hard', assigned_to=superman)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, rank=1, score=100)
        Leaderboard.objects.create(team=dc, rank=2, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
