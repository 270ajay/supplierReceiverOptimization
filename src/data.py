import utils, logging
from utils import consts


class InputData:

    def __init__(self):

        self.supplyQtyForSupplier = utils.getSupplyInfo(consts.SUPPLY_FILE_LOCATION)
        self.capacityQtyForReceiver = utils.getCapacityInfo(consts.CAPACITY_FILE_LOCATION)
        self.costMatrix, self.supplierList, self.receiverList = utils.getCostMatrix(consts.COST_MATRIX_FILE_LOCATION)

        self.timeLimitForSolver = 30
        self.writePhaseOneLp = 1
        self.writeLp = 1


        logging.info("Stored data into objects")