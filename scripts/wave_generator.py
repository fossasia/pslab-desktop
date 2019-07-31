import sys
import json
import time
import datetime


class Wave_generator:
    def __init__(self, I, file_write):
        self.file_write = file_write

        self.device = I
        self.wave = True
        self.digital = False
        self.s1_frequency = 500
        self.s2_frequency = 500
        self.s2_phase = 90
        self.wave_form_s1 = 'sine'
        self.wave_form_s2 = 'sine'
        self.pwm_frequency = 500
        self.sqr1_duty_cycle = 50
        self.sqr2_duty_cycle = 50
        self.sqr2_phase = 90
        self.sqr3_duty_cycle = 50
        self.sqr3_phase = 90
        self.sqr4_duty_cycle = 50
        self.sqr4_phase = 90
        self.change_device_settings()

    def set_config(self, wave, digital,
                   s1_frequency, s2_frequency, s2_phase, wave_form_s1,
                   wave_form_s2, pwm_frequency, sqr1_duty_cycle,
                   sqr2_duty_cycle, sqr2_phase,
                   sqr3_duty_cycle, sqr3_phase,
                   sqr4_duty_cycle, sqr4_phase):
        self.wave = wave
        self.digital = digital
        self.s1_frequency = s1_frequency
        self.s2_frequency = s2_frequency
        self.s2_phase = s2_phase
        self.wave_form_s1 = wave_form_s1
        self.wave_form_s2 = wave_form_s2
        self.pwm_frequency = pwm_frequency
        self.sqr1_duty_cycle = sqr1_duty_cycle
        self.sqr2_duty_cycle = sqr2_duty_cycle
        self.sqr2_phase = sqr2_phase
        self.sqr3_duty_cycle = sqr3_duty_cycle
        self.sqr3_phase = sqr3_phase
        self.sqr4_duty_cycle = sqr4_duty_cycle
        self.sqr4_phase = sqr4_phase
        self.change_device_settings()

    def change_device_settings(self):
        if self.wave:
            self.device.set_w1(self.s1_frequency, waveType=self.wave_form_s1)
            self.device.set_w2(self.s2_frequency, waveType=self.wave_form_s2)
            self.device.set_waves(
                self.s1_frequency, self.s2_phase, self.s2_frequency)
        else:
            self.device.sqrPWM(self.pwm_frequency,  self.sqr1_duty_cycle/100.,
                               self.sqr2_phase/360., self.sqr2_duty_cycle/100.,
                               self.sqr3_phase/360., self.sqr3_duty_cycle/100.,
                               self.sqr4_phase/360., self.sqr4_duty_cycle/100.)

    def get_config(self):
        output = {'type': 'GET_CONFIG_WAV_GEN',
                  'wave': self.wave,
                  'digital': self.digital,
                  's1Frequency': self.s1_frequency,
                  's2Frequency': self.s2_frequency,
                  's2Phase': self.s2_phase,
                  'waveFormS1': self.wave_form_s1,
                  'waveFormS2': self.wave_form_s2,
                  'pwmFrequency': self.pwm_frequency,
                  'sqr1DutyCycle': self.sqr1_duty_cycle,
                  'sqr2DutyCycle': self.sqr2_duty_cycle,
                  'sqr2Phase': self.sqr2_phase,
                  'sqr3DutyCycle': self.sqr3_duty_cycle,
                  'sqr3Phase': self.sqr3_phase,
                  'sqr4DutyCycle': self.sqr4_duty_cycle,
                  'sqr4Phase': self.sqr4_phase,
                  }
        print(json.dumps(output))
        sys.stdout.flush()

    def get_config_from_file(self, data_path):
        self.file_write.get_config_from_file(data_path, "WaveGenerator")

    def save_config(self, data_path):
        datetime_data = datetime.datetime.now()
        timestamp = time.time()
        self.file_write.save_config(
            data_path, "WaveGenerator",  timestamp=timestamp, datetime=datetime_data,
            wave=self.wave, digital=self.digital, s1_f=self.s1_frequency, s1_shape=self.wave_form_s1,
            s2_f=self.s2_frequency, s2_p=self.s2_phase, s2_shape=self.wave_form_s2,
            pwm_f=self.pwm_frequency,
            dc_1=self.sqr1_duty_cycle,
            p2=self.sqr2_phase, dc_2=self.sqr2_duty_cycle,
            p3=self.sqr3_phase, dc_3=self.sqr3_duty_cycle,
            p4=self.sqr4_phase, dc_4=self.sqr4_duty_cycle)
