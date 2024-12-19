const message = document.getElementById("pop-up");

    if (message) {
        // Set a timeout to hide the message after 5 seconds
        setTimeout(function () {
            message.style.display = "none";
        }, 4000);
    }