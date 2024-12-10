import subprocess

# Запуск FastAPI
fastapi_process = subprocess.Popen(["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"])

# Запуск Streamlit
streamlit_process = subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

try:
    fastapi_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    fastapi_process.terminate()
    streamlit_process.terminate()
