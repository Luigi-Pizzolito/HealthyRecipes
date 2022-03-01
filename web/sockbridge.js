// Run setup when page is finished loading
window.addEventListener('DOMContentLoaded', (event) => {

    // Handle WebSock Connection to backend
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
        msg = JSON.parse(event.data)
        switch (msg.res) {
            case "echo":
                alert(msg.msg);
                break;
            default:
                alert(`[error] Invalid backend response: ${msg.res}`);
        }

    };


    // Setup UI actions
    document.getElementById("b").addEventListener("click", () => {
        socket.send('{"req":"echo","msg":"' + document.getElementById('s').value + '"}');
    })


});