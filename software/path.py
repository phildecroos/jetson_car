def path(pinout, status_q, stop_q, map_q, motors_q):
    while not stop_q.qsize():
        pass
        # TODO
        # - read data from map_q (cv inputs and motor encoder readings)
        # - process map data into model of known area (2D overhead map)
        # - plan a robot path using the model
        # - send motor commands associated with planned path to motors_q
