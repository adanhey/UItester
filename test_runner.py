from basebility import *
import pytest
from testUnion.testUnion import testUnion
from testStep.testStep import testStep
from environment.environment import environmentIndex
from tools import *
from pic_compare.picture_compare import *
import shutil

currentEnvironment = environmentIndex['汇服务']


def runner(element_dict, sendEnvironment=currentEnvironment, screen=1):
    t = PageObject()
    os.mkdir(f"./mission{t.execTime}/{element_dict['unionNO']}")
    t.get_url(sendEnvironment['url'], sendEnvironment)
    case_num = 1
    while True:
        if f"step{case_num}" in element_dict['runStep']:
            if element_dict['runStep'][f"step{case_num}"]["type"] == 'step':
                step_dict = testStep[element_dict['runStep'][f"step{case_num}"]["NO"]]
                eval(
                    f"t.{step_dict['actionDict']['actionType']}('{step_dict['element_path']}', "
                    f"{step_dict['actionDict']}, '{step_dict['title']}')")
                if screen:
                    pic_path = t.save_screen(element_dict['unionNO'], step_dict['title'])
                    result = result_compare(element_dict['unionNO'], f"{step_dict['title']}.png", pic_path)
                    if int(result) < 90:
                        t.logger.log_event(f"{step_dict['title']}.png相似度小于90：{result}")
                    else:
                        t.logger.log_event(f"{step_dict['title']}.png相似度大于90：{result}")
                        shutil.copyfile(f"{pic_path}",
                                        f"./picResult/{element_dict['unionNO']}/{step_dict['title']}.png")
            else:
                step_dict = testUnion(element_dict['runStep'][f"step{case_num}"]["NO"], screen=None)
                runner(step_dict)
            case_num += 1
        else:
            break
    t.close_browser()


@pytest.mark.parametrize('dict1', testUnion)
class TestDemo:
    def test_demo01(self, dict1):
        runner(dict1)


if __name__ == "__main__":
    del_pic()
    del_log()
    pytest.main()
