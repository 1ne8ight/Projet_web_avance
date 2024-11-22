var socket = io.connect("http://127.0.0.1:5000");

socket.on("connection", function (msg) {
  //    alert('Connection established');
  location.reload(true);
});


