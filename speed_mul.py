""" 
    This files relates average speed to carbon emission multiplier
    Based on https://escholarship.org/uc/item/07n946vd
"""

import math

km_to_mile: float = 1.609344

B = [ 7.613534994965560,
    -0.138565467462594,
    0.003915102063854,
    -0.000049451361017,
    0.000000238630156,]

C = [B[i]/(km_to_mile**i) for i in range(5)]
C[0] = B[0] - math.log(km_to_mile)

def curve_mph_to_co2_mile(mph: float):
    return math.exp(B[0] + B[1] * mph + B[2] * mph**2 + B[3] * mph**3 + B[4] * mph**4)


def curve_kmh_to_co2_km(kmh: float):
    return math.exp(C[0] + C[1] * kmh + C[2] * kmh**2 + C[3] * kmh**3 + C[4] * kmh**4)

def get_multiplier(km: float) -> float:
    return curve_kmh_to_co2_km(km)/curve_kmh_to_co2_km(46.532)