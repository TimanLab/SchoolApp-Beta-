// Example data for buses (replace it with your actual data)
const busesData = [
    { id: 1, name: "Bus 1" },
    { id: 2, name: "Bus 2" },
    // Add more entries as needed
];

document.addEventListener("DOMContentLoaded", function () {
    const busSelector = document.getElementById("busSelector");
    const mileageValue = document.getElementById("mileageValue");

    // Populate bus options
    busesData.forEach(bus => {
        const option = document.createElement("option");
        option.value = bus.id;
        option.innerText = bus.name;
        busSelector.appendChild(option);
    });

    // Set initial mileage value
    updateMileage();

    // Event listener for changing bus selection
    busSelector.addEventListener("change", function () {
        updateMileage();
    });
});

function updateMileage() {
    const selectedBusId = document.getElementById("busSelector").value;
    const mileage = getBusMileage(selectedBusId);
    document.getElementById("mileageValue").innerText = mileage + " km";
}

function getBusMileage(busId) {
    // In a real-world scenario, you would fetch this data from a server
    // Here, a simple example is used with a fixed mileage value
    return Math.floor(Math.random() * 1000) + 1;
}

function goBack() {
    // Implement logic to navigate back
    // For demonstration purposes, let's use the browser's built-in history back function
    window.history.back();
}
