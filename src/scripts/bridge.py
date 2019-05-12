import sys
import threading
import json
from oscilloscope import Oscilloscope
from device_detection import Device_detection


def main():
    I = None
    oscilloscope = None
    oscilloscope_data_read_thread = None
    device_detection = None
    device_detection_thread = None

    # connection and connection check loop initialization
    device_detection = Device_detection()
    device_detection_thread = device_detection.async_connect()
    device_detection_thread.start()
    I = device_detection.device

    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']

        # ---------------------------- Oscilloscope block ------------------------------
        if command == 'START_OSC':
            # for test
            I.set_sine1(1000)
            I.set_sine2(500)

            time_gap = parsed_stream_data['timeGap']
            number_of_samples = parsed_stream_data['numberOfSamples']
            delay = parsed_stream_data['delay']
            ch1 = parsed_stream_data['ch1']
            ch2 = parsed_stream_data['ch2']
            ch3 = parsed_stream_data['ch3']
            ch4 = parsed_stream_data['ch4']

            oscilloscope = Oscilloscope(
                I, time_gap, number_of_samples, delay, ch1, ch2, ch3, ch4)
            oscilloscope_data_read_thread = oscilloscope.readData()
            oscilloscope_data_read_thread.start()

        if command == "STOP_OSC":
            oscilloscope.isReading = False
            oscilloscope_data_read_thread.join()

        if command == "CONFIG_OSC":
            pass

        # -------------------------- Power Source block ---------------------------------
        if command == 'SET_CONFIG_PWR_SRC':
            pcs_value = parsed_stream_data['pcs']
            pv1_value = parsed_stream_data['pv1']
            pv2_value = parsed_stream_data['pv2']
            pv3_value = parsed_stream_data['pv3']
            I.set_pcs(pcs_value)
            I.set_pv1(pv1_value)
            I.set_pv2(pv2_value)
            I.set_pv3(pv3_value)

        if command == 'GET_CONFIG_PWR_SRC':
            pcs_value = I.get_pcs()
            pv1_value = I.get_pv1()
            pv2_value = I.get_pv2()
            pv3_value = I.get_pv3()
            output = {'type': 'GET_CONFIG_PWR_SRC',
                      'pcs': pcs_value,
                      'pv1': pv1_value,
                      'pv2': pv2_value,
                      'pv3': pv3_value}
            print(json.dumps(output))
            sys.stdout.flush()

        # -------------------------- Script termination block ----------------------------
        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
    print("app exited successfully")
    sys.stdout.flush()
