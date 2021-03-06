from fastapi import HTTPException

invalidJson = HTTPException(status_code=400, detail="Invalid JSON - No valid json provided.")
missingCallbackUrl = HTTPException(status_code=400, detail="callbackUrl missing")
missingSubmissions = HTTPException(status_code=400, detail="Submissions missing")
missingTaskType = HTTPException(status_code=400, detail="taskType missing")
invalidTaskType = HTTPException(status_code=400, detail="Invalid taskType")
missingChunkSize = HTTPException(status_code=400, detail="chunkSize missing")
invalidChunkSize = HTTPException(status_code=400, detail="Invalid chunkSize - Has to be at least 2")
missingJobId = HTTPException(status_code=400, detail="jobId missing")
invalidJobId = HTTPException(status_code=400, detail="Invalid jobId")
missingResultType = HTTPException(status_code=400, detail="resultType missing")
invalidResultType = HTTPException(status_code=400, detail="Invalid resultType")
missingTextBlocks = HTTPException(status_code=400, detail="textBlocks missing")
missingEmbeddings = HTTPException(status_code=400, detail="embeddings missing")
missingTaskId = HTTPException(status_code=400, detail="taskId missing")
invalidResults = HTTPException(status_code=400, detail="Invalid results - Provided results do not seem to match job/task with provided jobId/taskId")
noUpdateNeeded = HTTPException(status_code=400, detail="Provided jobId/taskId needs no (such) update")
missingClusters = HTTPException(status_code=400, detail="clusters missing")
missingDistanceMatrix = HTTPException(status_code=400, detail="distanceMatrix missing")
missingClusterTree = HTTPException(status_code=400, detail="clusterTree missing")
invalidAuthorization = HTTPException(status_code=401, detail="Invalid Authorization Header")
taskTypeError = HTTPException(status_code=500, detail="Error with taskType")
