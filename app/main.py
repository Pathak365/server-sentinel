
from fastapi import FastAPI, HTTPException

from app.services.system_collector import SystemCollector
from app.services.health_checker import HealthChecker
from app.services.history_manager import HistoryManager
from app.utils.cache import TTLCache

app = FastAPI(
    title="Server Sentinel",
    description="A local-first server monitoring application.",
    version="0.1.0",
)

system_collector = SystemCollector()
health_checker = HealthChecker()
history_manager = HistoryManager()
metrics_cache = TTLCache(ttl_seconds=5)


def get_cached_metrics():
    metrics = metrics_cache.get("system_metrics")

    if metrics is None:
        metrics = system_collector.collector()
        metrics_cache.set("system_metrics", metrics)

    return metrics


@app.get("/")
def root():
    return {
        "application": "Server Sentinel",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/api/v1/system")
def get_system_metrics():
    return get_cached_metrics()


@app.get("/api/v1/health")
@app.get("/health")
def get_health():
    metrics = get_cached_metrics()
    health = health_checker.evaluate(metrics)

    record = history_manager.add({
        **metrics,
        "health_status": health["status"],
        "failed_checks": health["failed_checks"],
    })

    history_manager.save()
    return record


@app.get("/api/v1/history")
def get_history():
    return history_manager.get_all()


@app.get("/api/v1/history/{record_id}")
def get_history_record(record_id: str):
    record = history_manager.get_by_id(record_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="History record not found",
        )

    return record
