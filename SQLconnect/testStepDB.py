from flask_public.flask_public import *
from SQLconnect.DBfile import *


@app.route('/createTestSteps', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@create_commit
def create_test_steps():
    return {"message": "新增成功"}


@app.route('/updateTestSteps', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@update_commit
def update_test_steps():
    return {"message": "修改成功"}


@app.route('/deleteTestSteps', methods=['DELETE'])
@permission
@requires
@data_exist_check
@delete_commit
def delete_test_steps():
    return {"message": "删除成功"}


@app.route('/listTestSteps', methods=['GET'])
@permission

def list_test_steps():
#     if not request.args.get('project_id'):
#         return {"message": f"缺失项目id"}, 400
#     select_pam = ['name', 'project_id']
#     select_str = ""
#     for pam in select_pam:
#         exec(f"{pam} = request.args.get('{pam}')")
#         if eval(f"{pam}"):
#             select_str += f"PublicCase.{pam} == {pam}"
#     result = eval(f"PublicCase.query.filter({select_str}).all()")
#     res = []
#     for i in result:
#         mid_dic = {}
#         for key, value in i.__dict__.items():
#             if key == '_sa_instance_state':
#                 pass
#             elif isinstance(value, datetime):
#                 mid_dic[key] = str(value)
#             else:
#                 mid_dic[key] = value
#         res.append(mid_dic)
#     return {"查询结果": res}


if __name__ == "__main__":
    app.run(host='10.53.3.46', port=7777)
