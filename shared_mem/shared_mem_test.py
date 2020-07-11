from multiprocessing import shared_memory, Manager
import sys
from math import pi

example_crowdnav_robot_action = {'v_x': 1,
                                 'v_y': 2,
                                 'alpha': pi}
# TODO: complete this example
example_gazebo_world_action = {'robot': {},
                               'goal': {},
                               'humans': []}

shared_crowdnav_to_gazebo_memory_name = "psm_crowdnav_to_gazebo"
shared_gazebo_to_crowdnav_memory_name = "psm_gazebo_to_crowdnav"
shared_crowdnav_to_gazebo_memory = None
shared_gazebo_to_crowdnav_memory = None



def test():
    setup_shared_memory_space()


def setup_shared_memory_space():
    shm_ctg = shared_memory.SharedMemory(name=shared_crowdnav_to_gazebo_memory_name, create=True,
                                         size=sys.getsizeof(example_crowdnav_robot_action))
    global shared_crowdnav_to_gazebo_memory
    shared_crowdnav_to_gazebo_memory = shm_ctg

    try:
        shm_gtc = shared_memory.SharedMemory(name=shared_gazebo_to_crowdnav_memory_name, create=True,
                                            size=sys.getsizeof(example_gazebo_world_action))
    except FileExistsError:
        shm_gtc = shared_memory.SharedMemory(name=shared_gazebo_to_crowdnav_memory_name, create=False,
                                            size=sys.getsizeof(example_gazebo_world_action))

    global shared_gazebo_to_crowdnav_memory
    shared_gazebo_to_crowdnav_memory= shm_gtc


class CrowdNavGazeboInterfaceManager:
    def __init__(self, max_number_of_buffered_states=10):
        if max_number_of_buffered_states < 1:
            raise ValueError(f"max_number_of_buffered_states is {max_number_of_buffered_states}. Must be at least 1!")
        self.buffered_gazebo_states = []
        self.current_gazebo_state_index = -1
        self.max_number_of_buffered_states = max_number_of_buffered_states
        self.last_error_message = 'No error has occurred yet.'
        self.last_method_success = False

    def get_most_recent_gazebo_state(self):
        if self.buffered_gazebo_states:
            self.last_method_success = True
            return self.buffered_gazebo_states[-1], len(self.buffered_gazebo_states)-1
        self.last_method_success = False
        self.last_error_message = "No buffered states: There are no states in the buffer to get."
        return False

    def get_next_gazebo_state(self):
        if self.buffered_gazebo_states and self.current_gazebo_state_index + 1 < len(self.buffered_gazebo_states):
            self.current_gazebo_state_index += 1
            self.last_method_success = True
            return self.buffered_gazebo_states[self.current_gazebo_state_index]
        self.last_error_message = "Current state index out of range: " \
                                  "There is either no buffered state left or no new state to return"
        self.last_method_success = False
        return False

    def get_current_gazebo_state(self):
        if self.current_gazebo_state_index < 0:
            self.last_method_success = False
            self.last_error_message = "Current state no longer in memory: " \
                                      "It was either pushed out of the buffer or has not been filled to begin with."
            return False
        elif self.current_gazebo_state_index > len(self.buffered_gazebo_states):
            # Should never happen
            self.last_method_success = False
            self.last_error_message = "Current state index out of range: " \
                                      "This should not happen when returning the current state. " \
                                      "Something must have failed."
            return False
        self.last_method_success = True
        return self.buffered_gazebo_states[self.current_gazebo_state_index]

    def pull_gazebo_state(self):
        # Get the state
        new_state = ''  # TODO: implement

        # TODO: implement routine for when len() has more than 1 more than allowed
        # Check if the buffer limit has been reached
        if len(self.buffered_gazebo_states) == self.max_number_of_buffered_states:
            # Delete the oldest entry and adjust the index accordingly
            del self.buffered_gazebo_states[0]
            self.current_gazebo_state_index -= 1

        # Buffer and return the state
        self.buffered_gazebo_states.append(new_state)
        self.last_method_success = True
        return new_state

    def push_crowdnav_action(self, crowdnav_action):
        # TODO: implement
        return True


if __name__ == '__main__':
    test()
