def normalize(container, carrier, scraped, vessel_fallback):

    return {
        "container": container,
        "carrier": carrier if carrier else "UNKNOWN",
        "vessel": scraped.get("vessel") or vessel_fallback,
        "eta": scraped.get("eta") or "UNKNOWN",
        "etd": scraped.get("etd") or "UNKNOWN",
        "pol": scraped.get("pol") or "UNKNOWN",
        "pod": scraped.get("pod") or "UNKNOWN"
    }
