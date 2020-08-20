class Amountclass:
    menu_items = [{'text': '5 Ampere', "height": "15dp", "top_pad": "5dp", "bot_pad": "5dp"},
                  {'text': '15 Ampere', "height": "15dp", "top_pad": "5dp", "bot_pad": "5dp"},
                  {'text': '30 Ampere', "height": "15dp", "top_pad": "5dp", "bot_pad": "5dp"},
                  {'text': '60 Ampere', "height": "15dp", "top_pad": "5dp", "bot_pad": "5dp"}]

    def __init__(self, load, unit):
        self.load = load
        self.unit = unit

    def Calculation(load, unit_tot):
        stramount = "0"

        if load == "5 Ampere":
            if unit_tot <= 10:
                stramount = str(unit_tot * 0 + 30.00)
            if 10 < unit_tot <= 20:
                stramount = str((unit_tot - 10) * 3.00 + 30 + 30.00)
            if 20 < unit_tot <= 30:
                stramount = str((unit_tot - 20) * 6.50 + 60 + 50.00)
            if 30 < unit_tot <= 50:
                stramount = str((unit_tot - 30) * 8 + 125 + 50.00)
            if 50 < unit_tot <= 100:
                stramount = str((unit_tot - 50) * 9.50 + 285 + 75.00)
            if 100 < unit_tot <= 150:
                stramount = str((unit_tot - 100) * 9.50 + 760 + 100.00)
            if 150 < unit_tot <= 250:
                stramount = str((unit_tot - 150) * 10.0 + 1235.0 + 125.00)
            if 250 < unit_tot <= 400:
                stramount = str((unit_tot - 250) * 11 + 2235 + 150.00)
            if 400 < unit_tot:
                stramount = str((unit_tot - 400) * 12 + 3885 + 175.00)

        if load == "15 Ampere":
            if unit_tot <= 10:
                stramount = str(unit_tot * 4 + 50.00)
            if 10 < unit_tot <= 20:
                stramount = str((unit_tot - 10) * 4.00 + 40 + 50.00)
            if 20 < unit_tot <= 30:
                stramount = str((unit_tot - 20) * 6.50 + 80 + 75.00)
            if 30 < unit_tot <= 50:
                stramount = str((unit_tot - 30) * 8 + 145 + 75.00)
            if 50 < unit_tot <= 100:
                stramount = str((unit_tot - 50) * 9.50 + 305 + 100.00)
            if 100 < unit_tot <= 150:
                stramount = str((unit_tot - 100) * 9.50 + 780 + 125.00)
            if 150 < unit_tot <= 250:
                stramount = str((unit_tot - 150) * 10.0 + 1255.0 + 150.00)
            if 250 < unit_tot <= 400:
                stramount = str((unit_tot - 250) * 11 + 2255 + 175.00)
            if 400 < unit_tot:
                stramount = str((unit_tot - 400) * 12 + 3905 + 200.00)

        if load == "30 Ampere":
            if unit_tot <= 10:
                stramount = str(unit_tot * 5 + 75.00)
            if 10 < unit_tot <= 20:
                stramount = str((unit_tot - 10) * 5.00 + 50 + 75.00)
            if 20 < unit_tot <= 30:
                stramount = str((unit_tot - 20) * 6.50 + 100 + 100.00)
            if 30 < unit_tot <= 50:
                stramount = str((unit_tot - 30) * 8 + 165 + 100.00)
            if 50 < unit_tot <= 100:
                stramount = str((unit_tot - 50) * 9.50 + 325 + 125.00)
            if 100 < unit_tot <= 150:
                stramount = str((unit_tot - 100) * 9.50 + 800 + 150.00)
            if 150 < unit_tot <= 250:
                stramount = str((unit_tot - 150) * 10.0 + 1275.0 + 175.00)
            if 250 < unit_tot <= 400:
                stramount = str((unit_tot - 250) * 11 + 2275 + 200.00)
            if 400 < unit_tot:
                stramount = str((unit_tot - 400) * 12 + 3925 + 225.00)

        if load == "60 Ampere":
            if unit_tot <= 10:
                stramount = str(unit_tot * 6 + 125.00)
            if 10 < unit_tot <= 20:
                stramount = str((unit_tot - 10) * 6.00 + 60 + 125.00)
            if 20 < unit_tot <= 30:
                stramount = str((unit_tot - 20) * 6.50 + 120 + 125.00)
            if 30 < unit_tot <= 50:
                stramount = str((unit_tot - 30) * 8 + 185 + 125.00)
            if 50 < unit_tot <= 100:
                stramount = str((unit_tot - 50) * 9.5 + 345 + 150.00)
            if 100 < unit_tot <= 150:
                stramount = str((unit_tot - 100) * 9.5 + 820 + 200.00)
            if 150 < unit_tot <= 250:
                stramount = str((unit_tot - 150) * 10 + 1295 + 200.00)
            if 250 < unit_tot <= 400:
                stramount = str((unit_tot - 250) * 11 + 2295 + 250.00)
            if 400 < unit_tot:
                stramount = str((unit_tot - 400) * 12 + 3945 + 275.00)

        return stramount