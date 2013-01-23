#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we connect a signal
of a QtGui.QSlider to a slot 
of a QtGui.QLCDNumber. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def make_spin (self, min_val=0, max_val=99, label="", changed_callback = None ):

        spin =  QtGui.QSpinBox(self)
        spin.setMinimum (min_val)
        spin.setMaximum (max_val)
        spin.setPrefix(label)
        spin.setAlignment(QtCore.Qt.AlignRight)

        spin.valueChanged.connect(changed_callback)

        return spin

    def __init__(self):
        super(Example, self).__init__()
        self.force_p_ = 0
        self.force_i_ = 0
        self.force_d_ = 0

        self.initUI()

    def force_spin_changed(self, value):
        self.force_p_ = self.force_p_spin_.value()
        self.force_i_ = self.force_i_spin_.value()
        self.force_d_ = self.force_d_spin_.value()
        self.force_imax_ = self.force_i_spin_.value()
        self.force_idecay_ = self.force_d_spin_.value()
        #call set pid service

    def stiffness_changed(self, value):
        self.stiffness_slider_.setValue(value)
        self.stiffness_spin_.setValue(value)

        return
    def position_target_changed(self, value):
        self.position_slider_.setValue(value)
        self.position_spin_.setValue(value)
        
        return

    def make_force_box_group(self):
        force_box_group = QtGui.QGroupBox("Force PID")
        spin_vbox = QtGui.QVBoxLayout()

        force_p      =  self.make_spin(-255,255, "p = ", self.force_spin_changed)
        force_i      =  self.make_spin(-255,255, "i = ", self.force_spin_changed)
        force_d      =  self.make_spin(-255,255, "d = ", self.force_spin_changed)
        force_imax   =  self.make_spin(-255,255, "i max = ", self.force_spin_changed)
        force_idecay =  self.make_spin(-255,255, "i decay = ", self.force_spin_changed)

        self.force_p_spin_ = force_p
        self.force_i_spin_ = force_i
        self.force_d_spin_ = force_d
        self.force_imax_spin_ = force_imax
        self.force_idecay_spin_ = force_idecay

        spin_vbox.addWidget(force_p)
        spin_vbox.addWidget(force_i)
        spin_vbox.addWidget(force_d)
        spin_vbox.addWidget(force_imax)
        spin_vbox.addWidget(force_idecay)

        force_box_group.setLayout(spin_vbox)

        return force_box_group

    def make_stiffness_box_group(self) :
        stiffness_group_box = QtGui.QGroupBox("Stiffness")
        stiffness_vbox = QtGui.QVBoxLayout()

        stiffness_spin = self.make_spin(0,100, "k = ", self.stiffness_changed)
        stiffness_slider = QtGui.QSlider (QtCore.Qt.Horizontal, self)


        stiffness_slider.valueChanged.connect(self.stiffness_changed)


        self.stiffness_spin_ = stiffness_spin;
        self.stiffness_slider_ = stiffness_slider;

        stiffness_vbox.addWidget(stiffness_spin)
        stiffness_vbox.addWidget(stiffness_slider)
        stiffness_group_box.setLayout(stiffness_vbox)
        return stiffness_group_box
        
    def make_position_box_group(self):
        position_group_box = QtGui.QGroupBox("Position")
        position_vbox = QtGui.QVBoxLayout()
        position_spin = self.make_spin(-128,128, "Target = ", self.position_target_changed)
        position_slider = QtGui.QSlider (QtCore.Qt.Horizontal, self)
        position_slider.setMaximum(128)
        position_slider.setMinimum(-128)
        position_slider.valueChanged.connect(self.position_target_changed)

        self.position_spin_ = position_spin;
        self.position_slider_ = position_slider;

        position_vbox.addWidget(position_spin)
        position_vbox.addWidget(position_slider)
        position_group_box.setLayout(position_vbox)
        return position_group_box


    def initUI(self):

        force_box_group     = self.make_force_box_group()
        stiffness_group_box = self.make_stiffness_box_group()
        position_group_box  = self.make_position_box_group()

       
        control_vbox = QtGui.QVBoxLayout()
        control_vbox.addWidget(stiffness_group_box)

        control_vbox.addWidget(position_group_box)
        control_vbox.addStretch(1)

        main_hbox = QtGui.QHBoxLayout()
        main_hbox.addWidget(force_box_group)
        main_hbox.addItem(control_vbox)
 #       main_hbox.addWidget(control_box_group)
        self.setLayout(main_hbox)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Test Gui')


        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
