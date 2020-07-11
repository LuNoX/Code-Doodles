

def main(state):
	generate_crowdnav_action(state)


def generate_crowdnav_action(state):
	action = {
		'v_x': 3,
		'v_y': 4,
		'omega': 2.5
	}
	return action


if __name__ == '__main__':
	main()
