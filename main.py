from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner(name="Adou", pets=[])

# Create pets
dog = Pet(name="Max", species="Dog")
cat = Pet(name="Luna", species="Cat")

# Add tasks to dog
dog.add_task(Task(description="Morning Walk", time="08:00", duration=30, priority="High", frequency="daily"))
dog.add_task(Task(description="Feeding", time="07:00", duration=10, priority="High", frequency="daily"))
dog.add_task(Task(description="Medication", time="08:00", duration=5, priority="Medium", frequency="daily"))

# Add tasks to cat
cat.add_task(Task(description="Feeding", time="07:30", duration=10, priority="High", frequency="daily"))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner=owner)

# Print today's schedule sorted by time
print("=== Today's Schedule ===")
for task in scheduler.sort_by_time():
    print(f"{task.time} - {task.description} ({task.priority})")

# Check for conflicts
print("\n=== Conflict Check ===")
conflicts = scheduler.detect_conflicts()
for warning in conflicts:
    print(warning)