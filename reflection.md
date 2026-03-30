# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I designed four classes: Owner to manage user info, Pet to store pet details and tasks, Task to represent individual care activities, and Scheduler to organize and prioritize tasks across all pets.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I realized Scheduler needs an extra method I didn't plan for
I moved a method from Owner to Scheduler because it made more sense there
I added a next_due_date attribute to Task for recurring tasks 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers time (tasks are sorted chronologically), priority 
(High/Medium/Low labels help owners focus on what matters most), and 
frequency (daily tasks auto-reschedule). Time was the most important 
constraint because a pet owner's day is structured around a clock.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The conflict detection only checks for exact time matches, not overlapping durations. For example, a 30-minute task at 08:00 and a 10-minute task at 08:15 would not be flagged as a conflict even though they overlap. This is a reasonable tradeoff for simplicity but would need to be improved in a production system.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used GitHub Copilot for design brainstorming (generating the UML diagram), 
scaffolding class skeletons, implementing algorithms like sort_by_time() and 
detect_conflicts(), and generating tests. The most helpful prompts were 
specific ones that included context like #file:pawpal_system.py and described 
exactly what behavior I wanted rather than asking for general solutions.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

Copilot suggested replacing get_all_tasks() with a one-line list comprehension. I kept the explicit loop version because it's easier to read and debug, even though the list comprehension is more Pythonic. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, task addition, sorting correctness, recurring task 
generation, case-insensitive frequency handling, non-recurring task behavior, 
and infinite loop prevention. These were important because they verified both 
the happy paths and the edge cases that could silently break the scheduler.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

4/5 stars. The core scheduling logic is well tested. Duration-based conflict 
detection and weekly recurring tasks would need additional coverage for a 
production system.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

a. Most satisfied with the algorithmic layer — sort, filter, conflict 
detection, and recurring tasks all working together cleanly.

b. I would add duration-aware conflict detection and a weekly recurrence 
option in the next iteration.

c. The most important thing I learned is that AI is a powerful design partner 
but the architect's judgment — deciding what to keep, reject, or modify — is 
what makes the difference between clean and messy code.