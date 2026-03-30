import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")

# Initialize the Owner object in the session state vault
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

# Update the owner's name based on the input, defaulting to the session state value
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name

st.subheader("Manage Pets")
col_p1, col_p2 = st.columns(2)
with col_p1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col_p2:
    species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, species=species)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name} the {species}!")

if st.session_state.owner.pets:
    st.write("Current Pets:")
    for p in st.session_state.owner.pets:
        st.write(f"- **{p.name}** ({p.species})")

st.markdown("### Tasks")
st.caption("Add tasks to your pets to feed into your scheduler.")

if st.session_state.owner.pets:
    selected_pet_name = st.selectbox("Assign task to pet", [p.name for p in st.session_state.owner.pets])
else:
    st.warning("Please add a pet first before adding tasks.")
    selected_pet_name = None

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
    task_time = st.time_input("Task time", value=None)
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
with col3:
    priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=2)

if st.button("Add task") and selected_pet_name:
    # Find the selected pet
    pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet_name)
    
    # Store using the Task dataclass!
    new_task = Task(
        description=task_title, 
        time=task_time.strftime("%H:%M") if task_time else "12:00", 
        duration=int(duration), 
        priority=priority, 
        frequency=frequency
    )
    pet.add_task(new_task)
    st.success(f"Added '{task_title}' to {pet.name}'s task list!")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate your organized schedule using the backend Scheduler logic.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner=st.session_state.owner)
    sorted_tasks = scheduler.sort_by_time()
    
    if not sorted_tasks:
        st.info("No tasks to schedule yet! Add some above.")
    else:
        st.markdown("### 📅 Today's Schedule")
        
        # Format the tasks into a list of dictionaries for a professional st.table/dataframe
        table_data = []
        for t in sorted_tasks:
            pet_owner_name = next((p.name for p in st.session_state.owner.pets if t in p.tasks), "Unknown Pet")
            table_data.append({
                "Time": t.time,
                "Pet": pet_owner_name,
                "Task": t.description,
                "Duration (mins)": t.duration,
                "Priority": t.priority,
                "Status": "✅ Complete" if t.is_complete else "⏳ Pending"
            })
            
        # Display the schedule using Streamlit's table component
        st.table(table_data)
        
        # Checking for any conflicts
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.warning("⚠️ **Heads up! Scheduling conflicts detected:**")
            for c in conflicts:
                st.error(f"- {c}")
            st.info("💡 Tip: Try adjusting the times of the overlapping tasks so you aren't double-booked!")
        else:
            st.success("✅ Perfect! No scheduling conflicts detected.")
            
        st.divider()
        st.subheader("🤖 Smart Assistant")
        st.markdown("Need to squeeze in another task?")
        duration_needed = st.number_input("Duration needed (minutes)", min_value=1, max_value=120, value=15)
        if st.button("Find Next Available Slot"):
            suggested_time = scheduler.suggest_next_available_slot(duration_needed)
            if suggested_time != "No available slots":
                st.success(f"🎉 The next available {duration_needed}-minute slot is at **{suggested_time}**!")
            else:
                st.error(f"❌ Schedule is too full! Could not find a {duration_needed}-minute gap.")
