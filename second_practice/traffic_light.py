def traffic_light():
    """Simulate traffic light behavior"""
    color = input("input 'red', 'yellow' or 'green' : ")
    if(color == "green"):
        print("go")
    elif(color == "red" or color == "yellow"):
        print("stop")
    else:
        print("incorrect input")


traffic_light()
