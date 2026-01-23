import time

def countdown_timer(seconds):
    while seconds > 0:
        mins=seconds//60 #gives dividant
        secs=seconds%60 #gives remainder
        timer = f"{mins:02d}:{secs:02d}" #Here 02d shows that it will show 2 digit 
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number.")
