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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The conflict detection only checks for exact time matches, not overlapping durations. For example, a 30-minute task at 08:00 and a 10-minute task at 08:15 would not be flagged as a conflict even though they overlap. This is a reasonable tradeoff for simplicity but would need to be improved in a production system.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
