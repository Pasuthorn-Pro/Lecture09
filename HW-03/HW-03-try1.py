def analyze_log_file(log_file_path: str) -> dict:
    requests_by_ip = {}
    resource_count = {}
    total_404_errors = 0
    total_bytes = 0

    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) != 5:
                # ข้ามบรรทัดที่รูปแบบไม่ตรง
                continue

            ip, method, resource, status, size = parts
            status = int(status)
            size = int(size)

            # นับจำนวนการร้องขอจากแต่ละ IP Address
            if ip in requests_by_ip:
                requests_by_ip[ip] += 1
            else:
                requests_by_ip[ip] = 1

            # นับจำนวนการร้องขอแต่ละ resource
            if resource in resource_count:
                resource_count[resource] += 1
            else:
                resource_count[resource] = 1

            # นับจำนวน 404 errors
            if status == 404:
                total_404_errors += 1

            # คำนวณขนาดรวมของการร้องขอ
            total_bytes += size

    # หาทรัพยากรที่ถูกเรียกร้องมากที่สุด
    if resource_count:
        most_requested_resource = max(resource_count, key=resource_count.get)
    else:
        most_requested_resource = None

    # คืนผลลัพธ์เป็น dictionary
    return {
        "requests_by_ip": requests_by_ip,
        "most_requested_resource": most_requested_resource,
        "total_404_errors": total_404_errors,
        "total_bytes": total_bytes
    }

log_file_path = 'server_log.txt'  # Replace with the path to your log file
result = analyze_log_file(log_file_path)

print("Log File Analysis Result:")
print(f"Requests by IP: {result['requests_by_ip']}")
print(f"Most Requested Resource: {result['most_requested_resource']}")
print(f"Total 404 Errors: {result['total_404_errors']}")
print(f"Total Bytes Transferred: {result['total_bytes']}")