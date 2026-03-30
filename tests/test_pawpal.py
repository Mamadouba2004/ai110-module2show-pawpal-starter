import sys
import os

# Ensure the parent directory is in the path so we can import pawpal_system
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task(description="Morning Walk", time="08:00", duration=30, priority="High", frequency="daily")
    assert not task.is_complete
    task.mark_complete()
    assert task.is_complete

def test_pet_task_addition():
    pet = Pet(name="Max", species="Dog")
    task = Task(description="Morning Walk", time="08:00", duration=30, priority="High", frequency="daily")
    
    initial_count = len(pet.get_tasks())
    pet.add_task(task)
    new_count = len(pet.get_tasks())
    
    assert new_count == initial_count + 1
    assert task in pet.get_tasks()

def test_scheduler_sort_tasks():
    pet = Pet(name="Buddy", species="Dog")
    pet.add_task(Task(description="Lunch", time="12:00", duration=15, priority="Medium", frequency="one-time"))
    pet.add_task(Task(description="Breakfast", time="08:00", duration=15, priority="High", frequency="daily"))
    pet.add_task(Task(description="Dinner", time="18:00", duration=15, priority="Medium", frequency="daily"))
    
    owner = Owner("Alice")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "12:00"
    assert sorted_tasks[2].time == "18:00"

def test_handle_recurring_daily():
    pet = Pet(name="Buddy", species="Dog")
    task = Task(description="Walk", time="08:00", duration=30, priority="High", frequency="daily")
    pet.add_task(task)
    task.mark_complete()
    
    owner = Owner("Alice")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    
    scheduler.handle_recurring()
    tasks = pet.get_tasks()
    
    assert len(tasks) == 2
    assert tasks[0].is_complete is True
    assert tasks[1].is_complete is False

def test_handle_recurring_case_insensitive():
    pet = Pet(name="Buddy", species="Dog")
    task = Task(description="Walk", time="08:00", duration=30, priority="High", frequency="DAILY")
    pet.add_task(task)
    task.mark_complete()
    
    owner = Owner("Alice")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    
    scheduler.handle_recurring()
    assert len(pet.get_tasks()) == 2

def test_handle_recurring_one_time():
    pet = Pet(name="Buddy", species="Dog")
    task = Task(description="Vet", time="10:00", duration=60, priority="High", frequency="one-time")
    pet.add_task(task)
    task.mark_complete()
    
    owner = Owner("Alice")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    
    scheduler.handle_recurring()
    assert len(pet.get_tasks()) == 1

def test_handle_recurring_no_infinite_loop():
    pet = Pet(name="Buddy", species="Dog")
    task = Task(description="Walk", time="08:00", duration=30, priority="High", frequency="daily")
    pet.add_task(task)
    task.mark_complete()
    
    owner = Owner("Alice")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    
    # If the method iterates and mutates the list improperly, this will hang.
    scheduler.handle_recurring()
    
    assert len(pet.get_tasks()) == 2

def test_scheduler_detect_conflicts():
    pet1 = Pet(name="Buddy", species="Dog")
    pet1.add_task(Task(description="Morning Walk", time="09:00", duration=30, priority="High", frequency="daily"))
    
    pet2 = Pet(name="Luna", species="Cat")
    pet2.add_task(Task(description="Feeding", time="09:00", duration=15, priority="Medium", frequency="daily"))
    
    pet3 = Pet(name="Max", species="Dog")
    pet3.add_task(Task(description="Vet", time="14:00", duration=60, priority="High", frequency="one-time"))

    owner = Owner("Alice")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    
    assert len(conflicts) == 1
    assert "09:00" in conflicts[0]

