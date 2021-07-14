def reward_function(params):
    distance_from_center_multiplier = 1

    # Read input parameters
    track_width = params['track_width']
    lane_width = track_width / 2.0
    distance_from_center = params['distance_from_center']

    relative_distance_from_center = (lane_width - distance_from_center) / lane_width

    reward = distance_from_center_multiplier * relative_distance_from_center

    if params['speed'] >= 3.2 and (2 < params['x'] < 8):
        reward += 1
    elif params['speed'] >= 2.5 and (1.8 < params['y'] < 3.2):
        reward += 1

    if not params['all_wheels_on_track']:
        reward = 0

    return float(reward)