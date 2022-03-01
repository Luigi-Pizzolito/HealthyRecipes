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
├── app
│   └── *Application Function Libraries and Code*
├── db
│   ├── foodcomposition.csv
│   └── recipes.csv
├── web
│   ├── bootstrap
│   │   ├── bootstrap.bundle.min.js
│   │   └── bootstrap.min.css
│   ├── index.html
│   └── sockbridge.js
├── backend
│   ├── embeddedbrowser.qml
│   ├── sockserver.py
│   └── webserver.py
├── LICENSE
├── README.md
└── app.py
```