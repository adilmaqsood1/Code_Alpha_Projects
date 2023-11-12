// static/script.js

function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    document.getElementById("chat-box").innerHTML += "<p><strong>You:</strong> " + userInput + "</p>";
    
    // Send user input to the server and receive the response
    fetch("/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML += "<p><strong>ChatGPTBot:</strong> " + data.response + "</p>";
    });

    // Clear the input field
    document.getElementById("user-input").value = "";
}
