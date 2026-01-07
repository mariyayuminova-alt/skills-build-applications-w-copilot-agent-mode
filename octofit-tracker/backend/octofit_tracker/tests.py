from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team3', description='A test team')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, calories=100, date='2026-01-07')
        self.assertEqual(str(activity), 'Run by Test User2 on 2026-01-07')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team4', description='A test team')
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team5', description='A test team')
        leaderboard = Leaderboard.objects.create(team=team, points=10, rank=1)
        self.assertEqual(str(leaderboard), 'Test Team5 - 10 pts')
