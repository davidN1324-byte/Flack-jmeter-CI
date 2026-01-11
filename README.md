# Flask + JMeter + Docker + GitHub Actions

## local test
```bash
docker compose up -d flask
docker compose run --rm jmeter
```
## all 
```bash
docker compose up --build
```
> change "Server Name or IP" to: localhost

# Results 
> ✔ /unknown → 404
> As expected → test passed.

> ✔ /process (empty) → 400
> As expected → test passed.

> ✔ /validate?limit=-1 → 400
> As expected → test passed.

> ✔ /process POST JSON → 200
> As expected → test passed.

> ✔ /fast, /slow, /unstable → 200 / 500
> As expected → test passed.

# 
> ✔ # Functional Tests Low High
> ✔ # Light Load Low Medium
> ✔ # SLA Checks Low High
> ✔ # HTML Reports Low High
> ✔ # Matrix Pipeline Medium High
> ✔ # Smoke Test Low High
> ✔ # Automated Jobs Medium High