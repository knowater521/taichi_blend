import bpy
import numpy as np

from .addon import *
from .numio import *
from .anim import *
from .helper import *
from .wrapper import *
from .console import *



def init():
    register()
    clear_animations()
