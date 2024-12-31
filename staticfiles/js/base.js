const messages = document.querySelectorAll(".message");

console.log(messages)

if (messages.length > 0) {
    messages.forEach((message) => {
        setTimeout(function () {
            message.style.display = "none";
        }, 3500);
    });
}