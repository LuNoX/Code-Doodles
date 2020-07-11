

def main(shared_memory_handler):
	pulled_state = shared_memory_handler.pull_gazebo_state()
	print(pulled_state)
	crowdnav_action = generate_crowdnav_action(pulled_state)
	shared_memory_handler.push_crowdnav_action(crowdnav_action)


def generate_crowdnav_action(state):
	action = {
		'v_x': 3,
		'v_y': 4,
		'omega': 2.5
	}
	return action


if __name__ == '__main__':
	main()
