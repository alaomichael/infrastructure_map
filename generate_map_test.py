import folium
import pandas as pd

# Sample data
data = pd.DataFrame({
    'name': ['Hospital A', 'School B', 'Road C'],
    'latitude': [9.0820, 9.0720, 9.0620],
    'longitude': [8.6753, 8.6653, 8.6553]
})

# Create a base map
m = folium.Map(location=[9.0820, 8.6753], zoom_start=6)

# Add infrastructure data to the map
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map
m.save('static/infrastructure_map.html')

