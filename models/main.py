def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    lane_width = track_width / 2.0
    distance_from_center = params['distance_from_center']

    # Initial vars
    track_position_multiplier = 0.5
    wheels_on_track_multiplier = 0.3
    speed_multiplier = 0.2
    # track_position_reward = 0
    wheels_on_track_reward = 0
    speed_reward = 0

    # Reward based on horizontal track position
    relative_distance_from_center = (lane_width - distance_from_center) / lane_width  # [0..1]

    track_position_reward = track_position_multiplier * relative_distance_from_center

    # Reward for on or off track
    if not params['all_wheels_on_track']:
        wheels_on_track_reward += -5

    wheels_on_track_reward *= wheels_on_track_multiplier

    # Reward for speed
    if params['speed'] < 1.5:
        speed_reward += .5
    if params['speed'] > 3:
        speed_reward += 2

    speed_reward *= speed_multiplier

    # Total reward calculation
    reward = track_position_reward + wheels_on_track_reward + speed_reward

    return float(reward)


def main():
    params = {'track_width': 10, 'distance_from_center': 2}
    print(reward_function(params))

if __name__ == '__main__':
    main()