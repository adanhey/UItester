from flask_public.flask_public import *
from SQLconnect.DBfile import *


@app.route('/createCases', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@create_commit
def create_cases():
    return {"message": "新增成功"}


@app.route('/updateCases', methods=['POST'])
@permission
@requires
@data_exist_check
@distinct_check
@update_commit
def update_cases():
    return {"message": "修改成功"}


@app.route('/deleteCases', methods=['DELETE'])
@permission
@requires
@data_exist_check
@delete_commit
def delete_cases():
    return {"message": "删除成功"}


@app.route('/listCases', methods=['GET'])
@permission
@list_commit
def list_cases():
    return {"message": "查询成功"}


if __name__ == "__main__":
    app.run(host='10.53.3.46', port=7777)
