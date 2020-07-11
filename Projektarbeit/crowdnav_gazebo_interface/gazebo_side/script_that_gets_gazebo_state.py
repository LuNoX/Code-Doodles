

def main():
	return get_gazebo_state() 


def get_gazebo_state():
	state = {
		'robot': {
					'p_x': 3,
					'p_y': 4
				},
		'goal': {
					'p_x': 3,
					'p_y': 5
				},
		'humans': 13.5
	}
	return state

if __name__ == "__main__":
	main()
