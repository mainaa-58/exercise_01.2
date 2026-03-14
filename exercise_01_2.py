import math

# Assign data to variables
principal = 172000
boe_rate = 2.25 / 100
rate_over_boe = 1.49 / 100

# Compute interest payable each month
total_annual_rate = boe_rate + rate_over_boe
annual_interest = principal * total_annual_rate
interest = annual_interest / 12

## test ##
assert math.isclose(interest, 536.0666666666667)
print("Test passed!")
