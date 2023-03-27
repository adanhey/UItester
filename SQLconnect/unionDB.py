from flask_public.flask_public import *
from SQLconnect.DBfile import *


@app.route('/createUnion', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@create_commit
def create_union():
    return {"message": "新增成功"}


@app.route('/updateUnion', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@update_commit
def update_test_steps():
    return {"message": "修改成功"}


@app.route('/deleteUnion', methods=['DELETE'])
@permission
@requires
@data_exist_check
@delete_commit
def delete_test_steps():
    return {"message": "删除成功"}


@app.route('/listUnion', methods=['GET'])
@permission
@list_commit
def list_test_steps():
    return {"message": "查询成功"}


if __name__ == "__main__":
    app.run(host='10.53.3.46', port=7777)
