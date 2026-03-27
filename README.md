# DevOps Intern Final Assessment

![CI Pipeline](https://github.com/YOUR_USERNAME/devops-intern-final/actions/workflows/ci.yml/badge.svg)

**Name:** Sumeet Yadav  
**Date:** 27-03-2026
**Description:** A complete DevOps pipeline demonstrating Git, Linux scripting, Docker, CI/CD with GitHub Actions, Nomad job deployment, and log monitoring with Grafana Loki.

---

## 📁 Repository Structure

```
devops-intern-final/
├── hello.py                        # Sample Python script
├── Dockerfile                      # Docker container definition
├── README.md                       # This file
├── scripts/
│   └── sysinfo.sh                  # Linux system info script
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI pipeline
├── nomad/
│   └── hello.nomad                 # Nomad job definition
├── monitoring/
│   └── loki_setup.txt              # Grafana Loki setup notes
└── mlflow/
    └── track_experiment.py         # MLflow extra credit
```

---

## Step 1 — Git & GitHub Setup

This repository was initialized with:
- A public GitHub repo named `devops-intern-final`
- This `README.md` with name, date, and project description
- A sample `hello.py` script

### `hello.py`
```python
print("Hello, DevOps!")
```

**Run it:**
```bash
python hello.py
# Output: Hello, DevOps!
```

---

## Step 2 — Linux & Scripting Basics

Located in `scripts/sysinfo.sh`, this script prints system info including the current user, date, and disk usage.

### Make it executable and run:
```bash
chmod +x scripts/sysinfo.sh
./scripts/sysinfo.sh
```

### Expected output:
```
===============================
       System Information
===============================

👤 Current User:
youruser

📅 Current Date & Time:
Mon Jun  1 10:30:00 UTC 2025

💾 Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   12G   36G  25% /
...
```

---

## Step 3 — Docker Basics

The `Dockerfile` containerizes `hello.py` using a lightweight Python 3.11 image.

### Build the image:
```bash
docker build -t hello-devops .
```

### Run the container:
```bash
docker run --rm hello-devops
# Output: Hello, DevOps!
```

### Dockerfile overview:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
```

---

## Step 4 — CI/CD with GitHub Actions

The workflow file at `.github/workflows/ci.yml` automatically runs on every push:

1. Checks out the code
2. Sets up Python 3.11
3. Runs `python hello.py`
4. Builds the Docker image
5. Runs the Docker container

### Trigger it:
Every `git push` to any branch triggers the pipeline automatically.

```bash
git add .
git commit -m "trigger ci"
git push
```

Check the **Actions** tab on your GitHub repo to see the pipeline run.

---

## Step 5 — Job Deployment with Nomad

The Nomad job file at `nomad/hello.nomad` defines a `service` type job that runs the Docker container with minimal resource allocation.

### Prerequisites:
- [Install Nomad](https://developer.hashicorp.com/nomad/install)
- Docker must be running

### Start a local Nomad dev agent:
```bash
nomad agent -dev
```

### Deploy the job (in a new terminal):
```bash
nomad job run nomad/hello.nomad
```

### Check job status:
```bash
nomad job status hello-devops
```

### View logs:
```bash
nomad alloc logs <alloc-id>
```

### Stop the job:
```bash
nomad job stop hello-devops
```

---

## Step 6 — Monitoring with Grafana Loki

Full setup instructions are in `monitoring/loki_setup.txt`.

### Quick start — run Loki locally:
```bash
docker run -d \
  --name loki \
  -p 3100:3100 \
  grafana/loki:2.9.0 \
  -config.file=/etc/loki/local-config.yaml
```

### Verify Loki is ready:
```bash
curl http://localhost:3100/ready
# Should return: ready
```

### Query logs via API:
```bash
curl -G -s "http://localhost:3100/loki/api/v1/query_range" \
  --data-urlencode 'query={job="docker-logs"}' \
  | python3 -m json.tool
```

### View in Grafana (optional):
```bash
docker run -d --name grafana -p 3000:3000 grafana/grafana:latest
# Open http://localhost:3000 → admin/admin → Add Loki data source
```

See `monitoring/loki_setup.txt` for full Promtail (log forwarder) setup.

---

## Step 7 — Extra Credit: MLflow Tracking

Located in `mlflow/track_experiment.py`, this script logs a dummy ML experiment with parameters and metrics.

### Install MLflow:
```bash
pip install mlflow
```

### Run the experiment:
```bash
python mlflow/track_experiment.py
```

### View the MLflow UI:
```bash
mlflow ui
# Open http://localhost:5000 in your browser
```

You'll see the experiment with logged loss/accuracy metrics per epoch.

---

## ✅ Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| Git & GitHub | Version control and repository hosting |
| Bash / Shell | Linux scripting (`sysinfo.sh`) |
| Python | Sample application (`hello.py`) |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| Nomad | Container orchestration / job deployment |
| Grafana Loki | Log aggregation and monitoring |
| MLflow | ML experiment tracking (extra credit) |

---

## 🚀 Quick Start (Run Everything Locally)

```bash
# 1. Clone the repo
git clone https://github.com/Sumeet-Y1/devops-intern-final.git
cd devops-intern-final

# 2. Run the Python script
python hello.py

# 3. Run the sysinfo script
chmod +x scripts/sysinfo.sh && ./scripts/sysinfo.sh

# 4. Build and run Docker
docker build -t hello-devops .
docker run --rm hello-devops

# 5. Start Loki
docker run -d --name loki -p 3100:3100 grafana/loki:2.9.0 -config.file=/etc/loki/local-config.yaml

# 6. Deploy with Nomad (requires nomad installed)
nomad agent -dev &
nomad job run nomad/hello.nomad
```