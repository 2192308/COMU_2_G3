#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import Act3_Lab1_epy_block_0 as epy_block_0  # embedded python block



from gnuradio import qtgui

class Act3_Lab1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Act3_Lab1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 6.25e6
        self.fcb = fcb = 10e3
        self.fc = fc = 90.7e6
        self.GRx = GRx = 0
        self.D = D = 25

        ##################################################
        # Blocks
        ##################################################

        self._fcb_range = Range(10e3, 100e3, 1e2, 10e3, 200)
        self._fcb_win = RangeWidget(self._fcb_range, self.set_fcb, "Frecuencia de corte del filtro", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fcb_win)
        self._fc_range = Range(50e6, 250e6, 1e5, 90.7e6, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "Frecuencia de la portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self._GRx_range = Range(0, 50, 1, 0, 200)
        self._GRx_win = RangeWidget(self._GRx_range, self.set_GRx, "Ganancia del transmisor", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GRx_win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_source_0_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0_0.set_gain(GRx, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=(int(samp_rate/D)),
                taps=[],
                fractional_bw=0)
        self.qtgui_number_sink_0_3 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_3.set_update_time(0.10)
        self.qtgui_number_sink_0_3.set_title("Desviacion Estadar")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_3.set_min(i, -1)
            self.qtgui_number_sink_0_3.set_max(i, 1)
            self.qtgui_number_sink_0_3.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_3.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_3.set_label(i, labels[i])
            self.qtgui_number_sink_0_3.set_unit(i, units[i])
            self.qtgui_number_sink_0_3.set_factor(i, factor[i])

        self.qtgui_number_sink_0_3.enable_autoscale(False)
        self._qtgui_number_sink_0_3_win = sip.wrapinstance(self.qtgui_number_sink_0_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_3_win)
        self.qtgui_number_sink_0_2 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_2.set_update_time(0.10)
        self.qtgui_number_sink_0_2.set_title("Media")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_2.set_min(i, -1)
            self.qtgui_number_sink_0_2.set_max(i, 1)
            self.qtgui_number_sink_0_2.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2.set_label(i, labels[i])
            self.qtgui_number_sink_0_2.set_unit(i, units[i])
            self.qtgui_number_sink_0_2.set_factor(i, factor[i])

        self.qtgui_number_sink_0_2.enable_autoscale(False)
        self._qtgui_number_sink_0_2_win = sip.wrapinstance(self.qtgui_number_sink_0_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_2_win)
        self.qtgui_number_sink_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_1.set_title("Potencia Promedio")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_1_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("RMS")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Media Cuadratica")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
            8192, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate/D), #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            8192, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            fc, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            8192, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate/25), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            D,
            firdes.low_pass(
                1,
                samp_rate,
                fcb,
                1e4,
                window.WIN_HAMMING,
                6.76))
        self.epy_block_0 = epy_block_0.blk()
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=(samp_rate/D),
        	audio_decimation=1,
        )
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=(samp_rate/D), tau=(75e-6), fh=(-1.0))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_preemph_0, 0), (self.qtgui_freq_sink_x_0_0_0, 1))
        self.connect((self.analog_fm_preemph_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.epy_block_0, 1), (self.qtgui_number_sink_0, 0))
        self.connect((self.epy_block_0, 2), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.epy_block_0, 3), (self.qtgui_number_sink_0_1, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_number_sink_0_2, 0))
        self.connect((self.epy_block_0, 4), (self.qtgui_number_sink_0_3, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Act3_Lab1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fcb, 1e4, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, (self.samp_rate/25))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.fc, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, (self.samp_rate/self.D))
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_fcb(self):
        return self.fcb

    def set_fcb(self, fcb):
        self.fcb = fcb
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fcb, 1e4, window.WIN_HAMMING, 6.76))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.fc, self.samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(self.fc, 0)

    def get_GRx(self):
        return self.GRx

    def set_GRx(self, GRx):
        self.GRx = GRx
        self.uhd_usrp_source_0_0.set_gain(self.GRx, 0)

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, (self.samp_rate/self.D))




def main(top_block_cls=Act3_Lab1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
