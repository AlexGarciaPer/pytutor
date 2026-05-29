import requests

SYSTEM_PROMPT = """Eres PyTutor, un asistente experto y paciente 
especializado en enseñar Python a principiantes.
Responde siempre en español, sé claro y usa ejemplos de código cuando ayude."""

historial = []

print("=" * 45)
print("  🐍  PyTutor — Asistente de Python en local")
print("=" * 45)
print("  Escribe 'salir' para terminar")
print("  Escribe 'limpiar' para borrar el historial")
print("=" * 45 + "\n")

while True:
    pregunta = input("Tú: ").strip()
    
    if not pregunta:
        continue
    if pregunta.lower() == "salir":
        print("\n¡Hasta pronto! Sigue practicando Python 🐍")
        break
    if pregunta.lower() == "limpiar":
        historial = []
        print("✓ Historial borrado\n")
        continue

    historial.append({"role": "user", "content": pregunta})

    try:
        respuesta = requests.post("http://localhost:11434/api/chat", json={
            "model": "qwen2.5-coder:3b",
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + historial,
            "stream": False
        })
        mensaje = respuesta.json()["message"]["content"]
        historial.append({"role": "assistant", "content": mensaje})
        print(f"\nPyTutor: {mensaje}\n")

    except Exception as e:
        print(f"\nError: {e}")
        print("Asegúrate de que Ollama está corriendo\n")