def analyze_threats(data):
    """Analyze threats in the dataset."""
    high_risk = data[data["threat_level"] == "High"]
    return high_risk
