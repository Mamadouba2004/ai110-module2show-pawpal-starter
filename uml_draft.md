classDiagram
    class Owner {
        +String name
        +List~Pet~ pets
        +add_pet(pet)
        +get_all_tasks()
    }

    class Pet {
        +String name
        +String species
        +List~Task~ tasks
        +add_task(task)
        +get_tasks()
    }

    class Task {
        +String description
        +String time
        +int duration
        +String priority
        +String frequency
        +boolean is_complete
        +mark_complete()
    }

    class Scheduler {
        +Owner owner
        +get_all_tasks()
        +sort_by_time()
        +filter_by_status(status)
        +detect_conflicts()
        +handle_recurring()
    }

    %% Relationships
    Owner "1" *-- "many" Pet : owns
    Pet "1" *-- "many" Task : has
    Scheduler "1" --> "1" Owner : manages