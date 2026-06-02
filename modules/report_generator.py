def generate_dashboard_report(kpi_summary, dashboard_status):
    report = f"""AI Executive Dashboard Report

KPI Summary
===========

Total Metrics: {kpi_summary['total_metrics']}
Met Targets: {kpi_summary['met_targets']}
Missed Targets: {kpi_summary['missed_targets']}

Business Status
===============

Success Rate: {dashboard_status['success_rate']}%
Status: {dashboard_status['business_status']}
"""

    return report