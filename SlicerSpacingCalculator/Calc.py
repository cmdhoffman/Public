import streamlit as st
import math

st.title("Power BI Slicer Spacing Calculator")

st.write("-------------------------")

sidebar_container = st.empty()
#radio options
with sidebar_container.container():
    st.sidebar.header("Select Slicer Spacing Option")
    
    option = st.sidebar.radio(" ", ("BOTH top and bottom slicer position known","ONLY top slicer position known", "Reset"))
    if option == "BOTH top and bottom slicer position known":
    # option 1
        a_first_slicer_vertical_position = st.number_input(label="First slicer vertical position", min_value=0)
        a_last_slicer_vertical_position = st.number_input(label="Last slicer vertical position",min_value=0)
        a_slicer_height = st.number_input(label="Slicer height",min_value=0)
        a_number_of_slicers = st.number_input(label="Total number of slicers",min_value=0)

        a_spaces_needed = a_number_of_slicers - 1
        a_vertical_pixels_between_slicers = a_last_slicer_vertical_position - a_first_slicer_vertical_position
        # use of round to create symmetrical spacing 
        a_pixels_between_each_slicer = math.ceil(((a_vertical_pixels_between_slicers-(a_slicer_height*a_spaces_needed))/a_spaces_needed))


        if st.button(label="Calculate"):
            st.write("Slicer 1 Position: ",a_first_slicer_vertical_position)
            i = 1
            a = a_first_slicer_vertical_position
            while i < a_number_of_slicers:
                i += 1
                a_next_slicer_position = a + a_slicer_height + a_pixels_between_each_slicer
                st.write("Slicer ",str(i)," Position: ",a_next_slicer_position)
                a = a_next_slicer_position
        else:
            st.warning("Please input parameters")

    if option == "ONLY top slicer position known":
        # option 2
        b_first_slicer_vertical_position = st.number_input(label="First slicer vertical position ", min_value=0)
        b_slicer_height = st.number_input(label="Slicer height ",min_value=0)
        b_number_of_slicers = st.number_input(label="Total number of slicers ",min_value=0)
        b_space_between_slicers = st.number_input(label="Desired space between slicers ", min_value=0)

        b_spaces_needed = b_number_of_slicers - 1

        if st.button(label="Calculate"):
            st.write("Slicer 1 Position: ",b_first_slicer_vertical_position)
            i = 1
            b = b_first_slicer_vertical_position
            while i < b_number_of_slicers:
                i += 1
                b_next_slicer_position = b + b_slicer_height + b_space_between_slicers
                st.write("Slicer ",str(i)," Position: ",b_next_slicer_position)
                b = b_next_slicer_position
        else:
            st.warning("Please input parameters")
    
    if option == "Reset":
        # if st.sidebar.button("Reset"):
        sidebar_container.empty()
