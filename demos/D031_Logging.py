"""
logging日志
"""
import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='./files/d031.log',
#                     filemode='a')

log = logging.getLogger()

fh = logging.FileHandler('./files/d031.log')
# fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

log.addHandler(fh)
log.addHandler(ch)
log.setLevel(logging.DEBUG)



log.critical("critical message-------")
log.error("error message-------")
log.warning("warning message-------")
log.info("info message-------")
log.debug("debug message-------")