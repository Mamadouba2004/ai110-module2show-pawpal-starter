import sys
import os

# Ensure the parent directory is in the path so we can import pawpal_system
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Task, Pet

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
