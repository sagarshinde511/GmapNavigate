import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Road Path Map", layout="centered")
st.title("🚌 Kolhapur Bus Stand ➝ 📍 Current Location (Road Route)")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet"
 href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>

<link rel="stylesheet"
 href="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.css"/>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.js"></script>

<style>
#map { height: 420px; width: 100%; }
</style>
</head>

<body>

<p id="status">📡 Getting your current location...</p>
<div id="map"></div>

<script>
const busStand = [16.704987, 74.243252];

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    function(position) {

      const userLat = position.coords.latitude;
      const userLon = position.coords.longitude;

      document.getElementById("status").innerHTML =
        `🚌 Start: Kolhapur Bus Stand<br>
         📍 Destination: Your Location`;

      var map = L.map('map').setView(busStand, 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
      }).addTo(map);

      L.Routing.control({
        waypoints: [
          L.latLng(busStand[0], busStand[1]),
          L.latLng(userLat, userLon)
        ],
        routeWhileDragging: false,
        draggableWaypoints: false,
        addWaypoints: false,
        show: false,
        lineOptions: {
          styles: [{color: 'blue', weight: 5}]
        }
      }).addTo(map);
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

components.html(html_code, height=480)
