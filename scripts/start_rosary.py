from rosary.rosary import setup_rosary, teardown_rosary, Rosary

def main():
    # Initialize the rosary object
    rosary = setup_rosary()
    rosary.set_day_of_week()

    #teardown the rosary object
    rosary = teardown_rosary()
    rosary.set_day_of_week()

if __name__ == "__main__":
    main()