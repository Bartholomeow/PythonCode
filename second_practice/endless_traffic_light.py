def endless_traffic_light():
    """Simulate endless traffic light behavior"""
    while(1):
        color = input("input 'red', 'yellow', 'green' or 'quit' : ")
        if(color == "green"):
            print("go")
        elif(color == "quit"):
            print("end")
            break
        elif(color == "red" or color == "yellow"):
            print("stop")
        else:
            print("incorrect input")


endless_traffic_light()
