import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mobile Location", layout="centered")

st.title("📍 Get Current Mobile Location")

html_code = """
<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const acc = position.coords.accuracy;

                const data = {
                    lat: lat,
                    lon: lon,
                    accuracy: acc
                };
                document.getElementById("output").innerHTML =
                    JSON.stringify(data);
            },
            (error) => {
                document.getElementById("output").innerHTML =
                    "ERROR: " + error.message;
            }
        );
    } else {
        document.getElementById("output").innerHTML =
            "Geolocation not supported";
    }
}
getLocation();
</script>

<div id="output">Fetching location...</div>
"""

location = components.html(html_code, height=100)
