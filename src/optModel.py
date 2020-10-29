import pulp, logging, createVarsAndCts, consts, utils 



def buildAndSolveOptimizationModel(data):

    logging.info("Building and solving optimization model")
    model = pulp.LpProblem("Optimization", pulp.LpMinimize)

    flowVars = createVarsAndCts.createVarsForFlow(model, data)
    noFlowVarsForSuppliers = createVarsAndCts.createNoFlowVarsForSuppliers(model, data)
    sumOfNoFlowVars = createVarsAndCts.createPhaseOneObjective(model, noFlowVarsForSuppliers, data)

    createVarsAndCts.createCtForCapacity(model, flowVars, data)
    createVarsAndCts.createCtForSupply(model, flowVars, noFlowVarsForSuppliers, data)

    if data.writePhaseOneLp:
        model.writeLP(consts.PHASE_ONE_LP_FILE_LOCATION)

    objectiveValuePhaseOne = solveWithParameters("Phase one Optimization", model, data)
    
    createVarsAndCts.createCtForPhaseOneObjective(model, sumOfNoFlowVars, objectiveValuePhaseOne)
    createVarsAndCts.createObjective(model, flowVars, data)

    if data.writeLp:
        model.writeLP(consts.LP_FILE_LOCATION)
        logging.info("Lp file is written")

    solveWithParameters("Phase two Optimization", model, data)
    utils.printSolutionToConsole(flowVars, noFlowVarsForSuppliers)





def solveWithParameters(message, model, data):
    
    pulp.LpSolverDefault.msg = 1
    logging.info(message)
    model.solve(pulp.PULP_CBC_CMD(maxSeconds=data.timeLimitForSolver))
    logging.info("Optimization status: " + str(pulp.LpStatus[model.status]))
    objectiveValue = pulp.value(model.objective)
    logging.info("Objective value: " + str(objectiveValue))

    return objectiveValue
