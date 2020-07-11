from .script_that_generates_a_crowdnav_action_from_a_state import generate_crowdnav_action

class CrowdNavController:
	def find_action_for_state(self, action):
		return generate_crowdnav_action(action)
