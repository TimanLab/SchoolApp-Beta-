function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Add your authentication logic here
    // Example: You can use AJAX to send a login request to the server

    // For demonstration purposes, let's just show an alert for successful login
    alert("Login successful. Redirecting to dashboard...");
    // Redirect to the appropriate dashboard based on the user's role
    // window.location.href = '/dashboard'; 
}
