function submitFeedback() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    // Add your logic to handle the feedback submission (e.g., AJAX request to the server)

    // For demonstration purposes, let's show an alert for successful submission
    alert("Feedback submitted successfully. Thank you!");
    // You can implement further logic like clearing the form or redirecting the user
}

function goBack() {
    // Implement logic to navigate back
    // For demonstration purposes, let's use the browser's built-in history back function
    window.history.back();
}
