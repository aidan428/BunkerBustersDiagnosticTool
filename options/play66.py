from playsound import playsound

def order_66():
    try:
        playsound("assets/66.mp3")
    except Exception as e:
        print("Execute Order 66.")

