import datetime
def transport_nearest_origtime(data):
    global transport_orig_datetime
    if depart_year != "":
        print('出発したい時間は{}'.format(transport_orig_datetime))
        for i in range(0,len(data)-1):
            if data[i]>transport_orig_datetime:
                print((datetime.datetime(data[i])-datetimetransport_orig_datetime).seconds)
                return min(data, key=lambda p: (datetime.datetime(p)-datetimetransport_orig_datetime).seconds, default="")
            else:
                pass
    elif arrival_year != "":
        print('到着したい時間は')
        print(transport_orig_datetime)
        return min(data, key=lambda p: (datetime.datetime.strptime(dest_stop_time.strftime("%Y/%m/%d %H:%M"),"%Y/%m/%d %H:%M")-p).seconds, default="")
    else:
        return None
                
                    
def transport_nearest_desttime(data):
    if depart_year != "":
        print('出発したい時間は')
        print(orig_stop_time)
        return min(data, key=lambda p: (datetime.datetime.strptime(orig_stop_time.strftime("%Y/%m/%d %H:%M"),"%Y/%m/%d %H:%M")-p).seconds, default="")
    elif arrival_year != "":
        print('到着したい時間は')
        print(transport_orig_datetime)
        return min(data, key=lambda p: (datetime.datetime.strptime(transport_orig_datetime.strftime("%Y/%m/%d %H:%M"),"%Y/%m/%d %H:%M")-p).seconds, default="")
    else:
        return None
