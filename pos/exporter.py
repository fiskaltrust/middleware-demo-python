from mw_request import RestRequest
import time
from datetime import datetime

class Exporter:
    def __init__(self):
        pass

    def export_dsfinvk(self,mw_request:RestRequest,filepath,date_from = None, date_to = None):
        raw_export_data = mw_request.sendJournal(0x4445000000000002,date_from,date_to)
        current_date = datetime.now().strftime("%d%m%Y")
        save_loc = filepath + f"/dsfinvk_{current_date}.zip"
        try:
            dsfinvk = open(save_loc, "wb")
            dsfinvk.write(raw_export_data)
            dsfinvk.close()
            print("DSFinV-K saved to: " + save_loc)
        except:
            print("Error saving DSFinV-K")
    
    def date_to_ticks(date_string):
        date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S") #2024-01-01 06:00:00
        unix_timestamp = int(time.mktime(date_object.timetuple()))
        net_ticks = 621355968000000000 + unix_timestamp * 10000000
        return net_ticks
    
