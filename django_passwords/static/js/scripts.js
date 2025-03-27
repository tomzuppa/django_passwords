document.addEventListener("DOMContentLoaded", function () {
    // Select all alert messages
    let alerts = document.querySelectorAll(".alert");

    // Loop through each message and set a timeout to fade out
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = "opacity 0.8s ease-out"; // Smooth fade-out effect
            alert.style.opacity = "0"; // Start fading

            // Ensure display is removed only after the fade-out is complete
            setTimeout(function () {
                if (alert.style.opacity === "0") {
                    alert.style.display = "none";
                }
            }, 800); // Wait for transition (same duration as CSS transition)
        }, 10000); // 10 seconds before disappearing
    });
});
