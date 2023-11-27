#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd3in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime
#import pytz

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd3in7 Demo")
    
    epd = epd3in7.EPD()
    logging.info("init and Clear")
    epd.init(0)
    epd.Clear(0xFF, 0)

    current_datetime = datetime.now()
    weekday = current_datetime.weekday()
    weekday_names = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    weekday_name = weekday_names[weekday]
    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('L', (epd.height, epd.width), 0xFF)  # 0xFF: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), current_datetime, font = font36, fill = 0)
    draw.text((340, 248), '@:o_mesut_', font = font24, fill = 0)
    draw.text((150, 60), '2023-11-27', font = font36, fill = 0)

    draw.line((0, 40, 480, 40), fill = 0)
    draw.line((0, 240, 480, 240), fill = 0)



    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(5)
    


    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in7.epdconfig.module_exit()
    exit()
