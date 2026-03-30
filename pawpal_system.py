from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a specific care task for a pet."""
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    is_complete: bool = False

    def mark_complete(self):
        self.is_complete = True

@dataclass
class Pet:
    """Represents a pet and the tasks associated with its care."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

@dataclass
class Owner:
    """Represents the pet owner who manages one or more pets."""
    def __init__(self, name: str, pets: List[Pet] = None):
        self.name = name
        self.pets: List[Pet] = pets if pets is not None else []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks

class Scheduler:
    """
    Manages the scheduling, filtering, and conflict resolution of tasks for an owner.
    """

    # __init__
    """
    Initializes the Scheduler.

    Args:
        owner (Owner): The owner whose tasks will be managed.
    """

    # get_all_tasks
    """
    Retrieves all tasks across all pets belonging to the owner.

    Returns:
        List[Task]: A list of all tasks.
    """

    # sort_by_time
    """
    Sorts all accumulated tasks by their scheduled time.

    Returns:
        List[Task]: A list of tasks ordered by time.
    """

    # filter_by_status
    """
    Filters the owner's tasks by their completion status.

    Args:
        status (bool): True to get completed tasks, False to get incomplete tasks.

    Returns:
        List[Task]: A list of tasks matching the specified completion status.
    """

    # detect_conflicts
    """
    Checks for scheduling conflicts where multiple tasks share the exact same time.

    Returns:
        List[str]: A list of message strings detailing the times where conflicts were detected.
    """

    # handle_recurring
    """
    Processes recurring daily tasks. 
    
    Identifies tasks marked as completed with a "daily" frequency and creates 
    new, uncompleted duplicate tasks for the owner's pets.
    """
    """Manages the scheduling, filtering, and conflict resolution of tasks for an owner."""
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        return self.owner.get_all_tasks()

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Returns all tasks that belong to a specific pet by name."""
        tasks = []
        for pet in self.owner.pets:
            if pet.name == pet_name:
                tasks.extend(pet.get_tasks())
        return tasks

    def sort_by_time(self):
        return sorted(self.get_all_tasks(), key=lambda t: t.time)

    def filter_by_status(self, status: bool):
        return [task for task in self.get_all_tasks() if task.is_complete == status]

    def detect_conflicts(self):
        tasks = self.get_all_tasks()
        seen_times = set()
        conflicts = []
        for task in tasks:
            if task.time in seen_times:
                conflicts.append(f"Conflict detected at time: {task.time}")
            else:
                seen_times.add(task.time)
        return conflicts

    def handle_recurring(self):
        # Create new uncompleted daily tasks for completed ones
        for pet in self.owner.pets:
            new_tasks = []
            for task in pet.tasks:
                if task.is_complete and task.frequency.lower() == "daily":
                    # In a real app we'd add +1 day to a datetime object. This duplicates the task with is_complete=False.
                    new_task = Task(
                        description=task.description,
                        time=task.time,
                        duration=task.duration,
                        priority=task.priority,
                        frequency=task.frequency,
                        is_complete=False
                    )
                    new_tasks.append(new_task)
            pet.tasks.extend(new_tasks)

    def suggest_next_available_slot(self, task_duration: int, day_start: str = "08:00", day_end: str = "20:00") -> str:
        """
        Algorithms Challenge: Finds the next available time slot that can fit a task of a given duration.
        Converts time to minutes from midnight, checks gaps between scheduled tasks, and returns a time string.
        """
        def time_to_mins(t_str):
            h, m = map(int, t_str.split(':'))
            return h * 60 + m
            
        def mins_to_time(m_int):
            h = m_int // 60
            m = m_int % 60
            return f"{h:02d}:{m:02d}"

        tasks = self.sort_by_time()
        current_time = time_to_mins(day_start)
        end_of_day = time_to_mins(day_end)
        
        for task in tasks:
            task_start = time_to_mins(task.time)
            # If there's a big enough gap before this task starts
            if task_start - current_time >= task_duration:
                return mins_to_time(current_time)
            
            # Jump to the end of the current task
            task_end = task_start + task.duration
            if task_end > current_time:
                current_time = task_end
                
        # Check gap between last task and end of day
        if end_of_day - current_time >= task_duration:
            return mins_to_time(current_time)
            
        return "No available slots"
