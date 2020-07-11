from .gazebo_side.gazebo_controller import GazeboController
from .crowdnav_side.crowdnav_controller import CrowdNavController


class BidirectionalCrowdNavGazeboInterface(GazeboController, CrowdNavController):
	def find_action_for_state(self, state):
		converted_state = self.convert_gazebo_state_to_crowdnav_state(state)
		return super().find_action_for_state(converted_state)

	def execute_action(self, action):
		converted_action = self.convert_crowdnav_action_to_gazebo_action(action)
		super().execute_action(converted_action)

	def execute_action_and_get_new_state(self, action):
		converted_action = self.convert_crowdnav_action_to_gazebo_action(action)
		return super().execute_action_and_get_new_state(converted_action)

	def convert_gazebo_state_to_crowdnav_state(self, gazebo_state):
		# TODO: do coordinate and other conversions here
		return gazebo_state

	def convert_crowdnav_action_to_gazebo_action(self, crowdnav_action):
		# TODO: do coordinate and other conversions here
		return crowdnav_action
