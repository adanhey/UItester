testStep = {
    "sq_01": {
        "title": "诉求管理按键",
        "element_path": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[3]/div/span',
        "actionDict": {"actionType": "click"}
    },
    "sq_02": {
        "title": "诉求列表按键",
        "element_path": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[3]/ul/li[1]/span',
        "actionDict": {"actionType": "click"}
    },
    "sq_03": {
        "title": "新建诉求按键",
        "element_path": '//*[@id="pane-first"]/div/div/div[2]/div[2]/div/button/i',
        "actionDict": {"actionType": "click"}
    },
    "sq_04": {
        "title": "选择诉求类型",
        "element_path": '/html/body/ul/li[1]',
        "actionDict": {"actionType": "click"},
        "screenWait": 2
    },
    "sq_05": {
        "title": "诉求新建点击客户输入框",
        "element_path": '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/'
                        'div[6]/div/div/section/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div/input',
        "actionDict": {"actionType": "click"}
    },
    "sq_06": {
        "title": "诉求新建客户输入框输入",
        "actionDict": {"actionType": "enter_word", "sendWord": "自动化"},
        "element_path": '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/'
                        'div[6]/div/div/section/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div/input'
    },
    "sq_07": {
        "title": "诉求新建选择客户",
        "element_path": '/html/body/div[3]/div[1]/div[1]/ul/li/span',
        "actionDict": {"actionType": "click"}
    },
    "sq_08": {
        "title": "诉求新建点击标签输入框",
        "scroll": 800,
        "element_path": '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/'
                        'div[6]/div/div/section/div[1]/div/div[3]/div[2]/div/form/div[1]/div/div/div/input',
        "actionDict": {"actionType": "click"}
    },
    "sq_09": {
        "title": "诉求新建选择标签",
        "element_path": '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span',
        "actionDict": {"actionType": "click"}
    },
    "sq_10": {
        "title": "诉求新建输入描述",
        "element_path": '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/'
                        'div[6]/div/div/section/div[1]/div/div[3]/div[2]/div/form/div[2]/div/div/textarea',
        "actionDict": {"actionType": "enter_word", "sendWord": "可删除的"},
    },
    "sq_11": {
        "title": "诉求新建点击确定",
        "element_path": '//*[@id="el-drawer__title"]/div[2]/button/span',
        "actionDict": {"actionType": "click"}
    },
}