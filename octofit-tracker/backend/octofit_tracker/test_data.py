from bson import ObjectId
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

def populate_test_data():
    # Create users
    users = [
        User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
        User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
        User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
        User(_id=ObjectId(), username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
        User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
    ]
    User.objects.bulk_create(users)

    # Create teams
    team_blue = Team(_id=ObjectId(), name='Blue Team')
    team_gold = Team(_id=ObjectId(), name='Gold Team')
    team_blue.save()
    team_gold.save()
    team_blue.members.add(*users[:3])  # Add first three users to Blue Team
    team_gold.members.add(*users[3:])  # Add remaining users to Gold Team

    # Create activities
    activities = [
        Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
        Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
        Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
        Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
        Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
    ]
    Activity.objects.bulk_create(activities)

    # Create leaderboard entries
    leaderboard_entries = [
        Leaderboard(_id=ObjectId(), user=users[0], score=100),
        Leaderboard(_id=ObjectId(), user=users[1], score=90),
        Leaderboard(_id=ObjectId(), user=users[2], score=95),
        Leaderboard(_id=ObjectId(), user=users[3], score=85),
        Leaderboard(_id=ObjectId(), user=users[4], score=80),
    ]
    Leaderboard.objects.bulk_create(leaderboard_entries)

    # Create workouts
    workouts = [
        Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
        Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
        Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
        Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
        Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
    ]
    Workout.objects.bulk_create(workouts)

    print("Test data populated successfully.")
