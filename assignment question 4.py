from datetime import datetime

def find_peak_usage(timestamps):
    hour_counts = {}

    for timestamp in timestamps:
        clean_timestamp = timestamp.replace(" ", "")
        hour = datetime.fromisoformat(clean_timestamp).hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

    if not hour_counts:
        return -1

    peak_hour = max(hour_counts, key=lambda h: (hour_counts[h], -h))
    return peak_hour


log_list = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:00",
    "2026-08-04T09:10:05",
    "2026-08-04T09:30:00",
    "2026-08-04T22:00:00",
]

result = find_peak_usage(log_list)
print(result)