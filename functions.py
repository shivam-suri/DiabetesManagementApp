def conv_pass(password):
    hidden = ""
    for i in password:
        hidden += "*"
    return hidden


def prod_readings(bg):
    readings = []
    for i in bg:
        readings.append(i.mmol_l)
    return readings


def prod_trends(bg):
    trends = []
    for i in bg:
        if int(i.trend) == 0:
            bg_trend = "no trend"
        elif int(i.trend) == 1:
            bg_trend = "↑↑"
        elif int(i.trend) == 2:
            bg_trend = "↑"
        elif int(i.trend) == 3:
            bg_trend = "↗"
        elif int(i.trend) == 4:
            bg_trend = "→"
        elif int(i.trend) == 5:
            bg_trend = "↘"
        elif int(i.trend) == 6:
            bg_trend = "↓"
        elif int(i.trend) == 7:
            bg_trend = "↓↓"
        elif int(i.trend) == 8:
            bg_trend = "unable to determine trend"
        elif int(i.trend) == 9:
            bg_trend = "trend unavailable"
        trends.append(bg_trend)
    return trends


def avg_bg(aor):
    return round(sum(aor)/len(aor), 1)


def calc_in_range(aor):
    in_range = 0
    for i in aor:
        if 4 <= i < 10:
            in_range += 1
    return round((in_range/len(aor))*100)


def calc_high(aor):
    high = 0
    for i in aor:
        if i >= 10:
            high += 1
    return round((high/len(aor))*100)


def calc_low(aor):
    low = 0
    for i in aor:
        if i < 4:
            low += 1
    return round((low/len(aor))*100)


def calc_correction(factor, current_bg):
    bolus = (current_bg - 6) / float(factor)
    if bolus <= 0:
        bolus = 0
    return round(bolus, 1)


def calc_food_bolus(ic, carbs, factor, current_bg):
    bolus = calc_correction(float(factor), current_bg) + (float(carbs) / float(ic))
    return round(bolus, 1)
