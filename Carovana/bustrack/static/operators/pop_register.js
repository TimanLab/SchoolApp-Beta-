// Example data for the pop register (replace it with your actual data)
const popRegisterData = [
    { name: "Child 1" },
    { name: "Child 2" },
    // Add more entries as needed
];

document.addEventListener("DOMContentLoaded", function () {
    const popButtonsContainer = document.getElementById("popButtonsContainer");

    popRegisterData.forEach(entry => {
        const popButton = document.createElement("button");
        popButton.classList.add("pop-button");
        popButton.innerText = entry.name;

        const leftClickable = document.createElement("div");
        leftClickable.classList.add("pop-button", "left");
        leftClickable.innerText = "No";
        leftClickable.onclick = function() {
            togglePopStatus(popButton, "no");
        };

        const rightClickable = document.createElement("div");
        rightClickable.classList.add("pop-button", "right");
        rightClickable.innerText = "Yes";
        rightClickable.onclick = function() {
            togglePopStatus(popButton, "yes");
        };

        popButton.appendChild(leftClickable);
        popButton.appendChild(rightClickable);

        popButtonsContainer.appendChild(popButton);
    });
});

function togglePopStatus(popButton, status) {
    // Toggle the status when a pop button is clicked
    if (status === "no") {
        popButton.classList.remove("right");
        popButton.classList.add("left");
    } else {
        popButton.classList.remove("left");
        popButton.classList.add("right");
    }

    // Remove the button after clicking
    popButton.remove();
}

function goBack() {
    // Implement logic to navigate back
    // For demonstration purposes, let's use the browser's built-in history back function
    window.history.back();
}
