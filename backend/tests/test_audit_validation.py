import io
from PIL import Image
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def image_bytes():
    stream=io.BytesIO(); Image.new("RGB",(40,40),"white").save(stream,"JPEG"); return stream.getvalue()
def test_rejects_unsupported_file():
    r=client.post("/api/audit",files={"image":("x.txt",b"no","text/plain")},data={"place_type":"campus","perspective":"general"})
    assert r.status_code==415
def test_missing_ai_configuration_is_safe():
    r=client.post("/api/audit",files={"image":("x.jpg",image_bytes(),"image/jpeg")},data={"place_type":"campus","perspective":"general"})
    assert r.status_code in (502,503)
