from .gazebo_side.gazebo_controller import GazeboController
from .crowdnav_side.crowdnav_controller import CrowdNavController


class BidirectionalCrowdNavGazeboInterface(GazeboController, CrowdNavController):
	# TODO: do coordinate and other conversions here
	pass
