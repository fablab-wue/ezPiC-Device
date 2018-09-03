"""
Gadget Plugin for PAJ7620U2 Integrated Gesture Recognition Sensor
"""
from com.Globals import *

import dev.Gadget as Gadget
from dev.GadgetI2C import PluginGadgetI2C as GI2C
import dev.Variable as Variable
import dev.Machine as Machine

#######
# Globals:

EZPID = 'gdPAJ7620U2'
PTYPE = PT_SENSOR
PNAME = 'PAJ7620U2 Integrated Gesture Recognition Sensor (I2C only)'

#######

class PluginGadget(GI2C):
    _magic_init_values = [
    [0xEF, 0x00],
    [0x32, 0x29],
    [0x33, 0x01],
    [0x34, 0x00],
    [0x35, 0x01],
    [0x36, 0x00],
    [0x37, 0x07],
    [0x38, 0x17],
    [0x39, 0x06],
    [0x3A, 0x12],
    [0x3F, 0x00],
    [0x40, 0x02],
    [0x41, 0xFF],
    [0x42, 0x01],
    [0x46, 0x2D],
    [0x47, 0x0F],
    [0x48, 0x3C],
    [0x49, 0x00],
    [0x4A, 0x1E],
    [0x4B, 0x00],
    [0x4C, 0x20],
    [0x4D, 0x00],
    [0x4E, 0x1A],
    [0x4F, 0x14],
    [0x50, 0x00],
    [0x51, 0x10],
    [0x52, 0x00],
    [0x5C, 0x02],
    [0x5D, 0x00],
    [0x5E, 0x10],
    [0x5F, 0x3F],
    [0x60, 0x27],
    [0x61, 0x28],
    [0x62, 0x00],
    [0x63, 0x03],
    [0x64, 0xF7],
    [0x65, 0x03],
    [0x66, 0xD9],
    [0x67, 0x03],
    [0x68, 0x01],
    [0x69, 0xC8],
    [0x6A, 0x40],
    [0x6D, 0x04],
    [0x6E, 0x00],
    [0x6F, 0x00],
    [0x70, 0x80],
    [0x71, 0x00],
    [0x72, 0x00],
    [0x73, 0x00],
    [0x74, 0xF0],
    [0x75, 0x00],
    [0x80, 0x42],
    [0x81, 0x44],
    [0x82, 0x04],
    [0x83, 0x20],
    [0x84, 0x20],
    [0x85, 0x00],
    [0x86, 0x10],
    [0x87, 0x00],
    [0x88, 0x05],
    [0x89, 0x18],
    [0x8A, 0x10],
    [0x8B, 0x01],
    [0x8C, 0x37],
    [0x8D, 0x00],
    [0x8E, 0xF0],
    [0x8F, 0x81],
    [0x90, 0x06],
    [0x91, 0x06],
    [0x92, 0x1E],
    [0x93, 0x0D],
    [0x94, 0x0A],
    [0x95, 0x0A],
    [0x96, 0x0C],
    [0x97, 0x05],
    [0x98, 0x0A],
    [0x99, 0x41],
    [0x9A, 0x14],
    [0x9B, 0x0A],
    [0x9C, 0x3F],
    [0x9D, 0x33],
    [0x9E, 0xAE],
    [0x9F, 0xF9],
    [0xA0, 0x48],
    [0xA1, 0x13],
    [0xA2, 0x10],
    [0xA3, 0x08],
    [0xA4, 0x30],
    [0xA5, 0x19],
    [0xA6, 0x10],
    [0xA7, 0x08],
    [0xA8, 0x24],
    [0xA9, 0x04],
    [0xAA, 0x1E],
    [0xAB, 0x1E],
    [0xCC, 0x19],
    [0xCD, 0x0B],
    [0xCE, 0x13],
    [0xCF, 0x64],
    [0xD0, 0x21],
    [0xD1, 0x0F],
    [0xD2, 0x88],
    [0xE0, 0x01],
    [0xE1, 0x04],
    [0xE2, 0x41],
    [0xE3, 0xD6],
    [0xE4, 0x00],
    [0xE5, 0x0C],
    [0xE6, 0x0A],
    [0xE7, 0x00],
    [0xE8, 0x00],
    [0xE9, 0x00],
    [0xEE, 0x07],
    [0xEF, 0x01],
    [0x00, 0x1E],
    [0x01, 0x1E],
    [0x02, 0x0F],
    [0x03, 0x10],
    [0x04, 0x02],
    [0x05, 0x00],
    [0x06, 0xB0],
    [0x07, 0x04],
    [0x08, 0x0D],
    [0x09, 0x0E],
    [0x0A, 0x9C],
    [0x0B, 0x04],
    [0x0C, 0x05],
    [0x0D, 0x0F],
    [0x0E, 0x02],
    [0x0F, 0x12],
    [0x10, 0x02],
    [0x11, 0x02],
    [0x12, 0x00],
    [0x13, 0x01],
    [0x14, 0x05],
    [0x15, 0x07],
    [0x16, 0x05],
    [0x17, 0x07],
    [0x18, 0x01],
    [0x19, 0x04],
    [0x1A, 0x05],
    [0x1B, 0x0C],
    [0x1C, 0x2A],
    [0x1D, 0x01],
    [0x1E, 0x00],
    [0x21, 0x00],
    [0x22, 0x00],
    [0x23, 0x00],
    [0x25, 0x01],
    [0x26, 0x00],
    [0x27, 0x39],
    [0x28, 0x7F],
    [0x29, 0x08],
    [0x30, 0x03],
    [0x31, 0x00],
    [0x32, 0x1A],
    [0x33, 0x1A],
    [0x34, 0x07],
    [0x35, 0x07],
    [0x36, 0x01],
    [0x37, 0xFF],
    [0x38, 0x36],
    [0x39, 0x07],
    [0x3A, 0x00],
    [0x3E, 0xFF],
    [0x3F, 0x00],
    [0x40, 0x77],
    [0x41, 0x40],
    [0x42, 0x00],
    [0x43, 0x30],
    [0x44, 0xA0],
    [0x45, 0x5C],
    [0x46, 0x00],
    [0x47, 0x00],
    [0x48, 0x58],
    [0x4A, 0x1E],
    [0x4B, 0x1E],
    [0x4C, 0x00],
    [0x4D, 0x00],
    [0x4E, 0xA0],
    [0x4F, 0x80],
    [0x50, 0x00],
    [0x51, 0x00],
    [0x52, 0x00],
    [0x53, 0x00],
    [0x54, 0x00],
    [0x57, 0x80],
    [0x59, 0x10],
    [0x5A, 0x08],
    [0x5B, 0x94],
    [0x5C, 0xE8],
    [0x5D, 0x08],
    [0x5E, 0x3D],
    [0x5F, 0x99],
    [0x60, 0x45],
    [0x61, 0x40],
    [0x63, 0x2D],
    [0x64, 0x02],
    [0x65, 0x96],
    [0x66, 0x00],
    [0x67, 0x97],
    [0x68, 0x01],
    [0x69, 0xCD],
    [0x6A, 0x01],
    [0x6B, 0xB0],
    [0x6C, 0x04],
    [0x6D, 0x2C],
    [0x6E, 0x01],
    [0x6F, 0x32],
    [0x71, 0x00],
    [0x72, 0x01],
    [0x73, 0x35],
    [0x74, 0x00],
    [0x75, 0x33],
    [0x76, 0x31],
    [0x77, 0x01],
    [0x7C, 0x84],
    [0x7D, 0x03],
    [0x7E, 0x01]
    ]

    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {
            # required params
            'NAME':'PAJ7620U2',
            'ENABLE':False,
            'TIMER':0.1,
            'PORT':'1',
            'ADDR':'73',
            # instance specific params
            'Gesture':None,
            }

