from flask import Flask
import requests
from flask_cors import CORS


app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/1/<longe>/<lat>',methods=["GET"])
def location(longe,lat):
    res = requests.get(f"https://services.maps.cdtfa.ca.gov/api/taxrate/GetRateByLngLat?Longitude={longe}&Latitude={lat}")
    if res.status_code == 200:
        return res.text
    return "error"

@app.route('/api/2/<address>/<city>/<zip>',methods=["GET"])
def location_by_address(address,city,zip):
    address = "+".join((str(address).lower()).split(" "))
    city = str(city).lower()
    res = requests.get(f"https://services.maps.cdtfa.ca.gov/api/taxrate/GetRateByAddress?address={address}&city={city}&zip={zip}")
    if res.status_code == 200:
        return res.text
    return "error"


if __name__ == "__main__":
    app.run(debug = True)

      
