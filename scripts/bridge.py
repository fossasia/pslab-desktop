import sys
import time
import threading
import json
from file_write import FileWrite
from oscilloscope import Oscilloscope
from logic_analyser import LogicAnalyser
from device_detection import Device_detection
from power_source import Power_source
from multimeter import Multimeter
from wave_generator import Wave_generator
from robotic_arm import RoboticArm
from sensors import Sensors

def main():
    file_write = FileWrite()
    device_detection = Device_detection()
    device_detection.async_connect()
    I = device_detection.device

    # instrument cluster initialization
    oscilloscope = Oscilloscope(I, file_write)
    logic_analyser = LogicAnalyser(I, file_write)
    power_source = Power_source(I, file_write)
    multimeter = Multimeter(I, file_write)
    wave_generator = Wave_generator(I, file_write)
    robotic_arm = RoboticArm(I, file_write)
    sensors = Sensors(I, file_write)

    while(True):
        in_stream_data = input()
        parsed_stream_data = json.loads(in_stream_data)
        command = parsed_stream_data['command']

        # ---------------------------- Oscilloscope block ------------------------------
        if command == 'START_OSC':
            oscilloscope.start_read()

        if command == "STOP_OSC":
            oscilloscope.stop_read()

        if command == "SET_CONFIG_OSC":
            old_read_state = oscilloscope.is_reading_voltage or oscilloscope.is_reading_fft
            if oscilloscope.is_reading_voltage or oscilloscope.is_reading_fft:
                oscilloscope.stop_read()

            time_base = parsed_stream_data['timeBase']
            number_of_samples = parsed_stream_data['numberOfSamples']
            ch1 = parsed_stream_data['ch1']
            ch2 = parsed_stream_data['ch2']
            ch3 = parsed_stream_data['ch3']
            mic = parsed_stream_data['mic']
            # ch1_map = parsed_stream_data['ch1Map']
            # ch2_map = parsed_stream_data['ch2Map']
            # ch3_map = parsed_stream_data['ch3Map']
            is_trigger_active = parsed_stream_data['isTriggerActive']
            trigger_voltage = parsed_stream_data['triggerVoltage']
            trigger_channel = parsed_stream_data['triggerChannel']
            is_fourier_transform_active = parsed_stream_data['isFourierTransformActive']
            fit_type = parsed_stream_data['fitType']
            fit_channel1 = parsed_stream_data['fitChannel1']
            fit_channel2 = parsed_stream_data['fitChannel2']
            is_xy_plot_active = parsed_stream_data['isXYPlotActive']
            plot_channel1 = parsed_stream_data['plotChannel1']
            plot_channel2 = parsed_stream_data['plotChannel2']
            oscilloscope.set_config(
                time_base, number_of_samples, ch1, ch2, ch3, mic,
                is_trigger_active, trigger_channel, trigger_voltage,
                is_fourier_transform_active, fit_type, fit_channel1,
                fit_channel2, is_xy_plot_active, plot_channel1, plot_channel2)

            if old_read_state:
                oscilloscope.start_read()

        if command == 'GET_CONFIG_OSC':
            oscilloscope.get_config()

        # ---------------------------- LA block ------------------------------
        if command == 'START_LA':
            logic_analyser.start_read()

        if command == "STOP_LA":
            logic_analyser.stop_read()

        if command == "SET_CONFIG_LA":
            number_of_channels = parsed_stream_data['numberOfChannels']
            trigger1_type = parsed_stream_data['trigger1Type']
            trigger2_type = parsed_stream_data['trigger2Type']
            trigger3_type = parsed_stream_data['trigger3Type']
            trigger4_type = parsed_stream_data['trigger4Type']
            capture_time = parsed_stream_data['captureTime']
            logic_analyser.set_config(
                number_of_channels, trigger1_type, trigger2_type, trigger3_type, trigger4_type,capture_time)

        if command == 'GET_CONFIG_LA':
            logic_analyser.get_config()

        # --------------------------- Multimeter block ---------------------------------
        if command == 'START_MUL_MET':
            multimeter.start_read()

        if command == 'STOP_MUL_MET':
            multimeter.stop_read()

        if command == 'SET_CONFIG_MUL_MET':
            old_read_state = multimeter.is_reading
            if multimeter.is_reading:
                multimeter.stop_read()

            active_category = parsed_stream_data['activeCategory']
            active_subtype = parsed_stream_data['activeSubType']
            parameter = None
            if active_category == 'PULSE':
                parameter = parsed_stream_data['parameter']
            multimeter.set_config(active_category, active_subtype, parameter)

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

        if command == 'GET_CONFIG_PWR_SRC_FILE':
            data_path = parsed_stream_data['dataPath']
            power_source.get_config_from_file(data_path)

        if command == 'SAVE_CONFIG_PWR_SRC':
            data_path = parsed_stream_data['dataPath']
            power_source.save_config(data_path)

        # -------------------------- Wave Generator block ---------------------------------
        if command == 'SET_CONFIG_WAV_GEN':
            wave = parsed_stream_data['wave']
            digital = parsed_stream_data['digital']
            s1_frequency = parsed_stream_data['s1Frequency']
            s2_frequency = parsed_stream_data['s2Frequency']
            s2_phase = parsed_stream_data['s2Phase']
            wave_form_s1 = parsed_stream_data['waveFormS1']
            wave_form_s2 = parsed_stream_data['waveFormS2']
            pwm_frequency = parsed_stream_data['pwmFrequency']
            sqr1_duty_cycle = parsed_stream_data['sqr1DutyCycle']
            sqr2_duty_cycle = parsed_stream_data['sqr2DutyCycle']
            sqr2_phase = parsed_stream_data['sqr2Phase']
            sqr3_duty_cycle = parsed_stream_data['sqr3DutyCycle']
            sqr3_phase = parsed_stream_data['sqr3Phase']
            sqr4_duty_cycle = parsed_stream_data['sqr4DutyCycle']
            sqr4_phase = parsed_stream_data['sqr4Phase']
            wave_generator.set_config(
                wave, digital,
                s1_frequency, s2_frequency, s2_phase, wave_form_s1,
                wave_form_s2, pwm_frequency, sqr1_duty_cycle,
                sqr2_duty_cycle, sqr2_phase,
                sqr3_duty_cycle, sqr3_phase,
                sqr4_duty_cycle, sqr4_phase)

        if command == 'GET_CONFIG_WAV_GEN':
            wave_generator.get_config()

        if command == 'GET_CONFIG_WAV_GEN_FILE':
            data_path = parsed_stream_data['dataPath']
            wave_generator.get_config_from_file(data_path)

        if command == 'SAVE_CONFIG_WAV_GEN':
            data_path = parsed_stream_data['dataPath']
            wave_generator.save_config(data_path)

        # ------------------------------- Robtic Arm block -------------------------------
        if command == 'SET_ROB_ARM':
            angle1 = parsed_stream_data['angle1']
            angle2 = parsed_stream_data['angle2']
            angle3 = parsed_stream_data['angle3']
            angle4 = parsed_stream_data['angle4']
            robotic_arm.setServo(angle1, angle2, angle3, angle4)

        # ------------------------------- Sensors block ----------------------------------
        if command == 'SENSORS_SCAN':
            sensors.scan()

        # -------------------------------- Write block -----------------------------------

        if command == 'START_WRITE':
            data_path = parsed_stream_data['dataPath']
            device_type = parsed_stream_data['deviceType']
            file_write.start_recording(data_path, device_type)

        if command == 'STOP_WRITE':
            file_write.stop_recording()

        # -------------------------- Script termination block ----------------------------
        if command == 'KILL':
            exit()


if __name__ == '__main__':
    main()
    print("app exited successfully")
    sys.stdout.flush()
