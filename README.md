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