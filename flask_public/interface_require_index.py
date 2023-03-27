interfaceRequire = {
    "/createProject": ['url', 'name', 'account', 'password', 'accountXpath', 'passwordXpath', "loginButton"],
    "/updateProject": ['id'],
    "/importModel": ['pro_id', 'name'],
    "/createTestSteps": ['projectID', 'title', 'stepNo'],
    "/updatePublicCase": ['id', 'project_id', 'name', 'jsonData'],
    "/updateTestSteps": ['id'],
    "/deleteTestSteps": ['id'],
    "/createUnion": ['unionNo', 'name', 'projectID']
}
dataStyle = {
    "/deleteTestSteps": "args"
}