# -----

    def init(self):
        super().init()

# -----

    def exit(self):
        super().exit()

# -----

    def get_features(self):
        return super().get_features()

# -----

    def get_addrs(self):
        return ('73')

# -----

    def variables(self, news:dict):
        return None

# -----

    def timer(self, prepare:bool):
        gest_data = self._i2c_read_reg_buffer(0x43, 1)
        Variable.set(self.param["Gesture"], gest_data[0])


    def _device_init(self):
        """Magic init sequence cargo-culted from https://github.com/Seeed-Studio/Gesture_PAJ7620/blob/master/paj7620.cpp
        """
        # 700 us delay implied
        self._i2c.write_reg_byte(0xEF, 0) # select bank 0
        self._i2c.write_reg_byte(0xEF, 0) # two times
        b0 = self._i2c.read_reg_buffer(0, 1) # status registers?
        b1 = self._i2c.read_reg_buffer(1, 1)
#        if (b0[0] != 0x20 || b1[0] != 0x76)
#            undefined error

        for magic in self._magic_init_values:
            self._i2c.write_reg_byte(magic[0],magic[1]) # load nuclear launch codes

        self._i2c.write_reg_byte(0xEF, 1)  # select bank 1
        self._i2c.write_reg_byte(0x65, 0x12) # "near" mode, 240 fps
        self._i2c.write_reg_byte(0xEF, 0)  # select bank 0

#######