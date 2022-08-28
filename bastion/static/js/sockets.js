const base_socket_url = 'http://127.0.0.1:5000/';
var socket = io();

// socket = io.connect(base_socket_url + '/live-status');

socket.on('connect', function () {
    console.log('connected');
});

socket.on('status', function (data) {
    console.log(data);
    if (data.msg !== undefined) {
        var el = document.getElementById('status');
        el.innerHTML = data.msg;
    }
});