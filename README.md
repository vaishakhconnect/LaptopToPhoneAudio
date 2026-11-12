# LaptopToPhoneAudio

![LaptopToPhoneAudio Banner](assets/banner.png)

**Stream your Windows laptop audio directly to your phone over a local network.**

LaptopToPhoneAudio is a lightweight Python-based application that captures audio playing on your laptop and streams it to a phone through a web browser.

## Features

- Real-time laptop audio streaming
- Browser-based interface
- No additional application required on the phone
- Supports local Wi-Fi and USB tethering
- Simple Python and Flask setup

## Screenshots

### Laptop Interface
![Desktop Interface](assets/screenshots/desktop.png)

### Phone Interface
![Phone Interface](assets/screenshots/phone.png)

## Technologies Used

- Python
- Flask
- SoundCard
- NumPy
- HTML, CSS and JavaScript
- Web Audio API

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vaishakhconnect/LaptopToPhoneAudio.git
```

### 2. Open the project folder

```bash
cd LaptopToPhoneAudio
```

### 3. Create a virtual environment

```bash
py -m venv .venv
```

### 4. Activate the environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

### 1. Start the server

```bash
python app.py
```

Keep the terminal running while streaming.

### 2. Open the application on your laptop

Visit:

```text
http://127.0.0.1:5000
```

### 3. Find your laptop's IP address

Open another terminal and run:

```powershell
ipconfig
```

Find the IPv4 address of the network adapter currently connecting your laptop to your phone or Wi-Fi network.

### 4. Connect your phone

Enter the following address in your phone's browser:

```text
http://YOUR_LAPTOP_IP:5000
```

Replace `YOUR_LAPTOP_IP` with the actual laptop IPv4 address.

### 5. Start listening

Play audio on your laptop and use the application on your phone.

## Network Requirements

- Both devices must be connected to the same local network.
- USB tethering or a shared Wi-Fi hotspot can also be used.
- Allow Python through Windows Firewall on private networks if prompted.
- Do not expose the server directly to the public internet.

## Troubleshooting

| Problem | Possible solution |
|---|---|
| Phone cannot open the page | Check that both devices are on the same network |
| Connection refused | Make sure `python app.py` is still running |
| No audio | Check the Windows default playback device |
| Firewall blocks connection | Allow Python on the trusted private network |
| Wrong IP address | Check `ipconfig` again for the active adapter |

## Project Structure

```text
LaptopToPhoneAudio/
│
├── assets/
│   ├── banner.png
│   └── screenshots/
│       ├── desktop.png
│       └── phone.png
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Author

**Vaishakh K**

GitHub: [@vaishakhconnect](https://github.com/vaishakhconnect)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!