alerts = alerts = [
    {
        "title": "Short CPU and Disk Spike Detected",
        "vm_instance": "vm-app-01",
        "impact_level": "Medium",
        "category": "Performance",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU, Disk Read, and Disk Write spiked together for a short duration, "
            "indicating a batch job or heavy workload running temporarily. "
            "This is normal if infrequent, but frequent spikes may cause latency "
            "for other workloads.\n\n"
            "Remediation:\n"
            "1. Schedule heavy jobs during off-peak hours.\n"
            "2. Enable autoscaling if spikes happen regularly."
        ),
    },
    {
        "title": "High Disk I/O With Low CPU Activity",
        "vm_instance": "vm-log-02",
        "impact_level": "Low",
        "category": "Storage",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "Disk I/O is high while CPU usage remains low, suggesting the instance "
            "is performing background file writes, log rotations, or inefficient I/O operations. "
            "This can increase disk latency and storage costs.\n\n"
            "Remediation:\n"
            "1. Check for redundant or overly frequent write operations.\n"
            "2. Move archived logs to a cheaper storage class like Nearline."
        ),
    },
    {
        "title": "High CPU Load With Low Disk Activity",
        "vm_instance": "vm-compute-03",
        "impact_level": "Medium",
        "category": "Performance",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU usage is elevated while Disk I/O remains low, indicating a compute-heavy "
            "workload such as compression, encryption, or data processing. "
            "This may lead to throttling if the CPU-to-memory ratio is poor.\n\n"
            "Remediation:\n"
            "1. Move to a machine type optimized for compute-heavy tasks.\n"
            "2. Evaluate CPU/memory ratio or consider custom machine types."
        ),
    },
    {
        "title": "Idle VM Instance Detected",
        "vm_instance": "vm-idle-04",
        "impact_level": "High",
        "category": "Cost",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU, Disk I/O, and Network activity have stayed consistently low for an extended period. "
            "This strongly suggests the VM is unused or underutilized, leading to unnecessary cost. "
            "An idle instance provides no operational value.\n\n"
            "Remediation:\n"
            "1. Stop or delete the VM if not required.\n"
            "2. Downsize the machine type to reduce ongoing cost."
        ),
    },
    {
        "title": "Sustained High Load Across All Metrics",
        "vm_instance": "vm-heavy-05",
        "impact_level": "High",
        "category": "Scaling",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU, Memory, and Disk activity remain consistently high, indicating an "
            "under-provisioned instance or a runaway process. Sustained pressure across resources "
            "can lead to failures or major slowdowns.\n\n"
            "Remediation:\n"
            "1. Upgrade to a larger instance or enable autoscaling.\n"
            "2. Investigate application behavior to rule out memory leaks."
        ),
    },
    {
        "title": "Rapid CPU Fluctuations With Constant Disk I/O",
        "vm_instance": "vm-app-06",
        "impact_level": "Medium",
        "category": "Reliability",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU usage fluctuates rapidly while Disk I/O remains constant, indicating unstable "
            "workload behavior or possible application misconfiguration. This instability can "
            "impact performance unpredictably.\n\n"
            "Remediation:\n"
            "1. Review autoscaling configuration for overly aggressive thresholds.\n"
            "2. Optimize application code to smooth CPU spikes."
        ),
    },
    {
        "title": "High Disk Write Activity With Low CPU",
        "vm_instance": "vm-backup-07",
        "impact_level": "Low",
        "category": "Storage",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "Disk Write Bytes are elevated while CPU usage remains low, indicating a backup, "
            "log rotation, or archival process running. This behavior is typically normal but "
            "may cause higher storage throughput cost.\n\n"
            "Remediation:\n"
            "1. Eliminate redundant backups or reduce backup frequency.\n"
            "2. Move backup targets to Nearline/Coldline storage."
        ),
    },
    {
        "title": "Oversized VM With Low Actual CPU Utilization",
        "vm_instance": "vm-large-08",
        "impact_level": "Medium",
        "category": "Cost",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU usage is high but CPU utilization (active cores used) is low—indicating the VM "
            "has too many vCPUs compared to the workload it is running. This means the machine "
            "is overprovisioned and wasting compute capacity.\n\n"
            "Remediation:\n"
            "1. Resize to a smaller VM type to reduce unused cores.\n"
            "2. Consider committed-use discounts for predictable workloads."
        ),
    },
    {
        "title": "Spike in Disk Reads With Steady CPU",
        "vm_instance": "vm-db-09",
        "impact_level": "Low",
        "category": "Performance",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "A sudden surge in Disk Read Bytes occurred while CPU remained steady, indicating "
            "a large dataset load or database read operation. This may be expected, but repeated "
            "spikes can cause IO latency.\n\n"
            "Remediation:\n"
            "1. Investigate query patterns and caching strategy.\n"
            "2. Add read replicas if load patterns increase."
        ),
    },
    {
        "title": "High Network Throughput With Low Disk Usage",
        "vm_instance": "vm-api-10",
        "impact_level": "High",
        "category": "Network",
        # "cost_saved": "$0",
        "detailed_explanation": (
            "CPU utilization is moderately high while Disk Read and Write remain low, but "
            "Network egress is elevated. This indicates a heavy network-bound workload such "
            "as an API server or data streaming service.\n\n"
            "Remediation:\n"
            "1. Optimize network egress using caching or compression.\n"
            "2. Consider using a regional load balancer to distribute traffic."
        ),
    },
]