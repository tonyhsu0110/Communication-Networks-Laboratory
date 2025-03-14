# -*- coding: utf-8 -*-
import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7788")

print('Worker %s is running ...' % os.getpid())

while True:
    # Receive a, b from the client
    # 此處會用到的 function
    #   1. socket.recv_multipart()
    ''' start of you code '''
    a, b = socket.recv_multipart()
    c = int(a) + int(b)
    ''' end of you code '''

    # Return the result back to the client
    # 此處會用到的 function
    #   1. socket.send_string(....)
    ''' start of you code '''
    print("Compute " + a + " + " + b + " and send response")
    socket.send_multipart([str(c), str(os.getpid())])
    ''' end of you code '''


    a, b = socket.recv_multipart()
    c = int(a) + int(b)
    print("Compute " + a + " + " + b + " and send response")
    socket.send_multipart([str(c), str(os.getpid())])


