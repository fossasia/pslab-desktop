import sys
import json


class Wave_generator:
    def __init__(self, I):
        self.device = I
        self.s1_frequency = 500
        self.s2_frequency = 500
        self.s2_phase = 90
        self.wave_form_s1 = 'sine'
        self.wave_form_s2 = 'sine'
        self.sqr1_frequency = 500
        self.sqr1_duty_cycle = 50
        self.sqr2_frequency = 500
        self.sqr2_duty_cycle = 50
        self.sqr2_phase = 90
        self.sqr3_frequency = 500
        self.sqr3_duty_cycle = 50
        self.sqr3_phase = 90
        self.sqr4_frequency = 500
        self.sqr4_duty_cycle = 50
        self.sqr4_phase = 90
        self.mode = 'square'
        self.change_device_settings()

    def set_config(self, s1_frequency, s2_frequency, s2_phase, wave_form_s1,
                   wave_form_s2, sqr1_frequency, sqr1_duty_cycle,
                   sqr2_frequency, sqr2_duty_cycle, sqr2_phase, sqr3_frequency,
                   sqr3_duty_cycle, sqr3_phase, sqr4_frequency,
                   sqr4_duty_cycle, sqr4_phase, mode):
        self.s1_frequency = s1_frequency
        self.s2_frequency = s2_frequency
        self.s2_phase = s2_phase
        self.wave_form_s1 = wave_form_s1
        self.wave_form_s2 = wave_form_s2
        self.sqr1_frequency = sqr1_frequency
        self.sqr1_duty_cycle = sqr1_duty_cycle
        self.sqr2_frequency = sqr2_frequency
        self.sqr2_duty_cycle = sqr2_duty_cycle
        self.sqr2_phase = sqr2_phase
        self.sqr3_frequency = sqr3_frequency
        self.sqr3_duty_cycle = sqr3_duty_cycle
        self.sqr3_phase = sqr3_phase
        self.sqr4_frequency = sqr4_frequency
        self.sqr4_duty_cycle = sqr4_duty_cycle
        self.sqr4_phase = sqr4_phase
        self.mode = mode
        self.change_device_settings()

    def change_device_settings(self):
        self.device.set_w1(self.s1_frequency, waveType=self.wave_form_s1)
        self.device.set_w2(self.s2_frequency, waveType=self.wave_form_s2)
        self.device.set_waves(
            self.s1_frequency, self.s2_phase, self.s2_frequency)
        # self.device.sqrPWM(self.sqr1_frequency,  self.sqr1_duty_cycle/100.,
        #                    self.sqr2_phase/360., self.sqr2_duty_cycle/100.,
        #                    self.sqr3_phase/360., self.sqr3_duty_cycle/100.,
        #                    self.sqr4_phase/360., self.sqr4_duty_cycle/100.)
        # self.device.sqr1(self.sqr1_frequency, self.sqr1_duty_cycle)
        # self.device.sqr2(self.sqr2_frequency, self.sqr2_duty_cycle)

    def get_config(self):
        output = {'type': 'GET_CONFIG_WAV_GEN',
                  's1Frequency': self.s1_frequency,
                  's2Frequency': self.s2_frequency,
                  's2Phase': self.s2_phase,
                  'waveFormS1': self.wave_form_s1,
                  'waveFormS2': self.wave_form_s2,
                  'sqr1Frequency': self.sqr1_frequency,
                  'sqr1DutyCycle': self.sqr1_duty_cycle,
                  'sqr2Frequency': self.sqr2_frequency,
                  'sqr2DutyCycle': self.sqr2_duty_cycle,
                  'sqr2Phase': self.sqr2_phase,
                  'sqr3Frequency': self.sqr3_frequency,
                  'sqr3DutyCycle': self.sqr3_duty_cycle,
                  'sqr3Phase': self.sqr3_phase,
                  'sqr4Frequency': self.sqr4_frequency,
                  'sqr4DutyCycle': self.sqr4_duty_cycle,
                  'sqr4Phase': self.sqr4_phase,
                  'mode': self.mode,
                  }
        print(json.dumps(output))
        sys.stdout.flush()
