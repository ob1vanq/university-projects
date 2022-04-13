import logging
import sys

from loguru import logger
import os

if __name__ == "__main__":
    try:
        os.system("cls")
        logger.info("Очищаю данные")
        for dir in ["data/", "log/"]:
            if not os.listdir(dir):
                break
            for filename in os.listdir(dir):
                os.remove(dir+filename)
        import methods
        logger.info("Начинаю считать потенциалы")
        import potentials
        print()
        logger.info("Начинаю считать поле")
        import field
        logger.info("Сохраняю графики")
        import show
        logger.info("Процесс заершен успешно")
        if str(input("reload[y/n] >> ")).lower() != "n":
            python = sys.executable
            os.execl(python, python, *sys.argv)
        input("...")
    except:
        print("Щось пішло не так...")
        logging.exception('')
        if str(input("reload[y/n] >> ")).lower() != "n":
            python = sys.executable
            os.execl(python, python, *sys.argv)
