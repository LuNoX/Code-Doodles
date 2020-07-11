

def main(shared_memory_handler):
	pulled_action = shared_memory_handler.pull_crowdnav_action()
	print(pulled_action)
	gazebo_state = apply_action_and_get_updated_gazebo_state(pulled_action)
	shared_memory_handler.push_gazebo_state(gazebo_state)


def apply_action_and_get_updated_gazebo_state(pulled_action):
	state = {
		'robot': 5,
		'goal': 12,
		'humans': 13.5
	}
	return state


if __name__ == '__main__':
	main()
