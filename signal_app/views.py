from django.shortcuts import render

# Create your views here.
import time
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.http import HttpResponse
import threading
from django.db import transaction

# Signal receiver for post_save
@receiver(post_save, sender=User)
def question1_signal_receiver(sender, instance, **kwargs):
    print("Signal received: Executing receiver function...")
    time.sleep(2)  # Simulating a long-running task
    print("Receiver function finished execution.")


def question1(request):
    print("Creating a new User instance...")
    # Creating a new user which will trigger the post_save signal
    User.objects.create(username='testuser', email='testuser@example.com')
    print("User created, continuing with view logic...")
    
    return HttpResponse("Signal triggered.")


# Signal receiver for pre_save
@receiver(pre_save, sender=User)
def question2_signal_receiver(sender, instance, **kwargs):
    print("Signal received: Executing receiver function...")
    print(f"Receiver running in thread: {threading.current_thread().name} (ID: {threading.get_ident()})")

def question2(request):
    print(f"View running in thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
    
    # Creating a new user which will trigger the post_save signal
    User.objects.create(username='testuser1', email='testuser1@example.com')

    return HttpResponse("Signal triggered.")


# Signal receiver for pre_save
@receiver(pre_save, sender=User)
def question3_signal_receiver(sender, instance, **kwargs):
    print("Signal received: Creating a record in User model...")
    User.objects.create(username = "signal user2", email="signalemail@example.com")

# Triggering signal in view
def question3(request):
    users = User.objects.all().count()
    print("Users count before creating: ", users)
    try:
        with transaction.atomic():  # Start a database transaction
            print("Creating a new User instance...")
            User.objects.create(username='testuser3', email='testuser@example.com')

            # Simulating an error to force a rollback
            raise Exception("Simulating an error, rolling back transaction")

    except Exception as e:
        print(f"Exception occurred: {e}")

    users = User.objects.all().count()
    print("Users count after creating: ", users)
    # Check if any records were created
    signal_actions = User.objects.all()
    return HttpResponse(f"SignalAction entries: {signal_actions.count()}")