import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Line Path Map", layout="centered")
st.title("🚌 Kolhapur Bus Stand ➝ 📍 Current Location (Line Path)")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet"
 href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<style>
#map { height: 400px; width: 100%; }
</style>
</head>

<body>

<p id="status">📡 Getting your location...</p>
<div id="map"></div>

<script>
const busStand = [16.704987, 74.243252];

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    function(position) {

      const userLat = position.coords.latitude;
      const userLon = position.coords.longitude;

      document.getElementById("status").innerHTML =
        `🚌 Kolhapur Bus Stand<br>
         📍 Your Location<br>
         Lat: ${userLat}, Lon: ${userLon}`;

      var map = L.map('map').setView(busStand, 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
      }).addTo(map);

      // Markers
      L.marker(busStand).addTo(map).bindPopup("🚌 Kolhapur Bus Stand");
      L.marker([userLat, userLon]).addTo(map).bindPopup("📍 You");

      // Line Path
      var path = [
        busStand,
        [userLat, userLon]
      ];

      L.polyline(path, {
        color: 'blue',
        weight: 4,
        dashArray: '6, 6'
      }).addTo(map);

      map.fitBounds(path);
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

components.html(html_code, height=460)
