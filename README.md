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

## Smarter Scheduling

PawPal+ includes intelligent scheduling features:

- **Sort by time**: Tasks are automatically sorted chronologically so you always see what's coming up next.
- **Filter by pet**: View tasks for a specific pet by name.
- **Filter by status**: See only completed or incomplete tasks.
- **Conflict detection**: The scheduler warns you when two tasks are scheduled at the same time.
- **Recurring tasks**: Daily tasks automatically reschedule for the next day when marked complete.

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
