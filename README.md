# El Vals de la Novia — plan de estrategia

La aplicación histórica de Streamlit, sus documentos y datasets están en
[`strategy/`](strategy/README.md). Para usarla localmente:

```sh
cd strategy
streamlit run app.py
```

El repositorio independiente `vals-novia-landing/` se conserva fuera del control
de versiones de este proyecto. No es un submódulo ni se incluye en sus commits.

El traslado mantiene el estado local de la checklist en
`strategy/.checklist_state.json`, ignorado por Git. Se conserva también la copia
anterior de la raíz para poder comparar o recuperar el estado.
