from crowdnav_gazebo_interface.crowdnav_gazebo_interface import BidirectionalCrowdNavGazeboInterface


def main():
	interface = BidirectionalCrowdNavGazeboInterface()
	state = interface.get_state() 
	while not goal_is_reached(state):
		action = interface.find_action_for_state(state)
		state = interface.execute_action_and_get_new_state(action)
		print(state)
	return


def goal_is_reached(state):
	return state['robot']['p_x'] == state['goal']['p_x'] and state['robot']['p_y'] == state['goal']['p_y']


if __name__ == '__main__':
	main()
