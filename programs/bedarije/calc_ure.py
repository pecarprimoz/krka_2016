def get_seconds(hours, minutes, seconds):
    sumSekunde = 0
    while hours != 0:
        sumSekunde += 3600
        hours -= 1
    while minutes != 0:
        sumSekunde += 60
        minutes -= 1
    return sumSekunde + seconds


def to_normal(diff):
    ure = 0
    minute = 0
    sekunde = 0
    while diff > 0:
        if minute > 60:
            minute -= 60
            ure += 1
        if sekunde >= 60:
            sekunde -= 60
            minute += 1
        if diff % 3600 == 0:
            ure += 1
            diff -= 3600
        if diff % 60 == 0:
            minute += 1
            diff -= 60
        else:
            diff -= 1
            sekunde += 1
    return "{:02}:{:02}:{:02}".format(ure, minute, sekunde)


def get_time(time_value):
    # break time into 3 parts, take part on ind 1 int(s)
    h, m, s = time_value.split(":")
    # change to integers and return
    return int(h), int(m), int(s)


def core():
    zac = [
        "7:50:00",
        "5:34:00",
        "5:35:00",
        "5:38:00",
        "5:38:00",
        "5:56:00",
        "5:55:00",
        "5:55:00",
        "5:57:00",
        "5:55:00",
        "5:57:00",
    ]
    kon = [
        "14:00:00",
        "14:03:00",
        "14:05:00",
        "14:03:00",
        "14:03:00",
        "14:03:00",
        "13:58:00",
        "14:01:00",
        "14:00:00",
        "13:49:00",
        "14:00:00"
    ]
    start, end = zac, kon
    skupno = 0
    for i in zip(start, end):
        zac = i[0]
        kon = i[1]
        h1, m1, s1 = get_time(zac)
        h2, m2, s2 = get_time(kon)
        r1 = get_seconds(h1, m1, s1)
        r2 = get_seconds(h2, m2, s2)
        razlika = r2 - r1
        skupno += razlika
    return to_normal(skupno)


ure = core().split(":")[0]  # 20 Kappa
print("Zasluženo: {}€\nŠt.ur: {}".format((float(ure) * 3.80) - 20,ure))
