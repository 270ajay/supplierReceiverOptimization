import pulp, logging
from utils import consts


def createVarsForFlow(model, data):
    flowVars = {}

    for supplier in data.supplierList:
        for receiver in data.receiverList:

            varNameInLpFile = consts.FLOW_VAR + consts.SEPARATOR + str(supplier) + consts.SEPARATOR + str(receiver)
            variable = pulp.LpVariable(varNameInLpFile, lowBound=0, cat=pulp.LpContinuous)
            flowVars[(supplier, receiver)] = variable
            model.addVariable(variable)

    logging.info("Created flow variables")
    return flowVars



def createNoFlowVarsForSuppliers(model, data):
    noFlowVars = {}

    for supplier in data.supplierList:
        varNameInLpFile = consts.NO_FLOW_VAR + consts.SEPARATOR + str(supplier)
        variable = pulp.LpVariable(varNameInLpFile, lowBound=0, cat=pulp.LpContinuous)
        noFlowVars[supplier] = variable
        model.addVariable(variable)

    logging.info("Created noFlow variables")
    return noFlowVars



###############################################################


def createPhaseOneObjective(model, noFlowVarsForSuppliers, data):

    coeffVarList = []
    for supplier in (data.supplierList):
        coeffVarList.append(noFlowVarsForSuppliers[supplier])

    sumOfNoFlowVars = pulp.lpSum(coeffVarList)
    model.setObjective(sumOfNoFlowVars)
    logging.info("Phase One Objective is set")
    return sumOfNoFlowVars





def createObjective(model, flowVars, data):

    costMatrix = data.costMatrix

    coeffVarList = []
    for supplier in (data.supplierList):
        for receiver in (data.receiverList):

            coeffVarList.append(costMatrix[supplier][receiver] * flowVars[(supplier, receiver)])

    model.setObjective(pulp.lpSum(coeffVarList))
    logging.info("Original objective is set")





###############################################################


def createCtForCapacity(model, flowVars, data):

    coeffVarList = []
    for receiver in data.receiverList:
        for supplier in data.supplierList:

            coeffVarList.append(flowVars[(supplier, receiver)])

        model += pulp.lpSum(coeffVarList) <= data.capacityQtyForReceiver[receiver], consts.CAPACITY_CT + consts.SEPARATOR + str(receiver)
        coeffVarList.clear()

    logging.info("Created capacity constraint for receivers")




def createCtForSupply(model, flowVars, noFlowVarsForSuppliers, data):

    coeffVarList = []
    for supplier in data.supplierList:
        for receiver in data.receiverList:

            coeffVarList.append(flowVars[(supplier, receiver)])

        model += pulp.lpSum(coeffVarList) + noFlowVarsForSuppliers[supplier] == data.supplyQtyForSupplier[supplier], consts.SUPPLY_CT + consts.SEPARATOR + str(supplier)
        coeffVarList.clear()

    logging.info("Created supply constraint for suppliers")




def createCtForPhaseOneObjective(model, sumOfNoFlowVars, objectiveValuePhaseOne):
    model += sumOfNoFlowVars <= objectiveValuePhaseOne, consts.PHASE_ONE_OBJECTIVE_CT
    logging.info("Created phase one objective as constraint")