from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from quantum import quantum_optimize
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend running"}

# ---------------------------
# OSRM: get real routes
# ---------------------------
def get_osrm_routes(src_lat, src_lng, dst_lat, dst_lng):
    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{src_lng},{src_lat};{dst_lng},{dst_lat}"
        f"?alternatives=true&overview=full&geometries=geojson"
    )

    r = requests.get(url, timeout=10)
    data = r.json()

    return data["routes"]


@app.post("/sos")
def sos(data: dict = Body(...)):
    print("RECEIVED SOS:", data)

    victim_lat = data["victim_lat"]
    victim_lng = data["victim_lng"]

    # 🔹 Simulated nearby police station (demo-safe)
    police_lat = victim_lat + 0.02
    police_lng = victim_lng - 0.02

    # ---------------------------
    # Classical preprocessing
    # ---------------------------
    routes = get_osrm_routes(
        police_lat, police_lng,
        victim_lat, victim_lng
    )

    etas = [r["duration"] / 60 for r in routes]  # minutes
    max_eta = max(etas)
    costs = [e / max_eta for e in etas]

    print("ETAs:", etas)
    print("Costs:", costs)

    # ---------------------------
    # Quantum optimization
    # ---------------------------
    best_index, histogram = quantum_optimize(costs)

    print("Quantum histogram:", histogram)
    print("Best route index:", best_index)

    # ---------------------------
    # Classical post-processing
    # ---------------------------
    return {
        "status": "Police dispatched",
        "police_location": {
            "lat": police_lat,
            "lng": police_lng
        },
        "victim_location": {
            "lat": victim_lat,
            "lng": victim_lng
        },
        "optimal_route_index": best_index,
        "routes": [
            {
                "eta_minutes": round(r["duration"] / 60, 2),
                "geometry": r["geometry"]
            }
            for r in routes
        ]
    }
