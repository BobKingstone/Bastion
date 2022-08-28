// Globals
const base_api_url = 'http://127.0.0.1:5000/';
var calling = false;
const agentUL = document.getElementById('agents');


// API Functions

async function getstatus() {
    var url = base_api_url + 'status';
    calling = true;

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            UpdateStatusText(data);
        })
        .catch((error) => {
            console.log(error);
            UpdateStatusText({ status: 'Error' });
        });

    calling = false;
}

async function startSimulation() {
    var url = base_api_url + 'simulate';
    const response = await fetch(url);

    var data = await response.json();
    console.log(data);
}

async function stopSimulation() {
    var url = base_api_url + 'end_simulation';
    const response = await fetch(url);

    var data = await response.json();
    console.log(data);
}

async function getAgents() {
    var url = base_api_url + 'agents';
    const response = await fetch(url);
    var data = await response.json();

    console.log(data);

    agentUL.innerHTML = '';
    var docFragment = document.createDocumentFragment();

    for (var i = 0; i < data.length; i++) {
        var li = document.createElement('li');
        li.textContent = data[i].id + " " + data[i].type + " " + data[i].status;
        docFragment.appendChild(li);
    }

    agentUL.appendChild(docFragment);
}

function UpdateStatusText(msg) {
    console.log(msg);
    var el = document.getElementById('status');
    el.innerHTML = msg.status;
}

getstatus();
getAgents();

const startButton = document.getElementById('start').onclick = startSimulation;
const stopButton = document.getElementById('stop').onclick = stopSimulation;
