def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    current_speed = params['speed']
    current_x_pos = params['x']
    all_wheels_on_track = params['all_wheels_on_track']

    # Constants
    TARGET_TIME = 15  # anything longer than this value results in a negative reward
    STEPS_PER_SECOND = 15  # per AWS docs

    # Calculated
    lane_width = track_width / 2.0
    max_steps = TARGET_TIME * STEPS_PER_SECOND

    # Reward for staying near the center
    relative_distance_from_center = (lane_width - distance_from_center) / lane_width
    reward = relative_distance_from_center

    # Reward for finishing quickly
    current_progress_points = (max_steps - steps) * 0.3
    reward += current_progress_points

    # Reward for faster speed
    if current_speed >= 3 and (2 < current_x_pos < 7.5):
        reward += 1

    # Reset reward to 0 if car goes off track
    if not all_wheels_on_track:
        reward = 0

    return float(reward)
