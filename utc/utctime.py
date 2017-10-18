# encoding: utf-8

import sys
import time
from workflow import Workflow
reload(sys)
sys.setdefaultencoding('utf8')

def main(wf):
    gmt = time.gmtime()
    utc = time.strftime("%Y-%m-%d %H:%M:%S",gmt)
    wf.add_item(title=utc,subtitle="时间获取结果",arg=utc,valid=True)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))