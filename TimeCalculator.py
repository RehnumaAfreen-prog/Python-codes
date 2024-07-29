def add_time(start, duration,start_day = None):
    start = start.split() 

    c_time = str(start[0]) 
    hr1, min1 = c_time.split(":")
    hr2, min2 = duration.split(":")
    hours = int(hr1) + int(hr2)
    mins = int(min1) + int(min2)
    x= mins/60

    if start[1] == "AM":

        if x >= 1:
            h, y = str(x).split(".") 
            m = mins -(int(h)*60)
            hours += int(h)   
            if hours >=12:
                hours -= 12
                print(str(hours) +":"+ str(m) + " " + "PM")
            else:
                print(str(hours) +":"+ str(m) + " " + "AM")
        else:
            if hours >=12:
                hours -= 12
                print(str(hours) +":"+ str(mins) + " " + "PM")
            else:
                print(str(hours) +":"+ str(mins) + " " + "AM")

    elif start[1] == "PM":
        if x >= 1:
            h, y = str(x).split(".") 
            m = mins -(int(h)*60)
            hours += int(h)    
            if hours >=12:
                hours -= 12
                print(str(hours) +":"+ str(m) + " " + "AM"+ "(next day)")
            else:
                print(str(hours) +":"+ str(m) + " " + "PM")
        else:
            if hours >=12:
                hours -= 12
                print(str(hours) +":"+ str(mins) + " " + "AM" + "(next day)")
            else:
                print(str(hours) +":"+ str(mins) + " " + "PM")
    else:
        print("wrong time format (AM/PM)!")


add_time("7:30 PM", "2:50")








#return new_time