# Virtual IoT Device Simulator

## Project Specifications

### Repository Structure

```
virtual-iot-sim/
├── device/
│   ├── main.py - The Microcontroller Logic
│   └── requirements.txt - Python dependencies
├── index.html - The Dashboard UI
├── styles.css - Styling
├── app.js - Dashboard Logic (MQTT over WebSockets)
├── LICENSE - Licensing Information
└── README.md - Instructions
```

### File Purposes

- `index.html`: Defines Dashboard UI Structure; Additionally It Loads MQTT & Chart.js Libraries.
- `styles.css`: Manages Styling & Visual Appearance of IoT Device Simulator.
- `app.js`: Provides Logic for the Dashboard & Handles Connecting to MQTT Broker. Also Updares the Real-time Charts & Publishing Commands Back to the Device.

## Installation Guide

### Prerequisites

- **Python**: Ensure you have Python installed. (Version 3.x)
```bash
python --version # Check installed version already installed but unsure of version.
```
- **Code Editor**: VS Code (Preferably), Sublime Text, or even Notepad.

### Install
1. Copy the Repository to Documents or Desktop.
2. Install Python Dependencies in Terminal.
```bash
cd path/to/IoT-Device-Simulator/device
pip install paho-mqtt # Use pip3 if you're using macOS.
```

## Utilization Guide (Local)

### Launch Dashboard

1. Go to the `IoT-Device-Simulator` folder by running this command in Terminal.
```bash
cd path/to/IoT-Device-Simulator
```
2. Double-click `index.html`.
- It should open in your primary web-browser. I'd reccomend either using Zen or a Chromium browser.
3. **Status Check**: Look at the top right.
- If it says **"Connected"** (Green), the dashboard is listening for data.
- If it says **"Disconnected"** (Red), refresh the page or check your internet connection.

### Launch Device

1. Go to the `device` folder by running this command in Terminal.
```bash
cd path/to/IoT-Device-Simulator/device
```
2. Run this command in Terminal
```bash
python main.py # Use python3 if you're using macOS.
```
3. **Observe**: You should see logs like this one:
- ```[TX] Sent: {'temperature': 22.0, ...}```

## Utilization Guide (Reciever & Broadcaster | Global)

### Open Dashboard
- The dashboard is hosted on GitHub Pages at this URL: dev-ananta.github.io/IoT-device-simulator
- The dashboard connects to your computer by acting as a reciever while your computer acts as a broadcaster for the files in the `device` folder.

### Launch Device

1. Go to the `device` folder by running this command in Terminal.
```bash
cd path/to/IoT-Device-Simulator/device
```
2. Run this command in Terminal
```bash
python main.py # Use python3 if you're using macOS.
```
3. **Observe**: You should see logs like this one:
- ```[TX] Sent: {'temperature': 22.0, ...}```

## Testing

1. **Watch the Graph**: On your browser, you should see the temperature line begin to draw.
2. **Send a Command**: Click the **"Toggle LED"** button on the web page.
3. **Verify Feedback**:
- Look at your **Terminal**: You should see ```[ACTUATOR] LED switch ON```.
-  Look at the **Graph**: The temperature should begin to rise slowly (simulating gradual heating).
-  Click **"Toggle Fan"**: The temperature should begin to drop (simulating cooling).

## Goal

This project aims to **simulate** the following:
- Microcontroller Behavior
- Sensor Inputs
- MQTT Communication
- Web Dashboard

## Project Details

**Domain**: Software + Embedded Systems (Simulated)
**Uniqueness**: Very High

## Roadmap

- **Commit 1**: Create Repository Structure & Update `README.md`.
- **Commit 2**: Write `index.html` & `styles.css`.
- **Commit 3**: Write `app.js`.
- **Commit 4**: Update `README.md`.
- **Commit 5**: Write `main.py`.
- **Commit 6**: Write `requirements.txt`.
- **Commit 7**: Update `README.md`.
- **Commit 8**: Test & Debug.
- **Commit 9**: Publish MVP.
- **Commit 10**: Ask for Feedback.
- **Commit 11**: Improve Project.
- **Commit 12**: Finalize for Shipping to "Scraps by Hack Club".

#### Signed by Ananta the Developer
