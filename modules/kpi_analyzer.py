def analyze_kpis(metrics):
    total_metrics = len(metrics)
    met_targets = 0
    missed_targets = 0

    for metric in metrics:
        value = float(metric["value"])
        target = float(metric["target"])

        if value >= target:
            met_targets += 1
        else:
            missed_targets += 1

    return {
        "total_metrics": total_metrics,
        "met_targets": met_targets,
        "missed_targets": missed_targets
    }