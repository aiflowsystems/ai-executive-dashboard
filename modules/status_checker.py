def determine_business_status(kpi_summary):
    met_targets = kpi_summary["met_targets"]
    total_metrics = kpi_summary["total_metrics"]

    success_rate = round(
        (met_targets / total_metrics) * 100,
        1
    )

    if success_rate >= 80:
        status = "Excellent"

    elif success_rate >= 50:
        status = "Good"

    else:
        status = "Needs Attention"

    return {
        "success_rate": success_rate,
        "business_status": status
    }