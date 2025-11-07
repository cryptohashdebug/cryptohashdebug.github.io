from pelican import signals
import re
import json

def process_solicitud(instance):
    if not instance._content:
        return

    # Patrón para captar el bloque <solicitud> con JSON interno
    pattern = r"<solicitud>(.*?)</solicitud>"
    matches = re.findall(pattern, instance._content, re.DOTALL)

    if not matches:
        return

    for raw_content in matches:
        try:
            # Se espera que el contenido sea un JSON describiendo la petición
            # Ejemplo:
            # {
            #   "method": "POST",
            #   "url": "https://api.example.com/data",
            #   "headers": {"Content-Type": "application/json"},
            #   "body": {"key": "value"}
            # }
            request_spec = json.loads(raw_content.strip())
        except json.JSONDecodeError:
            # Si no es JSON válido, no modificar el contenido
            continue

        method = request_spec.get("method", "GET").upper()
        url = request_spec.get("url", "")
        headers = request_spec.get("headers", {})
        body = request_spec.get("body", None)

        # Código JS para los headers
        headers_js = json.dumps(headers) if headers else "{}"

        # Código JS para el cuerpo (body)
        if body is not None:
            body_js = json.dumps(body)
        else:
            body_js = "null"

        # Construcción del fetch options dependiendo del método
        # Para GET y DELETE no se envía body
        fetch_options = f"""
        {{
            method: "{method}",
            headers: {headers_js},
            {'' if method in ['GET', 'DELETE'] else f'body: JSON.stringify({body_js}),'}
        }}
        """

        # Código JavaScript insertado que realiza la petición fetch y muestra el resultado
        js_code = f"""
        <div id="api-response">Cargando datos...</div>
        <script>
        fetch("{url}", {fetch_options})
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

def register():
    signals.content_object_init.connect(process_solicitud)
