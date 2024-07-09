import streamlit as st
from generation import generate, complete


# Streamlit UI
st.title("Story Generation and Completion")

st.sidebar.title("Options")
task = st.sidebar.selectbox(
    "Choose Task", ["Generate a New Story", "Complete a Story"])

if task == "Generate a New Story":
    st.header("Enter your story prompt:")
    prompt = st.text_input(
        "Sory Title", placeholder="Dog and Cat", label_visibility='hidden')

    st.sidebar.header("Generation Options")

    # Creating the slider
    temperature = st.sidebar.slider(
        label="Realistic Creative", min_value=0.0, max_value=1.0, value=0.5)
    length = st.sidebar.selectbox(
        "Select length", ["Small", "Medium", "Large"])
    if length == "Small":
        length = 100
    elif length == "Medium":
        length = 300
    else:
        length = 500

    # Optional parameters (initially None)
    genre = None
    narrative_perspective = None
    character_name = None
    character_description = None
    setting_description = None

    # Check if optional parameters are given
    if st.sidebar.checkbox("Additional Options"):
        genre = st.sidebar.selectbox(
            "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])
        narrative_perspective = st.sidebar.selectbox(
            "Narrative perspective", ["First-person", "Third-person", "Epistolary", "Omniscient", "Interactive", "Camera Eye", "Observer", "Stream of Consciousness", "Multiple Perspectives"])
        character_name = st.sidebar.text_input(
            "Character Name", placeholder='Ex: Jane Doe')
        character_description = st.sidebar.text_area(
            "Character Description", placeholder='Ex: Jane Doe is is a timid 30-year-old librarian who has lizard as a pet.')
        setting_description = st.sidebar.text_area(
            "Setting Description", placeholder='Ex: An old small library with many windows.')

    if st.button("Generate Story"):
        if prompt.strip():
            story = generate(prompt, length, temperature, genre, narrative_perspective,
                             character_name, character_description, setting_description)
            st.subheader("Generated Story:")
            st.write(story)
        else:
            st.error("Please enter a story prompt.")

elif task == "Complete a Story":
    st.header("Enter your partial story:")
    partial_story = st.text_area(
        "Partial Story", placeholder="The adventure began when", label_visibility='hidden')

    st.sidebar.header("Completion Options")
    # Creating the slider
    temperature = st.sidebar.slider(
        label="Realistic Creative", min_value=0.0, max_value=1.0, value=0.7)
    length = st.sidebar.selectbox(
        "Select length", ["Small", "Medium", "Large"])
    if length == "Small":
        length = 100
    elif length == "Medium":
        length = 300
    else:
        length = 500

    # Optional parameters (initially None)
    genre = None
    narrative_perspective = None
    character_name = None
    character_description = None
    setting_description = None

    # Check if optional parameters are given
    if st.sidebar.checkbox("Additional Options"):
        genre = st.sidebar.selectbox(
            "Select genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror"])
        narrative_perspective = st.sidebar.selectbox(
            "Narrative perspective", ["First-person", "Third-person", "Epistolary", "Omniscient", "Interactive", "Camera Eye", "Observer", "Stream of Consciousness", "Multiple Perspectives"])
        character_name = st.sidebar.text_input(
            "Character Name", placeholder='Ex: Jane Doe')
        character_description = st.sidebar.text_area(
            "Character Description", placeholder='Ex: Jane Doe is is a timid 30-year-old librarian who has lizard as a pet.')
        setting_description = st.sidebar.text_area(
            "Setting Description", placeholder='Ex: An old small library with many windows.')

    if st.button("Complete Story"):
        if partial_story.strip():
            completed_story = generate(partial_story, length, temperature, genre,
                                       narrative_perspective, character_name, character_description, setting_description)
            st.subheader("Completed Story:")
            st.write(completed_story)
        else:
            st.error("Please enter a partial story.")
