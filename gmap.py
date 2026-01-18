import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mobile Location Map", layout="centered")

st.title("📍 Current Mobile Location with Map")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link
  rel="stylesheet"
  href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<style>
#map {
  height: 300px;
  width: 100%;
}
</style>
</head>

<body>

<p id="status">📡 Fetching location...</p>
<div id="map"></div>

<script>
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    function(position) {

      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      const acc = position.coords.accuracy;

      document.getElementById("status").innerHTML =
        `Latitude: ${lat}<br>Longitude: ${lon}<br>Accuracy: ${acc} meters`;

      var map = L.map('map').setView([lat, lon], 16);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
      }).addTo(map);

      L.marker([lat, lon]).addTo(map)
        .bindPopup("📍 You are here")
        .openPopup();
    },
    function(error) {
      document.getElementById("status").innerHTML =
        "❌ Error: " + error.message;
    }
  );
} else {
  document.getElementById("status").innerHTML =
    "❌ Geolocation not supported";
}
</script>

</body>
</html>
"""

components.html(html_code, height=420)
