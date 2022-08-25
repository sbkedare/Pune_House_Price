from concurrent.futures.process import _threads_wakeups
from tokenize import Ignore
from flask import Flask, request,render_template
import pickle
import warnings
warnings.filterwarnings('ignore')
from jinja2 import Template

print('hi')

with open ('model.pkl','rb') as f:
    mod=pickle.load(f)


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('data.html')


@app.route('/get_data', methods=['POST'])
def get_data():
    f1=request.form['area_type']
    f2=request.form['site_location']
    f3=request.form['size']
    f4=request.form['total_sqft']
    op=mod.predict([[f1,f2,f3,f4]])
    print(op.round(2))

    return f'Price should be around {op.round(2)} Lakh Rupees'

# op=mod.predict([[0,52,3,1521]])
# print(op)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)


# 0.0  1.0	2.0  1056.0	 39.07
#2.0	7.0	4.0	2600.0
#1.0	53.0	3.0	1440.0
#0.0	52.0	3.0	1521.0
#area_type	site_location	size	total_sqft1	price

