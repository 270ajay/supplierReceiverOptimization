import data, optModel, utils, logging


if __name__ == '__main__':

    try:
        utils.logger(logging)
        logging.info("------------\n")

        data = data.InputData()
        optModel.buildAndSolveOptimizationModel(data)

        logging.info("\n----------------------------------------------\n")




    except Exception as e:
        logging.exception('Optimization program failed')
        logging.info("\n----------------------------------------------\n")