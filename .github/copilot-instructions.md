# Copilot Instructions for PawPal+

This codebase is a Python-based Streamlit application (PawPal+) designed to help pet owners plan care tasks based on constraints (time, priority, owner preferences). 

## Architecture & Design Patterns
- **UML-First Approach:** The architecture heavily relies on upfront UML design. When adding new features or domain models, refer to or iterate on the existing UML before jumping into logic implementation.
- **Separation of Concerns:** 
  - **Domain Logic:** Core scheduling, pet/owner models, and constraint checking should be implemented in pure Python (e.g., `pawpal_system.py`).
  - **UI Layer:** The Streamlit frontend (`app.py`) should be kept "thin" and only responsible for state management (`st.session_state`) and displaying the schedule. Do not mix complex scheduling logic into the Streamlit file.

## Developer Workflow
- **Dependency Management:** The project uses a virtual environment pattern. Always ensure packages are added to `requirements.txt`.
- **Running the App:** Use `streamlit run app.py` to start the local server.
- **Testing:** The backend logic should be tested independently of the UI. Focus on testing critical scheduling behaviors and edge cases using `pytest` (e.g., handling impossible constraints, prioritizing tasks correctly).

## Implementation Guidelines
- **Task Modeling:** Ensure tasks have clear properties for `duration`, `priority`, and type. The scheduler should produce a plan and an *explanation* of why the plan was chosen.
- **State Management in Streamlit:** Variables that must persist across Streamlit re-renders (like added tasks or the generated schedule) must be stored in `st.session_state`.
- **Iterative Refinement:** After making changes to the backend codebase, ensure UML diagrams/documentation reflect the new structure.