from basebility import *
import pytest
from tools import *
from pic_compare.picture_compare import *
import shutil
from SQLconnect.DBfile import *


def get_environment(environment_name):
    environment = Project.query.filter(Project.name == environment_name).first()
    return environment


def get_union(unionNo):
    union = CaseUnion.query.filter(CaseUnion.unionNo == unionNo).first()
    return_dict = {
        "name": union.name,
        "unionNO": union.unionNo,
        "runStep": union.runStep
    }
    return return_dict


def runner(element_dict, sendEnvironment, screen=1, browser=None):
    if not browser:
        browser = PageObject()
    environment = get_environment(sendEnvironment)
    os.mkdir(f"./mission{browser.execTime}/{element_dict['unionNO']}")
    browser.get_url(environment)
    case_num = 1
    while True:
        if f"step{case_num}" in element_dict['runStep']:
            if element_dict['runStep'][f"step{case_num}"]["type"] == 'step':
                step_dict = CaseStep.query.filter(
                    CaseStep.stepNo == element_dict['runStep'][f"step{case_num}"]["NO"]).first()
                exec(
                    f"browser.{step_dict.actionDict['actionType']}('{step_dict.elementPath}', {step_dict.actionDict}, '{step_dict.title}')")
                if screen:
                    pic_path = browser.save_screen(element_dict['unionNO'], step_dict.title)
                    result = result_compare(element_dict['unionNO'], f"{step_dict.title}.png", pic_path)
                    if int(result) < 90:
                        browser.logger.log_event(f"{step_dict.title}.png相似度小于90：{result}")
                    else:
                        browser.logger.log_event(f"{step_dict.title}.png相似度大于90：{result}")
                        shutil.copyfile(f"{pic_path}",
                                        f"./picResult/{element_dict['unionNO']}/{step_dict.title}.png")
            else:
                step_dict = get_union(element_dict['runStep'][f"step{case_num}"]["NO"])
                runner(step_dict, sendEnvironment)
            case_num += 1
        else:
            break
    browser.close_browser()


def interface_contact(cas, mark, is_delete=None):
    now = datetime.now()
    now = str(now).replace('.', '')
    now = str(now).replace(' ', '')
    now = str(now).replace(':', '')
    now = str(now).replace('-', '')
    with open(f'{now}{mark}current.py', 'w', encoding='utf-8') as f:
        f.write(f"from test_runner import *\n")
        f.write(f"cas = {cas}\n")
        f.write(f"@pytest.mark.parametrize('unionNo,environments', cas)\n")
        f.write(f"def test_demo01(unionNo, environments):\n")
        f.write(f"    union_dict = get_union(unionNo)\n")
        f.write(f"    runner(union_dict, environments)\n")
        f.close()
    if is_delete:
        del_pic()
        del_log()
    with app.app_context():
        pytest.main([f"./{now}{mark}current.py"])
    os.remove(f'{now}{mark}current.py')


if __name__ == "__main__":
    interface_contact([("createAppeal", "汇服务")], 'sssss')
