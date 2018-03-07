def future_value(present_value, annual_rate, periods_per_year, years):
	rate_per_period = annual_rate / periods_per_year
	periods = periods_per_year* years
	FV = present_value*((1+rate_per_period)**periods)
	return FV


def area_equilateral_triangle(side_length):
	result = (side_length**2)*((3**.5)/4)
	return result

print(area_equilateral_triangle(5))
	