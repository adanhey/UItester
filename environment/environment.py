environmentIndex = {
    "汇服务": {
        "url": "https://huiservertest4.iotdataserver.net/huiservice/login",
        "account": {"sendWord": "sysadmin"},
        "password": {"sendWord": "hc300124"},
        "accountXpath": '//*[@id="huiservice"]/div/div[2]/div/div/form/div[1]/div/div/input',
        "passwordXpath": '//*[@id="huiservice"]/div/div[2]/div/div/form/div[2]/div/div/input',
        "loginButton": '//*[@id="huiservice"]/div/div[2]/div/div/form/button/span/span',
    },
    "金阳": {
        "url": "https://jinyang.dataserver.cn/sys/#/login",
        "account": {"sendWord": "superadmin"},
        "password": {"sendWord": "hc300124"},
        "accountXpath": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div[1]/input',
        "passwordXpath": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input',
        "loginButton": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[3]/div/button',
    }
}

environmentList = [
    {
        "url": "https://jinyang.dataserver.cn/sys/#/login",
        "account": "superadmin",
        "password": "hc300124",
        "accountXpath": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div[1]/input',
        "passwordXpath": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input',
        "loginButton": '//*[@id="app"]/div/div[2]/div[2]/div/form/div[3]/div/button',
        "checklist": [
            {
                "title": "智能派单-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/div/span',
            },
            {
                "title": "工单管理-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[1]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "经线管理-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[2]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "工艺卡管理-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[3]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "智能派单-拉丝",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[3]/div/span',
            },
            {
                "title": "工单管理-拉丝",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[3]/ul/li[1]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "经线管理-拉丝",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[3]/ul/li[2]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "工艺卡管理-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[3]/ul/li[3]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[1]/div/div[1]/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "报表管理",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/div/span',
            },
            {
                "title": "产量报表-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[1]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div/div/div/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "产量报表统计-漆包",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[2]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div/div/div/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "产量报表-拉丝",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[3]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div/div/div/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "产量报表统计-拉丝",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[4]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div/div/div/div[3]/div[3]',
                    }
                ]
            },
            {
                "title": "电子看板",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[11]/div/span',
            },
            {
                "title": "漆包机机台看板",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[11]/ul/li[1]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[2]/div[1]/div[3]',
                    }
                ]
            },
            {
                "title": "拉丝机机台看板",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[11]/ul/li[2]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[2]/div[1]/div[3]',
                    }
                ]
            },
            {
                "title": "漆包机生产看板",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[11]/ul/li[3]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[2]/div[1]/div[3]',
                    }
                ]
            },
            {
                "title": "拉丝机生产看板",
                "click": '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[11]/ul/li[4]/span',
                "becheck": [
                    {
                        'path': '//*[@id="avue-view"]/div/div[2]/div[1]/div[3]',
                    }
                ]
            },
        ]
    },
    {
        "url": "https://xingguan.dataserver.cn/itas-app/#/",
        "account": "sysadmin",
        "password": "277247",
        "accountxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[2]/div/div/input",
        "passwordxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[3]/div/div[1]/input",
        "loginbutx": "/html/body/div/div[1]/div[2]/div/div/form/div[4]/span",
        "checklist": [
            {
                "beflame": ['//*[@id="J_Iframe"]', '/html/body/iframe'],
                "click1": '//*[@id="dashboard-container"]/div/div/div[7]/div/div/div['
                          '3]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]',
            }
        ]
    },
    {
        "url": "https://mso.dataserver.cn/ims#/fullLogin?redirect=%2F",
        "account": "sysadmin",
        "password": "hc300124",
        "accountxpath": "/html/body/div[1]/div/div[2]/div/div/div/form/div[1]/div/div[1]/input",
        "passwordxpath": "/html/body/div[1]/div/div[2]/div/div/div/form/div[2]/div/div[1]/input",
        "loginbutx": "/html/body/div[1]/div/div[2]/div/div/div/form/div[4]/div/button",
        "loginextend": "/html/body/div[1]/div/div[2]/div/div/div/form/div[3]/div/div/div/input",
        "loginextend2": "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span",
        "checklist": [
            {
                "title": "菜单",
                "click": '/html/body/div/div[1]/div[2]',
                "becheck": [
                    {
                        'path': '/html/body/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span[2]',
                    }
                ]
            },
            {
                "title": "生产看板",
                "click": '/html/body/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/span[2]',
                "becheck": [
                    {
                        'path': '//*[@id="productionDashbord"]/div[3]/div/div[1]',
                    }
                ]
            },
            {
                "title": "机台看板",
                "click": '/html/body/div/div[2]/div[2]/ul/li[2]',
                "aflame": ['/html/body/div/div[3]/div/iframe'],
                "acheck": [
                    {
                        "path": '/html/body/div[3]/canvas'
                    }
                ],
            },
            {
                "behandle": 0,
                "title": "报表管理",
                "click": '/html/body/div/div[2]/div[1]/div[2]/div/ul/li[3]',
                "acheck": [
                    {
                        "path": '/html/body/div/div[2]/div[2]/ul/li'
                    }
                ],
            },
            {
                "title": "生产报表",
                "click": '/html/body/div/div[1]/div[1]/div/div[1]/div[1]/span[2]',
                "aflame": ['/html/body/div/div[3]/div/div[3]/iframe'],
                "acheck": [
                    {
                        "path": '//*[@id="dc_294"]/div'
                    }
                ],
            },
        ]
    },
    {
        "url": "https://zhongxiaoyun-zhusu.dataserver.cn/itas-app/#/",
        "account": "15086858301",
        "password": "zxy119119",
        "accountxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[2]/div/div/input",
        "passwordxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[3]/div/div[1]/input",
        "loginbutx": "/html/body/div/div[1]/div[2]/div/div/form/div[4]/span",
        "checklist": [
            {
                "title": "实时监控",
                "click": '/html/body/div/div[2]/div[2]/div/div/div[3]/ul/li[1]/a/div[1]/span/i[2]',
                "becheck": [
                    {
                        'path': '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[3]/a/div[1]/span/i',
                    }
                ]
            },
            {
                "title": "聚合监控",
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[3]/a/div[1]/span/i',
                "becheck": [
                    {
                        'path': '//*[@id="J_GraphViewBox"]',
                    }
                ],
            },
            {
                "title": "效能看板",
                "click": '//*[@id="J_GraphViewBox"]/div/ul/li[1]/div/img',
                "becheck": [
                    {
                        "path": '/html/body/div[4]/iframe'
                    }
                ],
                "acheck": [
                    {
                        "path": '//*[@id="myHistogram2"]/div[2]'
                    }
                ],
                "ahandle": 1,
                "aflame": ['/html/body/div[4]/iframe']
            },
            {
                "behandle": 0,
                "title": "车间看板",
                "click": '//*[@id="J_GraphViewBox"]/div/ul/li[2]/div/img',
                "becheck": [
                    {
                        "path": '/html/body/div[4]/iframe'
                    }
                ],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]'
                    }
                ],
                "aflame": ['/html/body/div[4]/iframe'],
                "ahandle": 2,
            },
            {
                "behandle": 0,
                "title": "总体看板",
                "click": '//*[@id="J_GraphViewBox"]/div/ul/li[3]/div/img',
                "becheck": [
                    {
                        "path": '/html/body/div[4]/iframe'
                    }
                ],
                "acheck": [
                    {
                        "path": '//*[@id="month_utilization_line"]/div[1]'
                    }
                ],
                "aflame": ['/html/body/div[4]/iframe'],
                "ahandle": 3,
            },
        ]

    },
    {
        "url": "https://flora.dataserver.cn/itas-app/#/",
        "account": "lby",
        "password": "hc300124",
        "accountxpath": '//*[@id="pane-first"]/form/div[1]/div/div/input',
        "passwordxpath": '//*[@id="pane-first"]/form/div[2]/div/div[1]/input',
        "loginbutx": '//*[@id="pane-first"]/form/div[4]/span',
        "checklist": [
            {
                "title": "首页看板",
                "click": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/span',
                "acheck": [
                    {
                        'path': '//*[@id="device_map"]/div[1]',
                    }
                ],
                "aflame": ['//*[@id="uwebApp"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/iframe']
            },
            {
                "beflame": ['default'],
                "title": "关键数据配置",
                "click": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[12]/span',
                "acheck": [
                    {
                        'path': '//*[@id="runtianzhi"]/div/basic-container/div/div[2]/div/form/div/div[3]/table/tbody/tr[10]/td[5]/div/span',
                    }
                ],
            },
            {
                "title": "常量配置",
                "click": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[13]/span',
                "acheck": [
                    {
                        'path': '//*[@id="runtianzhi"]/div/div/div/div[2]/div/form/div/div[3]/table/tbody/tr[10]/td[5]/div/span',
                    }
                ],
            },
        ]
    },
    {
        "url": "https://zxxc.dataserver.cn/itas-app/#/",
        "account": "zxxc",
        "password": "zxxc123456",
        "accountxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[2]/div/div/input",
        "passwordxpath": "/html/body/div/div[1]/div[2]/div/div/form/div[3]/div/div[1]/input",
        "loginbutx": "/html/body/div/div[1]/div[2]/div/div/form/div[4]/span",
        "checklist": [
            {
                "title": "实时监控",
                "click": '/html/body/div/div[2]/div[2]/div/div/div[3]/ul/li[1]/a/div[1]/span/i[2]',
                "becheck": [
                    {
                        'path': '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[3]/a/div[1]/span/i',
                    }
                ]
            },
            {
                "title": "聚合监控",
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[3]/a/div[1]/span/i',
                "becheck": [
                    {
                        'path': '//*[@id="J_GraphViewBox"]',
                    }
                ],
            },
            {
                "title": "大屏看板",
                "click": '//*[@id="J_GraphViewBox"]/div/ul/li/div/img',
                "becheck": [
                    {
                        "path": '/html/body/div[4]/iframe'
                    }
                ],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]'
                    }
                ],
                "ahandle": 1,
                "aflame": ['/html/body/div[4]/iframe']
            },
            {
                "title": '中线报表workstation',
                "behandle": 0,
                "click": '/html/body/div/div[2]/div[2]/div/div/div[1]/a/div[1]/span/i[2]',
            },
            {
                "title": '中线报表',
                "click": '/html/body/div/div[2]/div[2]/div/div/div[3]/ul/li[7]/a/div[1]/span/i[2]',
            },
            {
                "title": '计件报表',
                "aflame": ['//*[@id="J_Iframe"]'],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div[2]/div/div[3]/table/tbody/tr[50]/td[5]/div'
                    }
                ],
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[1]/a/div[1]/span/i',
                "screenwait": 3
            },
            {
                "beflame": ['default'],
                "title": '超速报表',
                "aflame": ['//*[@id="J_Iframe"]'],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div[2]/div/div[3]/table/tbody/tr[50]/td[4]/div'
                    }
                ],
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[2]/a/div[1]/span/i',
                "screenwait": 3
            },
            {
                "beflame": ['default'],
                "title": '断线报表',
                "aflame": ['//*[@id="J_Iframe"]'],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div[2]/div/div[3]/table/tbody/tr[50]/td[6]/div'
                    }
                ],
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[3]/a/div[1]/span/i',
                "screenwait": 3
            },
            {
                "beflame": ['default'],
                "title": '能耗报表',
                "aflame": ['//*[@id="J_Iframe"]'],
                "acheck": [
                    {
                        "path": '//*[@id="app"]/div/div[2]/div/div[3]/table/tbody/tr[50]/td[4]/div'
                    }
                ],
                "click": '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/ul/li[4]/a/div[1]/span/i',
                "screenwait": 3
            },
        ]
    },
    {
        "url": "https://dgxysy.dataserver.cn/base/login/index?type=1#/sysadmin",
        "account": "sysadmin",
        "password": "011013",
        "accountxpath": '//*[@id="pane-first"]/form/div[1]/div/div/input',
        "passwordxpath": '//*[@id="pane-first"]/form/div[2]/div/div[1]/input',
        "loginbutx": '//*[@id="pane-first"]/form/div[4]/span',
        "checklist": [
            {
                "title": "鸿翔报表",
                "click": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/span',
                "becheck": [
                    {
                        'path': '//*[@id="hongxiang"]/div/div[2]/div[1]/div[3]/table',
                    }
                ]
            },
            {
                "title": "员工信息管理",
                "click": '//*[@id="uwebApp"]/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[2]/span',
                "becheck": [
                    {
                        'path': '//*[@id="hongxiang"]/div/div[2]/div/div[3]/table',
                    }
                ]
            },
        ]
    }
]
