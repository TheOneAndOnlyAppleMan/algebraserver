from flask import Flask, jsonify, request
from sympy import Eq, solve, Symbol
x = Symbol('x')

app = Flask(__name__)
letters = ('abcdefghijklmnopqrstuvwxyz')

def solve(string):
    try:
        eqn = ('Eq(' + string + ')')
        eqn = str(eqn.replace(' ', ''))
        eqn = str(eqn.replace('=', ','))
        try:
            for char in letters:
                firdel = ('1'+char)
                firdell = ('1*'+char)
                secdel = ('2'+char)
                secdell = ('2*'+char)
                thirdel = ('3'+char)
                thirdell = ('3*'+char)
                foudel = ('4'+char)
                foudell = ('4*'+char)
                fivdel = ('5'+char)
                fivdell = ('5*'+char)
                sixdel = ('6'+char)
                sixdell = ('6*'+char)
                sevdel = ('7'+char)
                sevdell = ('7*'+char)
                eigdel = ('8'+char)
                eigdell = ('8*'+char)
                nindel = ('9'+char)
                nindell = ('9*'+char)
                zerdel = ('0'+char)
                zerdell = ('0*'+char)
                try:
                    eqn = eqn.replace(firdel, firdell)
                    eqn = eqn.replace(secdel, secdell)
                    eqn = eqn.replace(thirdel, thirdell)
                    eqn = eqn.replace(foudel, foudell)
                    eqn = eqn.replace(fivdel, fivdell)
                    eqn = eqn.replace(sixdel, sixdell)
                    eqn = eqn.replace(sevdel, sevdell)
                    eqn = eqn.replace(eigdel, eigdell)
                    eqn = eqn.replace(nindel, nindell)
                    eqn = eqn.replace(zerdel, zerdell)
                except:
                    pass
        except:
            pass
        eqn = str(solve(eqn))
        eqn = eqn.replace(']', '')
        eqn = eqn.replace('[', '')
        eqn = eqn.replace('}', '')
        eqn = eqn.replace('{', '')
        eqn = eqn.replace(':', '=')
        return eqn
    except:
        return 'Error'

@app.route('/user', methods = ['GET'])
def index():
    Query = str(request.args['Query'])
    print(Query)
    answer = solve(Query)
    return jsonify({'answer':answer})


if __name__ == '__main__':
    app.run(debug=False)
