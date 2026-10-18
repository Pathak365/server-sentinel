
class HealthChecker:
    def __init__(self, cpu_threshold=80, memory_threshold=80, disk_threshold=80):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.disk_threshold = disk_threshold

    def evaluate(self, metrics):
        failed_checks = []

        if metrics["cpu_uses"] >= self.cpu_threshold:
            failed_checks.append("cpu")

        if metrics["memory_uses"] >= self.memory_threshold:
            failed_checks.append("memory")

        if metrics["disk_uses"] >= self.disk_threshold:
            failed_checks.append("disk")

        status = "Unhealthy" if failed_checks else "Healthy"

        return {
            "status": status,
            "failed_checks": failed_checks,
            "metrics": metrics
        }
