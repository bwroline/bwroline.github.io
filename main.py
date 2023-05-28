from fastapi import FastAPI
import uvicorn

BWAYA_metadata = [
    {
        "name": "BMU",
        "description": "Website Application **CREATED** to help self interest"
    },
    {
        "name": "bwroline",
        "description": "A Website Application **CREATED** to help self interest",
        "externalDocs": {
            "description": "Website Application to help self interest",
            "url": "https://j26067.deta.dev/",
        },
    },
]

description = """A website application **created** to help self interest"""

app = FastAPI(title="server.com", description=description, version="0.0.1", terms_of_service="use", contact={
    "name": "btghoa",
    "url": "http://bwroline.com/about/btghoa/",
    "email": "bwroline@gmail.com",
}, license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
}, openapi_tags=BWAYA_metadata)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, debug=True)  # reload=True
