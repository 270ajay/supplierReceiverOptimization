import csv, logging, consts


def getCostMatrix(costMatrixFileName):
    ''' In this function, we create a dictionary of dictionary containing cost matrix.'''

    with open(costMatrixFileName) as csvfile:
        data = list(csv.reader(csvfile))

    supplierList = []
    for i in range(1, len(data)):
        supplierList.append(data[i][0])

    receiverList = []
    for i in range(1, len(data[0])):
        receiverList.append(data[0][i])

    costMatrix = {}
    counter = 1
    for supplier in supplierList:
        costMatrix[supplier] = {}
        for j in range(1, len(data[0])):
            costMatrix[supplier][receiverList[j - 1]] = int(data[counter][j])
        counter += 1

    return costMatrix, supplierList, receiverList




def getCapacityInfo(capacityFileName):
    capacityQtyForReceiver = {}

    with open(capacityFileName) as csvfile:
        data = list(csv.reader(csvfile))

    for i in range(len(data)):
        capacityQtyForReceiver[data[i][0]] = float(data[i][1])

    return capacityQtyForReceiver




def getSupplyInfo(supplyFileName):
    supplyQtyForSupplier = {}

    with open(supplyFileName) as csvfile:
        data = list(csv.reader(csvfile))

    for i in range(len(data)):
        supplyQtyForSupplier[data[i][0]] = float(data[i][1])

    return supplyQtyForSupplier



def printSolutionToConsole(flowVars, noFlowVarsForSuppliers):

    for flowVar in flowVars.values():
        if flowVar.varValue > 0.0:
            logging.info(str(flowVar.name) + " = " + str(flowVar.varValue))

    logging.info("````````````````")

    for noFlowVar in noFlowVarsForSuppliers.values():
        if noFlowVar.varValue > 0.0:
            logging.info(str(noFlowVar.name) + " = " + str(noFlowVar.varValue))




def logger(logging):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s %(process)d %(message)s',
                        #datefmt='%d/%m/%Y %I:%M:%S %p',
                        filename=consts.LOG_FILE_LOCATION, filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s %(process)d %(message)s'))
    logging.getLogger().addHandler(console)