import socket
import os
from stat import S_ISSOCK
import json


class Keeper:
    def __init__(self, sockpath):
        self.sockpath = sockpath

    def connect_and_serve(self):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            s.connect(self.sockpath)

            while True:
                json_str = s.recv(65535)
                if json_str:
                    raw_data = json.dumps(json_str.decode("utf-8").replace("][", ","))
                    

                    try:
                        frame = init_frame(data)

                        vin = str(frame["vin"])

                        if vin in vehicles:
                            if !vehicles[vin]["route_detected"]:
                                detect_route(vehicles[vin], frame)
                        else:
                            vehicles[sys.intern(vin)] = init_vehicle(frame)

                        # только для ТС с определенным маршрутом можно проверять маршрут и остановки
                        if vehicles[vin]['route_detected'] and len(vehicles[vin]['route']) == 1:
                            check_route(vehicles[vin], frame)
                            check_platform(vehicles[vin], frame)

                            check_direction(vehicles[vin], frame)
                    except:
                        < EXCEPTION_CODE >

                else:
                    break

    def is_socket(self):
        result = True
        try:
            assert os.path.exists(self.sockpath), (
                f"Socket file {self.sockpath} does not exists"
            )

            assert S_ISSOCK(os.stat(self.sockpath).st_mode), (
                f"{self.sockpath} it is not a UNIX socket file"
            )
        except AssertionError as e:
            print(e)
            result = False
        finally:
            return result
