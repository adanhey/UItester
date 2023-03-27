interfaceTableIndex = {
    "/createProject": "Project",
    "/updateProject": "Project",
    "/deleteProject": "Project",
    "/listProject": "Project",
    "/createCaseSteps": "CaseStep",
    "/updateCaseSteps": "CaseStep",
    "/deleteCaseSteps": "CaseStep",
    "/listCaseSteps": "CaseStep",
    "/createUnion": "CaseUnion",
    "/updateUnion": "CaseUnion",
    "/deleteUnion": "CaseUnion",
    "/listUnion": "CaseUnion",
    "/createCases": "CasesObj",
    "/updateCases": "CasesObj",
    "/deleteCases": "CasesObj",
    "/listCases": "CasesObj",
}
listBody = {
    "/createCaseSteps": 100
}
distinctIndex = {
    "/createProject": {"name": []},
    "/updateProject": {"name": []},
    "/createCaseSteps": {
        "stepNo": ["projectID"],
        "title": ["projectID"]
    },
    "/updateCaseSteps": {
        "stepNo": ["projectID"],
        "title": ["projectID"]
    },
    "/createUnion": {
        "unionNo": ["projectID"],
        "name": ["projectID"],
    },
    "/updateUnion": {
        "unionNo": ["projectID"],
        "name": ["projectID"],
    },
    "/createCases": {
        "casesNo": ["projectID"],
        "name": ["projectID"],
    },
    "/updateCases": {
        "casesNo": ["projectID"],
        "name": ["projectID"],
    }
}

objectExistIndex = {
    "/deleteProject": {
        "id": "Project.id"
    },
    "/createCaseSteps": {
        "projectID": "Project.id",
    },
    "/updateCaseSteps": {
        "id": "CaseStep.id",
        "projectID": "Project.id",
    },
    "/deleteCaseSteps": {
        "id": "CaseStep.id"
    },
    "/createUnion": {
        "projectID": "Project.id",
    },
    "/updateUnion": {
        "id": "CaseUnion.id",
        "projectID": "Project.id",
    },
    "/deleteUnion": {
        "id": "CaseUnion.id"
    },
    "/createCases": {
        "projectID": "Project.id",
    },
    "/updateCases": {
        "id": "CasesObj.id",
        "projectID": "Project.id",
    },
    "/deleteCases": {
        "id": "CasesObj.id"
    },
}
