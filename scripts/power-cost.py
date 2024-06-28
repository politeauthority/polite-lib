"""
    Power Usage
    Usage:
        power-cost.py <kwh>

    Variable Pricing
        OFF PEAK 7pm - 1pm
        MID PEAK 1pm - 3PM
        ON PEAK 3pm - 7pm

"""
import sys


class PowerCost:

    def __init__(self):
        self.var_mid_hours_per_day = 2
        self.var_high_hours_per_day = 4
        self.var_low_hours_per_day = 18
        self.var_kwh_price_high = .3171
        self.var_kwh_price_mid = .2181
        self.var_kwh_price_low = .1190

        self.static_kwh_price_summer = .16

    def run(self, kwh_device: float) -> bool:
        """Primary entrypoint"""
        kwh_device = float(kwh_device)
        self.compare_flat_to_variable(kwh_device)
        return True

    def compare_flat_to_variable(self, kwh_device) -> bool:
        """Run both variable pricing and static pricing evaluations."""
        print("Device KWH: %s\n" % kwh_device)
        self.monthly_cost_variable(kwh_device)
        self.monthly_cost_static(kwh_device)
        return True

    def monthly_cost_variable(self, kwh_device: float) -> bool:
        """Calculate the cost of a device hourly avg, daily and monthly. Assuming the device runs at at static 
        KWH usage throughout the period. """
        price_var_low_per_hour = self.price_kwh(kwh_device, self.var_kwh_price_low)
        price_var_low_per_day = round((price_var_low_per_hour * self.var_low_hours_per_day), 12)

        price_var_mid_per_hour = self.price_kwh(kwh_device, self.var_kwh_price_mid)
        price_var_mid_per_day = round((price_var_mid_per_hour * self.var_kwh_price_mid), 12)

        price_var_high_per_hour = self.price_kwh(kwh_device, self.var_kwh_price_high)
        price_var_high_per_day = round((price_var_high_per_hour * self.var_kwh_price_high), 12)

        total_price_per_day = (
            price_var_low_per_day + price_var_mid_per_day + price_var_high_per_day)
        total_price_per_day = round(total_price_per_day, 4)

        x_mid = (price_var_low_per_hour + price_var_mid_per_hour + price_var_high_per_hour) / 3

        total_price_per_hour_avg = round(x_mid, 4)

        total_price_per_month = total_price_per_day * 31

        print("Variable")
        print("\tPer Hour Avg\t%s" % total_price_per_hour_avg)
        print("\tPer Day\t\t%s" % total_price_per_day)
        print("\tPer Month\t%s" % total_price_per_month)
        return True

    def monthly_cost_static(self, kwh_device: float) -> bool:
        price_flat_per_hour = self.price_kwh(kwh_device, self.static_kwh_price_summer)
        price_flat_per_day = price_flat_per_hour * 24
        price_flat_per_month = price_flat_per_day * 31

        print("Static Pricing")

        print("\tPer Hour\t%s " % price_flat_per_hour)
        print("\tPer Day\t\t%s " % price_flat_per_day)
        print("\tPer Month\t%s " % price_flat_per_month)
        return True

    def price_kwh(self, kwh_usage: float, price_per_kwh: float, round_int: int = 4) -> float:
        return round((kwh_usage * price_per_kwh), round_int)

if __name__ == "__main__":
    PowerCost().run(sys.argv[1])


# End File: politeauthority/polite-lib/scripts/power-cost.py
