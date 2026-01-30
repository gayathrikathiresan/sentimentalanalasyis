# Face Emotion Demo - Simple Web UI

1. Ensure `best_fer_model.h5` is in this folder (same directory as `app.py`).
2. Create and activate your virtualenv (optional but recommended):

```powershell
python -m venv fer_env
.\\fer_env\\Scripts\\Activate.ps1   # PowerShell
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the app:

```powershell
python app.py
```

5. Open http://127.0.0.1:5000 in your browser, allow camera access, then click "Capture & Predict".

Notes:
- This is a minimal demo for local development. For production use, secure the endpoint and serve via a proper WSGI server.
- If you have a GPU-enabled TensorFlow build, install the appropriate `tensorflow` package.
