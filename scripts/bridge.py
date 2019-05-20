import sys
import threading
import json
from oscilloscope import Oscilloscope
from device_detection import Device_detection
from power_source import Power_source
from multimeter import Multimeter


def main():
    device_detection = Device_detection()
    device_detection.async_connect()
    I = device_detection.device

    # instrument cluster initialization
    oscilloscope = Oscilloscope(I)
    power_source = Power_source(I)
    multimeter = Multimeter(I)

    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']

        # ---------------------------- Oscilloscope block ------------------------------
        if command == 'START_OSC':
            # for test
            I.set_sine1(1000)
            I.set_sine2(500)

            oscilloscope.start_read()

        if command == "STOP_OSC":
            oscilloscope.stop_read()

        if command == "SET_CONFIG_OSC":
            old_read_state = oscilloscope.is_reading
            if oscilloscope.is_reading:
                oscilloscope.stop_read()

            time_gap = parsed_stream_data['timeGap']
            number_of_samples = parsed_stream_data['numberOfSamples']
            ch1 = parsed_stream_data['ch1']
            ch2 = parsed_stream_data['ch2']
            ch3 = parsed_stream_data['ch3']
            ch4 = parsed_stream_data['ch4']
            # ch1_map = parsed_stream_data['ch1Map']
            # ch2_map = parsed_stream_data['ch2Map']
            # ch3_map = parsed_stream_data['ch3Map']
            # is_mic_active = parsed_stream_data['mapToMic']
            trigger_voltage = parsed_stream_data['triggerVoltage']
            trigger_channel = parsed_stream_data['triggerVoltageChannel']
            is_trigger_active = parsed_stream_data['isTriggerActive']
            # is_fourier_transform_active = parsed_stream_data['isFourierTransformActive']
            # transform_type = parsed_stream_data['transformType']
            # transform_channel1 = parsed_stream_data['transformChannel1']
            # transform_channel2 = parsed_stream_data['transformChannel2']
            # is_xy_plot_active = parsed_stream_data['isXYPlotActive']
            # plot_channel1 = parsed_stream_data['plotChannel1']
            # plot_channel2 = parsed_stream_data['plotChannel2']

            oscilloscope.set_config(
                time_gap, number_of_samples, ch1, ch2, ch3, ch4, trigger_channel, trigger_voltage, is_trigger_active)

            if old_read_state:
                oscilloscope.start_read()

        if command == 'GET_CONFIG_OSC':
            oscilloscope.get_config()

        # --------------------------- Multimeter block ---------------------------------
        if command == 'START_MUL_MET':
            multimeter.start_read()

        if command == 'STOP_MUL_MET':
            multimeter.stop_read()

        if command == 'SET_CONFIG_MUL_MET':
            old_read_state = multimeter.is_reading
            if multimeter.is_reading:
                multimeter.stop_read()

            active_catagory = parsed_stream_data['activeCatagory']
            active_subtype = parsed_stream_data['activeSubType']
            parameter = None
            if active_catagory == 'PULSE':
                parameter = parsed_stream_data['parameter']
            multimeter.set_config(active_catagory, active_subtype, parameter)

            if old_read_state:
                multimeter.start_read()

        if command == 'GET_CONFIG_MUL_MET':
            multimeter.get_config()

        # -------------------------- Power Source block ---------------------------------
        if command == 'SET_CONFIG_PWR_SRC':
            pcs_value = parsed_stream_data['pcs']
            pv1_value = parsed_stream_data['pv1']
            pv2_value = parsed_stream_data['pv2']
            pv3_value = parsed_stream_data['pv3']
            power_source.set_config(pcs_value, pv1_value, pv2_value, pv3_value)

        if command == 'GET_CONFIG_PWR_SRC':
            power_source.get_config()

        # -------------------------- Script termination block ----------------------------
        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
    print("app exited successfully")
    sys.stdout.flush()
