let map;

function initMap() {
    // Initialize Google Maps
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -1.286389, lng: 36.817223 }, // Set the initial center to Nairobi, Kenya
        zoom: 15, // Adjust the initial zoom level as needed
    });

    // Add a marker for the bus location (example)
    const busMarker = new google.maps.Marker({
        position: { lat: -1.286389, lng: 36.817223 },
        map: map,
        title: 'Bus Location',
    });

    // You can update the marker position dynamically based on real-time data
    // Example: setInterval(() => updateMarkerPosition(busMarker), 5000);
}

// Example function to update marker position (simulate real-time updates)
function updateMarkerPosition(marker) {
    const newPosition = {
        lat: marker.getPosition().lat() + (Math.random() - 0.5) * 0.01,
        lng: marker.getPosition().lng() + (Math.random() - 0.5) * 0.01,
    };

    marker.setPosition(newPosition);
}
