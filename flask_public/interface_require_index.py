interfaceRequire = {
    "/createProject": ['url', 'name', 'account', 'password', 'accountXpath', 'passwordXpath', "loginButton"],
    "/updateProject": ['id'],
    "/deleteProject": ['id'],
    "/importModel": ['pro_id', 'name'],
    "/createCaseSteps": ['projectID', 'title', 'stepNo'],
    "/updateCaseSteps": ['id'],
    "/deleteCaseSteps": ['id'],
    "/createUnion": ['unionNo', 'name', 'projectID'],
    "/updateUnion": ['id'],
    "/deleteUnion": ['id'],
    "/createCases": ['casesNo', 'name', 'projectID'],
    "/updateCases": ['id'],
    "/deleteCases": ['id'],
}
dataStyle = {
    "/deleteCaseSteps": "args",
    "/deleteProject": "args",
    "/deleteUnion": "args",
    "/deleteCases": "args",
}
