import csv
import json
from pathlib import Path
from modules.kpi_analyzer import analyze_kpis
from modules.status_checker import determine_business_status
from modules.report_generator import generate_dashboard_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]

Path(output_folder).mkdir(exist_ok=True)

metrics = []

with open("business_metrics.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        metrics.append(row)

kpi_summary = analyze_kpis(metrics)
dashboard_status = determine_business_status(kpi_summary)
dashboard_report = generate_dashboard_report(kpi_summary, dashboard_status)

print("AI Executive Dashboard")
print("======================")
print()

print(f"Business metrics loaded: {len(metrics)}")

for metric in metrics:
    print(
        f"{metric['metric']} - "
        f"Value: {metric['value']} - "
        f"Target: {metric['target']}"
    )

print()
print("KPI SUMMARY")
print("-----------")
print(f"Total Metrics: {kpi_summary['total_metrics']}")
print(f"Met Targets: {kpi_summary['met_targets']}")
print(f"Missed Targets: {kpi_summary['missed_targets']}")

print()
print("BUSINESS STATUS")
print("---------------")
print(f"Success Rate: {dashboard_status['success_rate']}%")
print(f"Status: {dashboard_status['business_status']}")

report_file = Path(output_folder) / config["dashboard_report_file"]

with open(report_file, "w", encoding="utf-8") as file:
    file.write(dashboard_report)

print()
print(f"Dashboard report generated: {report_file}")
