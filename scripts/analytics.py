import math
from typing import Tuple

import numpy as np


class analyticsClass():
    """
    This class contains methods that allow mathematical analysis such as curve fitting
    """

    def __init__(self):
        try:
            import scipy.optimize as optimize
        except ImportError:
            self.optimize = None
        else:
            self.optimize = optimize

        try:
            import scipy.fftpack as fftpack
        except ImportError:
            self.fftpack = None
        else:
            self.fftpack = fftpack

        try:
            from scipy.optimize import leastsq
        except ImportError:
            self.leastsq = None
        else:
            self.leastsq = leastsq

        try:
            import scipy.signal as signal
        except ImportError:
            self.signal = None
        else:
            self.signal = signal

    def sineFunc(self, x, a1, a2, a3, a4):
        return a4 + a1 * np.sin(abs(a2 * (2 * np.pi)) * x + a3)

    def squareFunc(self, x, amp, freq, phase, dc, offset):
        return offset + amp * self.signal.square(2 * np.pi * freq * (x - phase), duty=dc)

    # -------------------------- Exponential Fit ----------------------------------------

    def func(self, x, a, b, c):
        return a * np.exp(-x / b) + c

    def fit_exp(self, t, v):  # accepts numpy arrays
        size = len(t)
        v80 = v[0] * 0.8
        for k in range(size - 1):
            if v[k] < v80:
                rc = t[k] / .223
                break
        pg = [v[0], rc, 0]
        po, err = self.optimize.curve_fit(self.func, t, v, pg)
        if abs(err[0][0]) > 0.1:
            return None, None
        vf = po[0] * np.exp(-t / po[1]) + po[2]
        return po, vf

    def squareFit(self, xReal, yReal):
        N = len(xReal)
        mx = yReal.max()
        mn = yReal.min()
        OFFSET = (mx + mn) / 2.
        amplitude = (np.average(yReal[yReal > OFFSET]) - np.average(yReal[yReal < OFFSET])) / 2.0
        yTmp = np.select([yReal < OFFSET, yReal > OFFSET], [0, 2])
        bools = abs(np.diff(yTmp)) > 1
        edges = xReal[bools]
        levels = yTmp[bools]
        frequency = 1. / (edges[2] - edges[0])

        phase = edges[0]  # .5*np.pi*((yReal[0]-offset)/amplitude)
        dc = 0.5
        if len(edges) >= 4:
            if levels[0] == 0:
                dc = (edges[1] - edges[0]) / (edges[2] - edges[0])
            else:
                dc = (edges[2] - edges[1]) / (edges[3] - edges[1])
                phase = edges[1]

        guess = [amplitude, frequency, phase, dc, 0]

        try:
            (amplitude, frequency, phase, dc, offset), pcov = self.optimize.curve_fit(self.squareFunc, xReal,
                                                                                      yReal - OFFSET, guess)
            offset += OFFSET

            if (frequency < 0):
                # print ('negative frq')
                return False

            freq = 1e6 * abs(frequency)
            amp = abs(amplitude)
            pcov[0] *= 1e6
            # print (pcov)
            if (abs(pcov[-1][0]) > 1e-6):
                False
            return [amp, freq, phase, dc, offset]
        except:
            return False

    def sineFit(self, xReal, yReal, **kwargs):
        N = len(xReal)
        OFFSET = (yReal.max() + yReal.min()) / 2.
        yhat = self.fftpack.rfft(yReal - OFFSET)
        idx = (yhat ** 2).argmax()
        freqs = self.fftpack.rfftfreq(N, d=(xReal[1] - xReal[0]) / (2 * np.pi))
        frequency = kwargs.get('freq', freqs[idx])
        frequency /= (2 * np.pi)  # Convert angular velocity to freq
        amplitude = kwargs.get('amp', (yReal.max() - yReal.min()) / 2.0)
        phase = kwargs.get('phase', 0)  # .5*np.pi*((yReal[0]-offset)/amplitude)
        guess = [amplitude, frequency, phase, 0]
        try:
            (amplitude, frequency, phase, offset), pcov = self.optimize.curve_fit(self.sineFunc, xReal, yReal - OFFSET,
                                                                                  guess)
            offset += OFFSET
            ph = ((phase) * 180 / (np.pi))
            if (frequency < 0):
                # print ('negative frq')
                return False

            if (amplitude < 0):
                ph -= 180

            if (ph < 0):
                ph = (ph + 720) % 360

            freq = 1e6 * abs(frequency)
            amp = abs(amplitude)
            pcov[0] *= 1e6
            # print (pcov)
            if (abs(pcov[-1][0]) > 1e-6):
                return False
            return [amp, freq, offset, ph]
        except:
            return False

    def find_frequency(self, v, si):  # voltages, samplimg interval is seconds
        from numpy import fft
        NP = len(v)
        v = v - v.mean()  # remove DC component
        frq = fft.fftfreq(NP, si)[:NP / 2]  # take only the +ive half of the frequncy array
        amp = abs(fft.fft(v)[:NP / 2]) / NP  # and the fft result
        index = amp.argmax()  # search for the tallest peak, the fundamental
        return frq[index]

    def sineFit2(self, x, y, t, v):
        freq = self.find_frequency(y, x[1] - x[0])
        amp = (y.max() - y.min()) / 2.0
        guess = [amp, freq, 0, 0]  # amplitude, freq, phase,offset
        # print (guess)
        OS = y.mean()
        try:
            par, pcov = self.optimize.curve_fit(self.sineFunc, x, y - OS, guess)
        except:
            return None
        vf = self.sineFunc(t, par[0], par[1], par[2], par[3])
        diff = sum((v - vf) ** 2) / max(v)
        if diff > self.error_limit:
            guess[2] += np.pi / 2  # try an out of phase
            try:
                # print 'L1: diff = %5.0f  frset= %6.3f  fr = %6.2f  phi = %6.2f'%(diff, res,par[1]*1e6,par[2])
                par, pcov = self.optimize.curve_fit(self.sineFunc, x, y, guess)
            except:
                return None
            vf = self.sineFunc(t, par[0], par[1], par[2], par[3])
            diff = sum((v - vf) ** 2) / max(v)
            if diff > self.error_limit:
                # print 'L2: diff = %5.0f  frset= %6.3f  fr = %6.2f  phi = %6.2f'%(diff, res,par[1]*1e6,par[2])
                return None
            else:
                pass
                # print 'fixed ',par[1]*1e6
        return par, vf

    def amp_spectrum(self, v, si, nhar=8):
        # voltages, samplimg interval is seconds, number of harmonics to retain
        from numpy import fft
        NP = len(v)
        frq = fft.fftfreq(NP, si)[:NP / 2]  # take only the +ive half of the frequncy array
        amp = abs(fft.fft(v)[:NP / 2]) / NP  # and the fft result
        index = amp.argmax()  # search for the tallest peak, the fundamental
        if index == 0:  # DC component is dominating
            index = amp[4:].argmax()  # skip frequencies close to zero
        return frq[:index * nhar], amp[:index * nhar]  # restrict to 'nhar' harmonics

    def dampedSine(self, x, amp, freq, phase, offset, damp):
        """
        A damped sine wave function

        """
        return offset + amp * np.exp(-damp * x) * np.sin(abs(freq) * x + phase)

    def getGuessValues(self, xReal, yReal, func='sine'):
        if (func == 'sine' or func == 'damped sine'):
            N = len(xReal)
            offset = np.average(yReal)
            yhat = self.fftpack.rfft(yReal - offset)
            idx = (yhat ** 2).argmax()
            freqs = self.fftpack.rfftfreq(N, d=(xReal[1] - xReal[0]) / (2 * np.pi))
            frequency = freqs[idx]

            amplitude = (yReal.max() - yReal.min()) / 2.0
            phase = 0.
            if func == 'sine':
                return amplitude, frequency, phase, offset
            if func == 'damped sine':
                return amplitude, frequency, phase, offset, 0

    def arbitFit(self, xReal, yReal, func, **args):
        N = len(xReal)
        guess = args.get('guess', [])
        try:
            results, pcov = self.optimize.curve_fit(func, xReal, yReal, guess)
            pcov[0] *= 1e6
            return True, results, pcov
        except:
            return False, [], []

    def fft(self, ya, si):
        '''
        Returns positive half of the Fourier transform of the signal ya.
        Sampling interval 'si', in milliseconds
        '''
        ns = len(ya)
        if ns % 2 == 1:  # odd values of np give exceptions
            ns -= 1  # make it even
            ya = ya[:-1]
        v = np.array(ya)
        tr = abs(np.fft.fft(v)) / ns
        frq = np.fft.fftfreq(ns, si)
        x = frq.reshape(2, ns // 2)
        y = tr.reshape(2, ns // 2)
        return x[0], y[0]

    def sineFitAndDisplay(self, chan, displayObject):
        '''
        chan : an object containing a get_xaxis, and a get_yaxis method.
        displayObject : an object containing a setValue method

        Fits against a sine function, and writes to the object
        '''
        fitres = None
        fit = ''
        try:
            fitres = self.sineFit(chan.get_xaxis(), chan.get_yaxis())
            if fitres:
                amp, freq, offset, phase = fitres
                if amp > 0.05: fit = 'Voltage=%s\nFrequency=%s' % (
                    apply_si_prefix(amp, 'V'), apply_si_prefix(freq, 'Hz'))
        except Exception as e:
            fitres = None

        if not fitres or len(fit) == 0: fit = 'Voltage=%s\n' % (apply_si_prefix(np.average(chan.get_yaxis()), 'V'))
        displayObject.setValue(fit)
        if fitres:
            return fitres
        else:
            return 0, 0, 0, 0

    def rmsAndDisplay(self, data, displayObject):
        '''
        data : an array of numbers
        displayObject : an object containing a setValue method

        Fits against a sine function, and writes to the object
        '''
        rms = self.RMS(data)
        displayObject.setValue('Voltage=%s' % (apply_si_prefix(rms, 'V')))
        return rms

    def RMS(self, data):
        data = np.array(data)
        return np.sqrt(np.average(data * data))

    def butter_notch(self, lowcut, highcut, fs, order=5):
        from scipy.signal import butter
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='bandstop')
        return b, a

    def butter_notch_filter(self, data, lowcut, highcut, fs, order=5):
        from scipy.signal import lfilter
        b, a = self.butter_notch(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y


SI_PREFIXES = {k: v for k, v in zip(range(-24, 25, 3), "yzafpnµm kMGTPEZY")}
SI_PREFIXES[0] = ""


def frexp10(x: float) -> Tuple[float, int]:
    """Return the base 10 fractional coefficient and exponent of x, as pair (m, e).

    This function is analogous to math.frexp, only for base 10 instead of base 2.
    If x is 0, m and e are both 0. Else 1 <= abs(m) < 10. Note that m * 10**e is not
    guaranteed to be exactly equal to x.

    Parameters
    ----------
    x : float
        Number to be split into base 10 fractional coefficient and exponent.

    Returns
    -------
    (float, int)
        Base 10 fractional coefficient and exponent of x.

    Examples
    --------
    >>> frexp10(37)
    (3.7, 1)
    """
    if x == 0:
        coefficient, exponent = 0.0, 0
    else:
        log10x = math.log10(abs(x))
        exponent = int(math.copysign(math.floor(log10x), log10x))
        coefficient = x / 10 ** exponent

    return coefficient, exponent


def apply_si_prefix(value: float, unit: str, precision: int = 2) -> str:
    """Scale :value: and apply appropriate SI prefix to :unit:.

    Parameters
    ----------
    value : float
        Number to be scaled.
    unit : str
        Base unit of :value: (without prefix).
    precision : int, optional
        :value: will be rounded to :precision: decimal places. The default value is 2.

    Returns
    -------
    str
        "<scaled> <prefix><unit>", such that 1 <= <scaled> < 1000.

    Examples
    -------
    apply_si_prefix(0.03409, "V")
    '34.09 mV'
    """
    coefficient, exponent = frexp10(value)
    si_exponent = exponent - (exponent % 3)
    si_coefficient = coefficient * 10 ** (exponent % 3)

    if abs(si_exponent) > max(SI_PREFIXES):
        raise ValueError("Exponent out of range of available prefixes.")

    return f"{si_coefficient:.{precision}f} {SI_PREFIXES[si_exponent]}{unit}"
