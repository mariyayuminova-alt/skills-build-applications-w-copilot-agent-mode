from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_leader=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_leader=True),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity workout', difficulty='Hard')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for superheroes', difficulty='Medium')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100, rank=1)
        Leaderboard.objects.create(team=dc, points=80, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))