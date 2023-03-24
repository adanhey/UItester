interfaceTableIndex = {
    "/createProject": "Project",
    "/updateProject": "Project",
    "/deleteProject": "Project",
    "/createTestSteps": "TestStep",
    "/updateTestSteps": "TestStep",
    "/deleteTestSteps": "TestStep"
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
}
