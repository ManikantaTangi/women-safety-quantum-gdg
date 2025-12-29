const sosBtn = document.getElementById("sosBtn");
const home = document.getElementById("home");
const mapContainer = document.getElementById("mapContainer");
const statusText = document.getElementById("statusText");
const etaText = document.getElementById("etaText");

let map;

sosBtn.addEventListener("click", () => {
  if (!navigator.geolocation) {
    alert("Geolocation not supported");
    return;
  }

  navigator.geolocation.getCurrentPosition(async (pos) => {
    const lat = pos.coords.latitude;
    const lng = pos.coords.longitude;

    console.log("LIVE LOCATION:", lat, lng);

    try {
     const res = await fetch("https://women-safety-backend-gdg.onrender.com/sos", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          victim_lat: lat,
          victim_lng: lng
        })
      });

      const data = await res.json();
      console.log("BACKEND RESPONSE:", data);

      // ---------------- UI SWITCH ----------------
      home.classList.add("hidden");
      mapContainer.classList.remove("hidden");

      statusText.innerText = data.status;

      const bestIndex = data.optimal_route_index;
      const bestETA = data.routes[bestIndex].eta_minutes;

      etaText.innerText = `Optimal ETA: ${bestETA} minutes`;

      // ---------------- MAP INIT ----------------
      if (!map) {
        map = L.map("map").setView([lat, lng], 13);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution: "© OpenStreetMap contributors"
        }).addTo(map);

        // IMPORTANT: fix hidden div issue
        setTimeout(() => {
          map.invalidateSize();
        }, 200);
      }

      // ---------------- MARKERS ----------------
      L.marker([
        data.victim_location.lat,
        data.victim_location.lng
      ])
        .addTo(map)
        .bindPopup("Victim Location");

      L.marker([
        data.police_location.lat,
        data.police_location.lng
      ])
        .addTo(map)
        .bindPopup("Police Station");

      // ---------------- ROUTES ----------------
       data.routes.forEach((route, index) => {
         const coords = route.geometry.coordinates.map(c => [c[1], c[0]]);

        L.polyline(coords, {
          color: index === bestIndex ? "#2ecc71" : "#b0b0b0", // GREEN optimal
          weight: index === bestIndex ? 6 : 3,
          opacity: index === bestIndex ? 1.0 : 0.6
        }).addTo(map);
       });


    } catch (err) {
      console.error(err);
      alert("Backend not reachable");
    }
  }, () => {
    alert("Location permission denied");
  });
});
