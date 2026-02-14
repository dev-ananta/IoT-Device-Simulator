// Configuration (Constants)
const BROKER_URL = 'wss://test.mosquitto.org:8081';
const TOPIC_SUB = 'iot/vdev-001/telemetry';
const TOPIC_PUB = 'iot/vdev-001/command';

// State (Lets)
let client = null;
let ledState = false;
let fanState = false;

// Chart Setup
const ctx = document.getElementById('tempChart').getContext('2d');
const tempChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature (˚C)',
            data: [],
            borderColor: '#e94560',
            tension: 0.4
        }]
    },

    options: {
        animation: false
    }
});

// MQTT Connection
function connect() {
    console.log("Connecting to Broker...");
    client = mqtt.connect(BROKER_URL);

    client.on('connect', () => {
        document.getElementById('connection-staatus').innerText = "Connected";
        document.getElementById('connection-staatus').className = "status-indicator connected";

        console.log("Connected! Subscribing...");

        client.subscribe(TOPIC_SUB);
    });

    client.on('message', (topic, message) => {
        const payload = JSON.parse(message.toString());
        updateDashboard(payload);
    });

    client.on('error', (err) => {
        console.error("Connection Error: ", err);
        logToConsole("Connection Error: " + err);
    });
}

// UI Update Functions

function updateDashboard (data) { // Dashboard Updater
    // Update Text
    document.getElementById('temp-value').innerText = data.sensors.temperature + " ˚C"; // Update Temperature
    document.getElementById('hum-value').innerText = data.sensors.humidity + " %"; // Update Humidity

    // Update Status Text
    const statusText = `LED: ${data.status.led ? 'ON' : 'OFF'} | Fan: ${data.status.fan}`;
    document.getElementById('actuator-status').innerText = statusText;

    // Log
    logToConsole(`RX: Temp ${data.sensors.temperature} | LED ${data.status.led}`);

    // Update Chart
    const timeLabel = new Date(data.timestamp).toLocaleTimeString();
    addDataToChart(timeLabel, data.sensors.temperature);
}

function addDataToChart (label, data) { // Chart Updater
    tempChart.data.labels.push(label);
    tempChart.data.datasets[0].data.shift();

    // Keep Chart Clean
    if (tempChart.data.labels.length > 20) {
        tempChart.data.labels.shift();
        tempChart.data.datasets[0].data.shift();
    }

    tempChart.update();
}

function logToConsole (message) { // Console Logger
    // Create Log Entry
    const box = document.getElementById('console-output');
    const entry = document.creareElement('div');
    // Style Log Entry
    entry.className = 'log-entry';
    entry.innerTex = `> ${msg}`;
    // Add to Console
    box.prepend(entry);
}

// Control Functions

function toggleLed () { // LED Toggle
    ledState = !ledState;
    sendCommand();
}

function toggleFan () { // Fan Toggle
    fanState = !fanState;
    sendCommand();
}

function sendCommand () {
    // Ensure Connection
    if (!client) return;
    // Create Payload
    const payload = JSON.stringify({
        led: ledState,
        fan: fanState
    });
    // Publish Command
    client.publish(TOPIC_PUB, payload);
    logToConsole(`TX Command: ${payload}`);
}

connect(); // Initialize System