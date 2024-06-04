import tensorflow as tf


def cv(pinout, status_q, stop_q, map_q, leds_q):
    while not stop_q.qsize():
        pass
        # TODO
        # - take image using camera
        # - process image into sobel edge tensor
        # - process edge tensor through model to get locations of road lines
        # - calculate positions of road lines using position/angle of camera
        # - send road line position data to map_q
