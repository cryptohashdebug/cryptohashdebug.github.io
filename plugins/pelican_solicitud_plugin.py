from pelican import signals
import re

# Función que detecta y reemplaza el campo <solicitud> en el contenido
def process_solicitud(instance):
    if not instance._content:
        return

    # Buscar el campo <solicitud> en el contenido del artículo/página
    pattern = r"<solicitud>(.*?)</solicitud>"
    matches = re.findall(pattern, instance._content, re.DOTALL)

    if not matches:
        return

    for solicitud_url in matches:
        # Código JS a insertar que hace una petición fetch a la URL indicada
        js_code = f"""
        <div id="api-response">Cargando datos...</div>
        <script>
        fetch("{solicitud_url.strip()}")
            .then(response => response.json())
            .then(data => {{
                document.getElementById("api-response").textContent = JSON.stringify(data, null, 2);
            }})
            .catch(error => {{
                document.getElementById("api-response").textContent = "Error al cargar los datos";
                console.error("Error en fetch:", error);
            }});
        </script>
        """

        # Reemplazar el bloque <solicitud>...</solicitud> por el código JS
        instance._content = re.sub(pattern, js_code, instance._content, flags=re.DOTALL)

# Registrar la función para que actúe sobre el contenido procesado antes de generar HTML
def register():
    signals.content_object_init.connect(process_solicitud)
