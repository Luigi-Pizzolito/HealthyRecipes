// Connect to websocket backend
let socket = new WebSocket("ws://0.0.0.0:8157");
// Error handling
socket.onclose = function (event) {
    if (!event.wasClean) {
        alert('[close] Connection died');
    }
};
socket.onerror = function (error) {
    alert(`[error] ${error.message}`);
};

socket.onopen = function (event) {
    alert("[open] Connection established");
    // alert("Sending to server");
    // socket.send("My name is John");
};

socket.onmessage = function (event) {
    alert(`[message] Data received from server: ${event.data}`);
};