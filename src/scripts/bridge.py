from PSL import sciencelab
import sys
import threading
import json
from oscilloscope import Oscilloscope


def main():
    I = None
    oscilloscope = None
    data_read_thread = None

    try:
        I = sciencelab.connect()
        output = {'type': 'DEVICE_CONNECTION_STATUS', 'isConnected': True}
    except:
        output = {'type': 'DEVICE_CONNECTION_STATUS', 'isConnected': False}
    print(json.dumps(output))
    sys.stdout.flush()

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
            data_read_thread = oscilloscope.readData()
            data_read_thread.start()

        if command == "STOP_OSC":
            oscilloscope.isReading = False
            data_read_thread.join()

        if command == "CONFIG_OSC":
            pass

        if command == 'CONFIG_PWR_SRC':
            pcs_value = parsed_stream_data['pcs']
            pv1_value = parsed_stream_data['pv1']
            pv2_value = parsed_stream_data['pv2']
            pv3_value = parsed_stream_data['pv3']
            I.set_pcs(pcs_value)
            I.set_pv1(pv1_value)
            I.set_pv2(pv2_value)
            I.set_pv3(pv3_value)

        # -------------------------- Script termination block ----------------------------
        if command == 'KILL':
            break


if __name__ == '__main__':
    main()
