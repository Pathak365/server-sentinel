
from app.services.health_checker import HealthChecker


def test_all_metrics_healthy():
    checker = HealthChecker()

    metrics = {
        "cpu_uses": 30.0,
        "memory_uses": 50.0,
        "disk_uses": 60.0,
    }

    result = checker.evaluate(metrics)

    assert result["status"] == "Healthy"
    assert result["failed_checks"] == []


def test_high_memory_is_unhealthy():
    checker = HealthChecker()

    metrics = {
        "cpu_uses": 30.0,
        "memory_uses": 90.0,
        "disk_uses": 60.0,
    }

    result = checker.evaluate(metrics)

    assert result["status"] == "Unhealthy"
    assert result["failed_checks"] == ["memory"]


def test_multiple_failed_checks():
    checker = HealthChecker()

    metrics = {
        "cpu_uses": 90.0,
        "memory_uses": 90.0,
        "disk_uses": 95.0,
    }

    result = checker.evaluate(metrics)

    assert result["status"] == "Unhealthy"
    assert result["failed_checks"] == [
        "cpu",
        "memory",
        "disk",
    ]
