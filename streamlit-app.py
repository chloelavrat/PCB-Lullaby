import streamlit as st
import subprocess

# Function to execute the command and generate the output file
def generate_gcode(file_name, bedTemp, timeMix, numWait, speed, zPosition, frontPosition, backPosition):
    command = [
        'python', './src/perchloride_mixer_generator.py',
        file_name,
        '--bedTemp', str(bedTemp),
        '--timeMix', str(timeMix),
        '--numWait', str(numWait),
        '--speed', str(speed),
        '--zPosition', str(zPosition),
        '--frontPosition', str(frontPosition),
        '--backPosition', str(backPosition)
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f"Error: {result.stderr}")
        return None
    else:
        st.success("G-code generated successfully!")
        with open(file_name, "r") as file:
            gcode = file.read()
        return gcode

st.title("PCB EtchCode G-code Creator")
st.markdown("""
            Welcome to the PCB EtchCode G-code Creator app! 
            
            This application is designed to simplify the process of generating G-code for controlling your Ender3 3D printer to mix iron perchloride for PCB etching. By utilizing the heated bed and (x,y) plate movements of the Ender 3, this app ensures efficient mixing of the fluid, significantly speeding up the PCB manufacturing process.
            
            Fill in the parameters, and click "Generate the G-code" to generate and download the customized G-code for your setup.""")

gcode_content = None

with st.form("my_form"):
    st.write("**Fill in the parameters below to adapt the pattern**")
    file_name_input = st.text_input("File name", "EtchCode_output.gcode")
    bedTemp_input = st.number_input("Bed temperature (0°C if no heat needed)", value=30)
    timeMix_input = st.number_input("Mix duration (minutes)", value=1)
    numWait_input = st.number_input("Number of messages at start ", value=2)
    speed_input = st.number_input("Bed speed", value=2000)
    frontPosition_input = st.number_input("X position in front", value=125)
    backPosition_input = st.number_input("Y position in back", value=150)
    zPosition_input = st.number_input("Z position safe", value=200)

    if submitted := st.form_submit_button("Generate the G-code"):
        gcode_content = generate_gcode(file_name_input, bedTemp_input, timeMix_input, numWait_input, speed_input, zPosition_input, frontPosition_input, backPosition_input)

if gcode_content:
    st.download_button(label="Download G-code", data=gcode_content, file_name=file_name_input, mime="text/plain")

with st.expander("Chloe Lavrat"):
    st.write(''' INFOS HERE ''')