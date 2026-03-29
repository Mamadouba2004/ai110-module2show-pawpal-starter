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
        pass

@dataclass
class Pet:
    """Represents a pet and the tasks associated with its care."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass

class Owner:
    """Represents the pet owner who manages one or more pets."""
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self) -> List[Task]:
        pass

class Scheduler:
    """Manages the scheduling, filtering, and conflict resolution of tasks for an owner."""
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        pass

    def sort_by_time(self):
        pass

    def filter_by_status(self, status: bool):
        pass

    def detect_conflicts(self):
        pass

    def handle_recurring(self):
        pass
