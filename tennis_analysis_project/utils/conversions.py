import math
def measure_distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
def convert_pixel_distance_to_meters(pixel_distance,reference_height_in_meters,
                                     reference_height_in_pixels):
    return(pixel_distance * reference_height_in_meters) / reference_height_in_pixels
def convert_meters_to_pixel_distance(meters,reference_height_in_meters, reference_height_in_pixels):
    return meters*reference_height_in_pixels/reference_height_in_meters
def calculate_speed_mps(distance_meters,time_seconds):
    return distance_meters/time_seconds
def convert_mps_toKmh(speed_mps):
    return speed_mps*3.6

