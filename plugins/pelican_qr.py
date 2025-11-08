import qrcode
import base64
from io import BytesIO
from pelican import signals

def generate_qr_code_base64(data):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_base64

def replace_tex_with_qr(instance):
    if not instance._content:
        return
    content = instance._content
        
    import re
    pattern = r'\[-\[(.*?)\]-\]'
    def repl(match):
        qr_data = match.group(1)
        print(str(qr_data))
        img_b64 = generate_qr_code_base64(qr_data)
        img_tag = f'<img src="data:image/png;base64,{img_b64}" alt="QR code" />'
        return img_tag
    new_content = re.sub(pattern, repl, content)
    instance._content = new_content

def register():
    signals.content_object_init.connect(replace_tex_with_qr)
