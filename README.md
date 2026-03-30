# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Key Features & Algorithms

PawPal+ includes an intelligent `Scheduler` engine powered by efficient data structures and algorithms:

- **Chronological Task Sorting (Timsort)**: Leverages Python's highly optimized built-in sorting combined with lambda functions to dynamically merge and order upcoming tasks—from all pets—into a single timeline.
- **O(N) Conflict Detection**: Uses a cycle-detection approach powered by Hash Sets (`set()`). By tracking mapped times, it detects duplicate schedules in a single pass over the data, ensuring fast $O(N)$ execution instead of slower nested loop checks.
- **Automated Recurrence Engine**: Features a safe-iteration system that checks frequency and completion states (with case-insensitive parsing) to automatically clone completed "daily" tasks and seamlessly requeue them as fresh, incomplete events.
- **Dynamic Comprehension Filtering**: Utilizes fast Python list comprehensions to cleanly slice large datasets of tasks by their completion statuses or specific pet owners without mutating existing lists.
- **Filter by status**: See only completed or incomplete tasks.
- **Conflict detection**: The scheduler warns you when two tasks are scheduled at the same time.
- **Recurring tasks**: Daily tasks automatically reschedule for the next day when marked complete.

### 🚀 Challenge 1: Advanced Algorithmic Capability (Agent Mode)
As part of extending the system's logic, PawPal+ includes a **"Next Available Slot" Suggestion Algorithm**.

**What it does:** Given a desired task duration (e.g., 30 minutes), the algorithm scans the owner's entire schedule, converts `HH:MM` time strings into flat integer minutes (from midnight), and iterates chronologically to find the earliest continuous open gap between existing tasks falling between an `08:00` start and `20:00` end-of-day. 

**How Copilot Agent Mode was used:**
1. I utilized **GitHub Copilot Agent Mode** to ideate the feature by prompting for a third algorithmic capability requiring interval math.
2. The Agent autonomously wrote the logic for `suggest_next_available_slot()`, specifically handling the tricky time conversions (`hh * 60 + mm`) and edge cases (e.g., jumping the `current_time` pointer to the end of existing tasks rather than overlapping).
3. The Agent seamlessly hooked up the new backend algorithm into the `app.py` Streamlit layout, producing a full-stack integrated feature under the **"🤖 Smart Assistant"** tab.

## Testing PawPal+

To run the test suite:

```bash
python -m pytest
```

### What the tests cover:

- **Task completion**: Verifies `mark_complete()` sets `is_complete` to True
- **Task addition**: Verifies adding a task increases pet's task count
- **Sorting correctness**: Verifies tasks are returned in chronological order
- **Recurring tasks**: Confirms daily tasks auto-reschedule after completion
- **Case-insensitive frequency**: Handles "DAILY", "Daily", "daily" correctly
- **Non-recurring tasks**: Verifies one-time tasks don't duplicate
- **Infinite loop prevention**: Confirms `handle_recurring()` safely iterates

### Confidence Level: ⭐⭐⭐⭐ (4/5)

The core scheduling logic is well tested. Edge cases around duration-based conflict detection and weekly recurring tasks would need additional coverage for a production system.
