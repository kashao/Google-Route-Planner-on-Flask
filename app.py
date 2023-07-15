from flask import Flask, render_template, request
import googlemaps
import yaml

app = Flask(__name__)
with open("Config.yml", "r", encoding="UTF-8") as f:
    config = yaml.safe_load(f)
api_key = config["GoogleMap"]["API"]
gmaps = googlemaps.Client(key=api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        locations = request.form.get('locations').split('\n')
        print(locations)
        locations = [loc.strip() for loc in locations if loc.strip()]
        print(locations)
        if not locations: # 如果地點列表是空的，返回錯誤訊息
            return "你必須輸入至少一個地點！"
        directions = []

        for i in range(len(locations) - 1):
            origin = locations[i]
            destination = locations[i + 1]
            try:
                directions_result = gmaps.directions(origin, destination, departure_time='now')
                # Extract the coordinates from the result
                origin_coords = directions_result[0]['legs'][0]['start_location']
                destination_coords = directions_result[0]['legs'][0]['end_location']
                distance = directions_result[0]['legs'][0]['distance']['text']
                duration = directions_result[0]['legs'][0]['duration']['text']
            except googlemaps.exceptions.ApiError:
                print(f"警告: 無法找到地點 '{locations[i]}' 或 '{locations[i + 1]}'。")
                origin_coords, destination_coords, distance, duration = None, None, None, None
            # Add the direction to the list
            directions.append({
                'index': i,
                'origin_name': origin.strip(),
                'destination_name': destination.strip(),
                'origin': origin_coords,
                'destination': destination_coords,
                'distance': distance,
                'duration': duration
            })

        # Extract all origin_name, destination_name, origin, and destination
        locations = [{'name': d['origin_name'], 'map': d['origin']} for d in directions]
        locations += [{'name': d['destination_name'], 'map': d['destination']} for d in directions]

        # Remove duplicates and None maps
        unique_locations = []
        seen = set()
        print(locations)
        for loc in locations:
            if loc['name'] not in seen and loc['map'] is not None:
                seen.add(loc['name'])
                unique_locations.append(loc)

        # Pass the directions to the results template
        return render_template('results.html', directions=directions, locations=unique_locations)
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)