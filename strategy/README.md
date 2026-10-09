# El Vals de la Novia - Dashboard de Estrategia

Dashboard interactivo en Streamlit para el seguimiento del plan estratégico de Instagram de @elvalsdelanovia.

## Características

- **Checklist interactivo**: Tareas organizadas por semana y día con progreso visual
- **Plan Estratégico**: Documentación completa del plan de rehabilitación
- **Análisis de Competidores**: Estudio de mercado del nicho bodas en España
- **Diseño mobile-first**: Optimizado para uso en móvil
- **Persistencia local**: El progreso se guarda automáticamente

## Ejecución Local

### Requisitos
- Python 3.8+
- pip

### Instalación

```bash
# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
streamlit run app.py
```

La app se abrirá en `http://localhost:8501`

## Despliegue en Streamlit Cloud (Gratuito)

### Paso 1: Subir a GitHub

```bash
# Si no tienes repositorio aún
git init
git add .
git commit -m "Initial commit: El Vals de la Novia dashboard"

# Crear repo en GitHub y conectar
git remote add origin https://github.com/TU_USUARIO/evdln.git
git push -u origin main
```

### Paso 2: Desplegar en Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con GitHub
3. Click en "New app"
4. Selecciona:
   - Repository: `TU_USUARIO/evdln`
   - Branch: `main`
   - Main file path: `app.py`
5. Click en "Deploy!"

La app estará disponible en: `https://TU_USUARIO-evdln-app-XXXX.streamlit.app`

### Nota sobre Persistencia

**Localmente**: El progreso se guarda en `.checklist_state.json`

**En Streamlit Cloud**: Por defecto, el progreso NO se persiste entre sesiones porque Streamlit Cloud no tiene sistema de archivos persistente.

Para persistencia en la nube, consulta la sección "Persistencia con Google Sheets" abajo.

## Persistencia con Google Sheets (Opcional)

Para mantener el progreso sincronizado en Streamlit Cloud:

### Paso 1: Crear Google Sheet

1. Ve a [sheets.google.com](https://sheets.google.com)
2. Crea una nueva hoja llamada "evdln_state"
3. Copia el ID de la URL (la parte entre `/d/` y `/edit`)

### Paso 2: Crear Service Account

1. Ve a [Google Cloud Console](https://console.cloud.google.com)
2. Crea un proyecto nuevo o usa uno existente
3. Habilita "Google Sheets API"
4. Ve a "Credentials" → "Create Credentials" → "Service Account"
5. Descarga el archivo JSON de credenciales

### Paso 3: Compartir la Hoja

1. Abre tu Google Sheet
2. Click en "Compartir"
3. Añade el email del service account (termina en `@...iam.gserviceaccount.com`)
4. Dale permisos de "Editor"

### Paso 4: Configurar Streamlit Cloud

1. En tu app de Streamlit Cloud, ve a "Settings" → "Secrets"
2. Añade los secrets:

```toml
[gcp_service_account]
type = "service_account"
project_id = "tu-project-id"
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "...@...iam.gserviceaccount.com"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"

[sheets]
spreadsheet_id = "TU_SPREADSHEET_ID"
```

### Paso 5: Modificar app.py

Descomentar las funciones de Google Sheets en `app.py` (si se añade esta funcionalidad en futuras versiones).

## Estructura del Proyecto

```
evdln/
├── app.py                    # App principal de Streamlit
├── requirements.txt          # Dependencias
├── README.md                 # Este archivo
├── .gitignore               # Archivos ignorados
├── .streamlit/
│   └── config.toml          # Configuración de tema
└── docs/
    └── plans/
        ├── 2026-01-17-el-vals-de-la-novia-plan.md
        ├── 2026-01-17-checklist-semanas-1-4.md
        └── 2026-01-17-analisis-competidores.md
```

## Uso

### Tab "Checklist"
- Marca las tareas completadas tocando los checkboxes
- El progreso se muestra por semana
- Las tareas tienen tiempo estimado

### Tab "Plan Estratégico"
- Lee el plan completo de rehabilitación de la cuenta
- Fases, estrategias y proyecciones

### Tab "Competidores"
- Análisis de cuentas similares
- Oportunidades y gaps identificados

## Notas Técnicas

- **Mobile-first**: CSS optimizado para pantallas táctiles
- **Colores**: Gradiente rosado-morado acorde con estética de bodas
- **Checkboxes grandes**: Fáciles de tocar en móvil
- **Progreso visual**: Barras y métricas claras

## Soporte

Desarrollado para @elvalsdelanovia
Enero 2026
