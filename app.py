from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

SYSTEM_PROMPT = """Eres PyTutor, un asistente experto y paciente 
especializado en enseñar Python a principiantes.
Responde siempre en español, sé claro y usa ejemplos de código cuando ayude."""

historial = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global historial
    
    datos = request.json
    pregunta = datos.get("mensaje", "")
    
    if pregunta.lower() == "limpiar":
        historial = []
        return jsonify({"respuesta": "✓ Historial borrado"})

    historial.append({"role": "user", "content": pregunta})

    try:
        respuesta = requests.post("http://localhost:11434/api/chat", json={
            "model": "qwen2.5-coder:3b",
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + historial,
            "stream": False
        })
        mensaje = respuesta.json()["message"]["content"]
        historial.append({"role": "assistant", "content": mensaje})
        return jsonify({"respuesta": mensaje})

    except Exception as e:
        return jsonify({"respuesta": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)