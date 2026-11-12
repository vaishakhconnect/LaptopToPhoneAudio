LAPTOP TO PHONE AUDIO - WINDOWS SETUP
=====================================

WHAT IT DOES
------------
Streams the laptop's default playback audio (YouTube, VLC, music players, etc.)
to a web page opened on your Android phone. The phone plays the stream through
its speaker or connected headphones.

REQUIREMENTS
------------
- Windows 10/11 laptop
- Python 3.10 or newer
- VS Code
- Android phone with Chrome
- Both devices connected to the same local network (phone hotspot is fine)

SETUP IN VS CODE
----------------
1. Extract this ZIP file.
2. Open the extracted LaptopToPhoneAudio folder in VS Code.
3. Open Terminal > New Terminal.
4. Run these commands:

   python -m venv venv
   venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt

START THE SERVER
----------------
Run:

   python app.py

Find the laptop's Wi-Fi IPv4 address:
   ipconfig

Look under the Wi-Fi adapter for "IPv4 Address", for example:
   192.168.43.120

On your phone, connected to the same hotspot/Wi-Fi, open:
   http://192.168.43.120:5000

Replace the example IP with the laptop's actual IPv4 address.
Tap Play on the phone, then play audio on the laptop.

WINDOWS FIREWALL
----------------
If Windows asks whether Python can communicate on the network, allow access
on Private networks. If the phone cannot connect, check that both devices are
on the same hotspot/Wi-Fi and that the network is set to Private in Windows.

TROUBLESHOOTING
---------------
- No audio: check that the laptop's correct output device is selected as the
  Windows default playback device.
- Connection refused: make sure "python app.py" is still running.
- Phone cannot open page: verify the laptop IPv4 address and firewall settings.
- Choppy sound: keep both devices close to the Wi-Fi hotspot and close other
  heavy network activity.
- Stop streaming by tapping Stop or pressing Ctrl+C in the VS Code terminal.

NOTES
-----
- Internet is not needed once the local network is established.
- This prototype captures the default Windows playback device, not an
  individual application's audio.
- Audio is transmitted as uncompressed 44.1 kHz, 16-bit stereo PCM.
- Latency and reliability depend on the local network and phone browser.
