// Example data for feedback (replace it with your actual data)
const feedbackData = [
    { id: 1, sender: "Parent 1", message: "Great service! Thank you." },
    { id: 2, sender: "Parent 2", message: "Bus was late today." },
    // Add more entries as needed
];

document.addEventListener("DOMContentLoaded", function () {
    const feedbackList = document.getElementById("feedbackList");

    feedbackData.forEach(entry => {
        const feedbackItem = document.createElement("div");
        feedbackItem.classList.add("feedback-item");
        feedbackItem.innerText = `ID: ${entry.id} | Sender: ${entry.sender}\nMessage: ${entry.message}`;
        feedbackItem.onclick = function() {
            viewFeedbackDetails(entry);
        };

        feedbackList.appendChild(feedbackItem);
    });
});

function viewFeedbackDetails(feedback) {
    // Implement logic to view feedback details
    // For demonstration purposes, let's show an alert with feedback details
    alert(`Feedback ID: ${feedback.id}\nSender: ${feedback.sender}\nMessage: ${feedback.message}`);
}

function goBack() {
    // Implement logic to navigate back
    // For demonstration purposes, let's use the browser's built-in history back function
    window.history.back();
}
