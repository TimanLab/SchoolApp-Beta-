// Example data for register (replace it with your actual data)
let registerData = [
    { id: 1, child: "Child 1", present: true },
    { id: 2, child: "Child 2", present: false },
    // Add more entries as needed
];

document.addEventListener("DOMContentLoaded", function () {
    const registerList = document.getElementById("registerList");

    displayRegister();

    function displayRegister() {
        registerList.innerHTML = ""; // Clear the list before displaying again

        registerData.forEach(entry => {
            const registerItem = document.createElement("div");
            registerItem.classList.add("register-item");
            registerItem.innerText = `ID: ${entry.id} | Child: ${entry.child} | Present: ${entry.present ? 'Yes' : 'No'}`;
            registerList.appendChild(registerItem);
        });
    }

    function submitExcluded() {
        // Get the names of excluded children
        const excludedChildren = registerData
            .filter(entry => !entry.present)
            .map(entry => entry.child);

        // In a real-world scenario, you would submit this information to operators
        alert(`Excluded Children: ${excludedChildren.join(', ')}`);
    }

    function goBack() {
        // Implement logic to navigate back
        // For demonstration purposes, let's use the browser's built-in history back function
        window.history.back();
    }
});
