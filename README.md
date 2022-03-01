# HealthyRecipes
A food composition DB aggregator and requirement-based recipes generator for a Python software engineering design course at Beijing Institute of Technology.

## Application Components
- QT/PySide GUI displays embedded web-browser.
- Bottle serves web app content.
- WebsocketServer handles web app system integration.
- Python code runs main program functions.
## Directory Structure
```
HealthyRecipes
├── backend
│   ├── embeddedbrowser.qml
│   ├── sockserver.py
│   ├── webserver.py
│   ├── app
│   │   ├── requesthandler.py
│   │   └── *Application Function Libraries and Code*
│   └── db
│       ├── foodcomposition.csv
│       └── recipes.csv
├── web
│   ├── bootstrap
│   │   ├── bootstrap.bundle.min.js
│   │   └── bootstrap.min.css
│   ├── index.html
│   └── sockbridge.js
├── LICENSE
├── README.md
└── app.py
```

## Dependencies
- QT/PySide6
- Bottle
- websocket-server