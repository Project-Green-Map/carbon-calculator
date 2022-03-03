""" Supposed to communicate with the server """

from data_extractor import get_car_value, get_cycling_value, get_public_transport_value


def car_calculation(distance, vehicle_type, fuel_type):
    return distance * get_car_value(vehicle_type, fuel_type)

def public_transport_calculation(distance, transport_type):
    return distance * get_public_transport_value(transport_type)

def cycling_calculation(distance):
    return distance * get_cycling_value()

