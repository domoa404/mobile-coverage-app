from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_coverage(env, distance_cat, walls_cat, mobility, network):
    
    env_factor = {
        "home_indoor": -10,
        "street_outdoor": 0,
        "mall": -18,
        "campus": -5,
        "rural": -8,
        "basement": -30,
    }

    distance_factor = {
        "very_close": 0,     # < 200m
        "near": -8,          # 200–500m
        "medium": -20,       # 500–1000m
        "far": -35,          # > 1000m
    }

    walls_factor = {
        "none": 0,
        "few": -8,
        "many": -18,
        "thick": -25,
    }

    mobility_factor = {
        "stationary": 5,
        "walking": 0,
        "car": -10,
    }

    network_latency_adj = {
        "3g": 30,
        "4g": 10,
        "5g": -5,
        "wifi": -10,
    }

    
    base_signal = 90
    base_signal += env_factor.get(env, 0)
    base_signal += distance_factor.get(distance_cat, 0)
    base_signal += walls_factor.get(walls_cat, 0)
    base_signal += mobility_factor.get(mobility, 0)

    
    signal = max(0, min(100, base_signal))

    
    latency_ms = 150 - signal  
    latency_ms += network_latency_adj.get(network, 0)
    latency_ms = max(10, min(250, latency_ms))

    
    if signal >= 70:
        drop_prob = "Low"
    elif signal >= 45:
        drop_prob = "Moderate"
    elif signal >= 25:
        drop_prob = "High"
    else:
        drop_prob = "Very High"

    
    if signal >= 80:
        quality = "Excellent"
        quality_desc = "You should experience very stable coverage and smooth data usage."
        quality_level = "excellent"
    elif signal >= 60:
        quality = "Good"
        quality_desc = "Overall good coverage with mostly stable calls and browsing."
        quality_level = "good"
    elif signal >= 40:
        quality = "Limited"
        quality_desc = "Coverage is usable but you may notice drops and slower data."
        quality_level = "limited"
    else:
        quality = "Poor"
        quality_desc = "Weak coverage. Calls and mobile data may frequently drop."
        quality_level = "poor"

    
    if latency_ms <= 40:
        latency_label = "Low"
        latency_desc = "Good for browsing, social apps, and most video streaming."
    elif latency_ms <= 80:
        latency_label = "Medium"
        latency_desc = "Acceptable for normal use, but you may feel delay in gaming or calls."
    else:
        latency_label = "High"
        latency_desc = "You will notice lag in calls, games, and video streaming."

    
    if mobility == "stationary":
        mobility_label = "Stable"
        mobility_desc = "Low mobility helps keep your connection stable."
    elif mobility == "walking":
        mobility_label = "Moderately Stable"
        mobility_desc = "Normal walking may cause small variations in signal."
    else:
        mobility_label = "Unstable"
        mobility_desc = "High speed (car) can cause frequent cell changes and signal variations."

    
    advice_list = []
    if walls_cat in ("many", "thick"):
        advice_list.append("Try to stay closer to windows or open areas indoors.")
    if distance_cat in ("medium", "far"):
        advice_list.append("Moving slightly closer to the tower area may improve signal.")
    if network in ("3g",) and signal < 60:
        advice_list.append("If possible, switch to 4G/5G for better performance.")
    if not advice_list:
        advice_list.append("Current conditions look fine. No major action required.")

    result = {
        "signal": int(signal),
        "quality": quality,
        "quality_desc": quality_desc,
        "quality_level": quality_level,
        "latency_ms": int(latency_ms),
        "latency_label": latency_label,
        "latency_desc": latency_desc,
        "drop_prob": drop_prob,
        "mobility_label": mobility_label,
        "mobility_desc": mobility_desc,
        "advice_list": advice_list,
    }

    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    
    form_values = {
        "env": "home_indoor",
        "distance_cat": "near",
        "walls_cat": "few",
        "mobility": "walking",
        "network": "4g",
    }

    if request.method == "POST":
        form_values["env"] = request.form.get("env", "home_indoor")
        form_values["distance_cat"] = request.form.get("distance_cat", "near")
        form_values["walls_cat"] = request.form.get("walls_cat", "few")
        form_values["mobility"] = request.form.get("mobility", "walking")
        form_values["network"] = request.form.get("network", "4g")

        result = analyze_coverage(
            form_values["env"],
            form_values["distance_cat"],
            form_values["walls_cat"],
            form_values["mobility"],
            form_values["network"],
        )
    

    return render_template("index.html", result=result, form_values=form_values)


if __name__ == "__main__":
    app.run(debug=True)
