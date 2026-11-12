from flask import Flask, render_template, Response
import soundcard as sc
import numpy as np

app = Flask(__name__)

SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK_SIZE = 2048


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/audio")
def audio():
    def generate():
        speaker = sc.default_speaker()
        if speaker is None:
            raise RuntimeError("No default Windows playback device was found.")

        # Capture the audio sent to the laptop's default playback device.
        loopback = sc.get_microphone(
            id=str(speaker.name),
            include_loopback=True
        )

        with loopback.recorder(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS
        ) as recorder:
            while True:
                data = recorder.record(numframes=BLOCK_SIZE)

                # Convert float audio (-1.0 to 1.0) to little-endian 16-bit PCM.
                data = np.clip(data, -1.0, 1.0)
                pcm = (data * 32767).astype("<i2")
                yield pcm.tobytes()

    return Response(
        generate(),
        mimetype="application/octet-stream",
        headers={
            "Cache-Control": "no-store",
            "X-Content-Type-Options": "nosniff"
        }
    )


if __name__ == "__main__":
    print("Laptop-to-phone audio server starting...")
    print("Open this computer's Wi-Fi IPv4 address on your phone, e.g.")
    print("http://192.168.1.100:5000")
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)
