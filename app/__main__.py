"""
An example of detecting ArUco markers with OpenCV.
"""
import argparse
import os
from dotenv import load_dotenv
from utils import *
import threading
from socket_connection import connectSocket

# load .env file
load_dotenv()

# full server url for connection to the socket
# server_url = "http://{}:{}/".format(FLASK_SERVER_IP, FLASK_SERVER_PORT)

# default values
# foo = 0

# Argument parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-d', '--debug', default=False, action='store_true')
args = parser.parse_args()

# arg variables
debug = args.debug

def init(): 
    # start opencv
    print("Starting OpenCV")

# run!
init()