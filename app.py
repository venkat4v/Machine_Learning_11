from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import sys

app=Flask(__name__)


@app.route("/venkat",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing Exception Module")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info("We are testing logging Module")
    return "CI CD pipeline has been established by venkat."


if __name__=="__main__":
    app.run(debug=True)
