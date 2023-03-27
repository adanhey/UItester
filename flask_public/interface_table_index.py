interfaceTableIndex = {
    "/createProject": "Project",
    "/updateProject": "Project",
    "/deleteProject": "Project",
    "/createTestSteps": "TestStep",
    "/updateTestSteps": "TestStep",
    "/deleteTestSteps": "TestStep",
    "/listTestSteps": "TestStep",
    "/createUnion": "TestUnion"
}
listBody = {
    "/createTestSteps": 100
}
distinctIndex = {
    "/createTestSteps": {
        "stepNo": ["projectID"],
        "title": ["projectID"]
    },
    "/updateTestSteps": {
        "stepNo": ["projectID"],
        "title": ["projectID"]
    },
    "/createUnion": {
        "unionNo": ["projectID"],
        "name": ["projectID"],
    }
}

objectExistIndex = {
    "/createTestSteps": {
        "projectID": "Project.id",
    },
    "/updateTestSteps": {
        "id": "TestStep.id",
        "projectID": "Project.id",
    },
    "/deleteTestSteps": {
        "id": "TestStep.id"
    },
    "/createUnion": {
        "projectID": "Project.id",
    }
}
