import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
from bite.stacked_hourglass.model import hg1, hg2, hg4, hg8
from bite.stacked_hourglass.predictor import HumanPosePredictor
