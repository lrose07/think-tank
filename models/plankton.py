def reward_function(params):
    # Hyperparameters
    # center_line_offset = 1

    distance_from_center_multiplier = 1

    # Read input parameters
    track_width = params['track_width']
    lane_width = track_width / 2.0
    distance_from_center = params['distance_from_center']

    # relative_distance_from_center = distance_from_center / lane_width  # [0..lane_width]
    relative_distance_from_center = (lane_width - distance_from_center) / lane_width  # [0..1]

    reward = distance_from_center_multiplier * relative_distance_from_center

    if params['speed'] >= 2.5 and (params['x'] > 2 and params['x'] < 8):
        reward += 1

    if params['all_wheels_on_track'] == False:
        reward = 0
    return float(reward)