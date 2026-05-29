# 🐍 PyTutor — Chatbot local de Python

Chatbot local especializado en responder dudas sobre Python.
Corre completamente en tu PC sin necesidad de internet ni APIs de pago.

## Tecnologías

- **Ollama** — motor para correr modelos de IA en local
- **qwen2.5-coder:3b** — modelo especializado en código
- **Flask** — servidor web en Python
- **HTML/CSS/JS** — interfaz visual del chat

## Estructura del proyecto
pytutor/
├── templates/
│   └── index.html      # Interfaz visual del chatbot
├── app.py              # Servidor Flask y lógica del chat
├── chatbot.py          # Versión original en terminal
└── arrancar.bat        # Lanzador automático (Windows)

## Requisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado

## Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/AlexGarciaPer/pytutor.git
cd pytutor
```

### 2. Instala las dependencias
```bash
pip install flask requests
```

### 3. Descarga el modelo
```bash
ollama pull qwen2.5-coder:3b
```

## Uso

### Opción A — Lanzador automático (Windows)
Doble click en `arrancar.bat`

### Opción B — Manual
```bash
python app.py
```
Abre el navegador en `http://127.0.0.1:5000`

## Comandos del chat

| Comando | Acción |
|---|---|
| `limpiar` | Borra el historial de conversación |

## Cómo funciona
Navegador (HTML)
↕
Flask (app.py)        ← gestiona el historial y las rutas
↕
Ollama API            ← corre el modelo de IA en local
↕
qwen2.5-coder:3b        ← responde las preguntas de Python

