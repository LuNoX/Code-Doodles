

def main():
	return get_gazebo_state() 


def get_gazebo_state():
	state = {
		'robot': 5,
		'goal': 12,
		'humans': 13.5
	}
	return state

if __name__ == "__main__":
	main()
