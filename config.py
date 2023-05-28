import yaml


bdb = {
    "version": "3",
    "services": {"bmu": {
        "image": {"postgres": "9.6.2-alpine"},
        "ports": ["8000:8000"],
        "environment": {"POSTGRES_USER": "bwroline", "POSTGRES_DB": "bmu"}
    }},

    "bwroline": {"build": {"context": "./bwroline"},
                 "Dockerfile": "Dockerfile",
                 "command": "uvicorn --reload -b 0.0.0.0:8080 bwroline.wsgi:application"
                 },
    "depends_on": ["bmu"],
    "ports": ["8080:8080"],
    "volumes": [".bwroline:/bwroline/bmu", ".bwroline.com:/bwroline/bwroline.com"],
    "environment": ["DATABASE_URL=postgres://bwroline@postgres/bwroline.com"]
}
with open(r'C:\Users\HP\Bwroline\docker-compos.yml', 'w') as file:
    bw = yaml.dump(bdb, file)
    # bl = yaml.load(file, Loader=yaml.FullLoader)
