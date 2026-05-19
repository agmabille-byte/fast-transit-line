def get_container_data(container, carrier):

    # ⚠️ MOCK SaaS (remplacé par Project44 / GoComet plus tard)

    return {
        "container": container,
        "carrier": carrier or "AUTO-DETECTED",
        "vessel": "MSC ANNA",
        "pol": "Shanghai",
        "pod": "Le Havre",
        "eta": "2026-06-01"
    }
