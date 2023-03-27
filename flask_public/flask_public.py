from functools import wraps
from flask_public.sign_compare import sign_compare
from http import HTTPStatus
from flask import Flask, request
from flask_public.interface_require_index import *
from flask_public.interface_select_index import *
from flask_public.interface_full_data import *
from SQLconnect.DBfile import *
from flask_public.interface_table_index import *

app = Flask(__name__)
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


def permission(func):
    @wraps(func)
    def permission_inner():
        if 'Authorization' not in request.headers:
            return {"message": "headers缺少Authorization", "status_code": 401}, 401
        auth = request.headers['Authorization']
        if not sign_compare(auth):
            return {"message": "签名校验失败", "status_code": HTTPStatus.FORBIDDEN}, 403
        return func()

    return permission_inner


def base_require(path, data):
    require_data = interfaceRequire[path]
    interface_info = data
    for require in require_data:
        if require not in interface_info:
            return f"请求体缺失{require}"
    return None


def make_json(obj):
    if obj.path in dataStyle:
        datas = {}
        if dataStyle[obj.path] == 'args':
            for key, value in obj.args.items():
                datas[key] = value
        elif dataStyle[obj.path] == 'form':
            for key, value in obj.form.items():
                datas[key] = value
    else:
        datas = obj.json
    return datas


def requires(func):
    @wraps(func)
    def inner():
        if request.path in listBody:
            pass
        else:
            datas = make_json(request)
            require_result = base_require(request.path, datas)
            if require_result:
                return {"message": require_result}, 400
        return func()

    return inner


def base_distinct(path, data):
    table_index = interfaceTableIndex[path]
    distinct = distinctIndex[path]
    for key, value in distinct.items():
        if value:
            select_string = ""
            cons = []
            for condition in value:
                select_string += f"{table_index}.{condition} == data['{condition}'],"
                cons.append(condition)
            if 'update' in path and key != 'id':
                select_string += f"{table_index}.id != data['id'],"
            if eval(
                    f"{table_index}.query.filter({table_index}.{key} == data['{key}'],{select_string}).first()"):
                return f"{cons}相同时，{key}不允许重复"
        else:
            path = path.split("/")
            if eval(
                    f"{table_index}.query.filter({table_index}.{key} == {''.join(path[1:])}).first()"):
                return f"id不存在"
    return None


def exist_base(path, data):
    exist_index = objectExistIndex[path]
    for key, value in exist_index.items():
        if key in data:
            value = value.split('.')
            if not eval(f"{value[0]}.query.filter({value[0]}.{value[1]} == data['{key}']).first()"):
                return f"{key}关联的{value[0]}不存在"
    return None


def data_exist_check(func):
    @wraps(func)
    def inner():
        if request.path in listBody:
            pass
        else:
            datas = make_json(request)
            exist_result = exist_base(request.path, datas)
            if exist_result:
                return {"message": exist_result}, 404
        return func()

    return inner


def distinct_check(func):
    @wraps(func)
    def inner():
        if request.path in listBody:
            pass
        else:
            distinct_result = base_distinct(request.path, request.json)
            if distinct_result:
                return {"message": distinct_result}, 400
        return func()

    return inner


def create_commit(func):
    def inner():
        full_data = interfaceFullData[request.path]
        table_index = interfaceTableIndex[request.path]
        if request.path in listBody:
            if not isinstance(request.json, list):
                return {"message": f"请求体格式错误"}, 400
            else:
                add_result = []
                for i in range(len(request.json)):
                    require_result = base_require(request.path, request.json[i])
                    distinct_result = base_distinct(request.path, request.json[i])
                    exist_result = exist_base(request.path, request.json[i])
                    if require_result:
                        add_result.append(f"第{i + 1}条数据：{require_result}\n")
                    elif distinct_result:
                        add_result.append(f"第{i + 1}条数据：{distinct_result}\n")
                    elif exist_result:
                        add_result.append(f"第{i + 1}条数据：{exist_result}\n")
                    else:
                        create_data(full_data, request.json[i], table_index)
            return {"失败结果": add_result}
        else:
            create_data(full_data, request.json, table_index)
        return func()

    return inner


def create_data(full_data, interface_info, table_index):
    add_string = ""
    for data in full_data:
        if data in interface_info:
            exec(f"{data} = interface_info['{data}']")
        else:
            exec(f"{data} = ''")
        add_string += f"{data}={data},"
    commit1 = eval(
        f"{table_index}({add_string})")
    db.session.add(commit1)
    db.session.commit()


def update_commit(func):
    @wraps(func)
    def inner():
        full_data = interfaceFullData[request.path]
        table_index = interfaceTableIndex[request.path]
        update_data(table_index, full_data, request.json)
        return func()

    return inner


def update_data(table_index, full_data, interface_info):
    pro1 = eval(f"{table_index}.query.filter({table_index}.id == interface_info['id']).first()")
    for data in full_data:
        if data in interface_info:
            exec(f"pro1.{data} = interface_info['{data}']")
    db.session.commit()


def delete_commit(func):
    @wraps(func)
    def inner():
        table_index = interfaceTableIndex[request.path]
        del_id = request.args.get('id')
        delete1 = eval(f"{table_index}.query.filter({table_index}.id == del_id).first()")
        db.session.delete(delete1)
        db.session.commit()
        return func()

    return inner


def list_commit(func):
    @wraps(func)
    def inner():
        select_string = ""
        order_by = ""
        table_index = interfaceTableIndex[request.path]
        if request.path in likeIndex:
            for obj in likeIndex[request.path]:
                if obj in request.args:
                    select_string += f"{table_index}.{obj}.like('%{request.args.get(obj)}%'),"
        if request.path in equalIndex:
            for obj in likeIndex[request.path]:
                if obj in request.args:
                    select_string += f"{table_index}.{obj} == {request.args.get(obj)},"
        if request.path in orderByIndex and request.args.get("orderBy") in orderByIndex[request.path]:
            order_by += f".order_by({table_index}.{request.args.get('orderBy')})"
        print(f"{table_index}.query.filter({select_string}){order_by}.all()")
        result = eval(f"{table_index}.query.filter({select_string}){order_by}.all()")
        res = []
        for i in result:
            mid_dic = {}
            for key, value in i.__dict__.items():
                if key == '_sa_instance_state':
                    pass
                elif isinstance(value, datetime):
                    mid_dic[key] = str(value)
                else:
                    mid_dic[key] = value
            res.append(mid_dic)
        return {"查询结果": res}

    return inner
