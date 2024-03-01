// Example data for the register (replace it with your actual data)
const registersData = [
    { id: 1, date: "2024-02-01", operator: "Operator 1", status: "submitted" },
    { id: 2, date: "2024-02-02", operator: "Operator 2", status: "in_progress" },
    // Add more entries as needed
];

document.addEventListener("DOMContentLoaded", function () {
    const registersList = document.getElementById("registersList");

    registersData.forEach(entry => {
        const registerItem = document.createElement("div");
        registerItem.classList.add("register-item");
        registerItem.innerText = `Register ID: ${entry.id} | Date: ${entry.date} | Operator: ${entry.operator} | Status: ${entry.status}`;
        registerItem.onclick = function() {
            viewRegisterDetails(entry);
        };

        registersList.appendChild(registerItem);
    });
});

function viewRegisterDetails(register) {
    // Implement logic to view register details
    // For demonstration purposes, let's show an alert with register details
    alert(`Register ID: ${register.id}\nDate: ${register.date}\nOperator: ${register.operator}\nStatus: ${register.status}`);
}

function goBack() {
    // Implement logic to navigate back
    // For demonstration purposes, let's use the browser's built-in history back function
    window.history.back();
}
