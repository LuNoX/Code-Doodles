from script_that_executes_gazebo_actions import execute_gazebo_action
from script_that_gets_gazebo_state import get_gazebo_state


class GazeboController:
	def get_state(self):
		return get_gazebo_state

	def execute_action(self, action):
		execute_gazebo_action(action)

	def execute_action_and_get_new_state(self, action):
		self.execute_action(action)
		return self.get_state()
