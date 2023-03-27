from flask_public.flask_public import *
from SQLconnect.DBfile import *


@app.route('/createProject', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@create_commit
def create_project():
    return {"message": "添加成功"}


@app.route('/updateProject', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@update_commit
def update_project():
    return {"message": "修改成功"}


@app.route('/deleteProject', methods=['DELETE'])
@permission
@requires
@data_exist_check
@delete_commit
def delete_project():
    return {"message": "删除成功"}


@app.route('/listProject', methods=['GET'])
@permission
@list_commit
def list_project():
    return {"message": "查询成功"}


if __name__ == "__main__":
    app.run(host='10.53.3.46', port=7777)
