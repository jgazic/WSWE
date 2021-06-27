# pylint: disable=no-member
from flask import Flask
from flask import json
from flask import request
<<<<<<< HEAD
from flask import jsonify
=======
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse, fields, marshal_with
import sqlite3
import random
import time
from datetime import date
import string

<<<<<<< HEAD

=======
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins": "*"
    }
})
api = Api(app)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    lunch_id=''.join(random.choice(chars) for _ in range(10))
    link = "http://localhost/Projekt_Seminar/Frontend/wswe.html?id=" + lunch_id
    return link


def izberiRandom(rez):
    
    if len(rez)==0:
        return
    
    random.seed(round(time.time()))
    x = random.randint(0,len(rez)-1)

    rez = rez[x]

    return rez


def create_table(table_name):
    if table_name == 'suggestions':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE suggestions(
                        user text,
                        suggestion text,
                        id text,
                        timestamp TIMESTAMP
                        )""")
        conn.commit()
        conn.close
    
    if table_name == 'decisions':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE decisions(
                        user text,
                        decision text,
                        id text,
                        timestamp TIMESTAMP
                        )""")
        conn.commit()
        conn.close



def add_suggestion(name,suggestion,id):
        
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO suggestions VALUES ('{name}','{suggestion}', '{id}', date('now'))")
    conn.commit()
    conn.close
    print('answer added')

def add_decision(name,decision,id):
        
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO decisions VALUES ('{name}','{decision}', '{id}', date('now'))")
    conn.commit()
    conn.close
    #print('answer added')

def remove_id_data(table_name,id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    with conn:            
        c.execute(f"DELETE FROM {table_name} WHERE id='{id}'")    


def make_decision(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM suggestions WHERE id='{id}'")
    all = c.fetchall()
    #print(all)
    conn.commit()
    conn.close    
    
    if not all:
        response = None

    else: 
        all = izberiRandom(all)   
        response = [{'name': f'{all[0]}','suggestion': f'{all[1]}', 'id': f'{all[2]}', 'timestamp': f'{all[3]}' }]
    
    return response
     
def check_if_duplicate(name,suggestion,id):
    today = date.today()            
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM suggestions WHERE user='{name}' AND suggestion = '{suggestion}' AND id = '{id}' AND timestamp = '{today}' ")
    duplicate = c.fetchall()
    if duplicate:
        return True
    else:
        return False

def check_for_decision(id):
    today = date.today()            
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM decisions WHERE id = '{id}' ")
    existing_decision = c.fetchall()
    if existing_decision:
        return True
    else:
        return False

class Suggestions(Resource): #Resource expose supported methods and if request have unspported method API will return 405 method not allowed

    def post(self):
        data = request.get_json()
        name = data['name']
        suggestion = data['choice']
        id = data['id']
        duplicate=check_if_duplicate(name,suggestion,id)
        

        if duplicate:
<<<<<<< HEAD
            return jsonify(
                status = 'You already suggested this one!'
            )
            
        elif check_for_decision(id):
            return jsonify(
                status = 'Decision for this lunch was already made!'
            )
=======
            return 'Sorry, you already suggested this one :)'
        elif check_for_decision(id):
            return 'Sorry decision for this lunch was already made. You can always start a new session and vote again!'
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f

        else:
            add_suggestion(name,suggestion,id)
            remove_id_data(table_name='decisions', id=id)
<<<<<<< HEAD
            return jsonify(
                status = 'Thanks! Suggestion added.'
            )            
            
=======
            return 'Thanks!', 201
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f

#Define resources and supported methods
class WSWE(Resource): 

#POST method on /wswe 
    def post(self):
        
        today = date.today()
        data = request.get_json()
        print(type(data))

        id = data ['id']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"SELECT *  FROM decisions WHERE id='{id}'")
        existing_decision = c.fetchall()
<<<<<<< HEAD
       
        if existing_decision:
            print('existing: ' f'{existing_decision}')
            decision = existing_decision[0][1]
            name = existing_decision[0][0]
            response = jsonify(
                decision = decision,
                name = name
            )
            remove_id_data(table_name='suggestions', id=id)
            

        else:
            response = make_decision(id)
            
            if response == None:
                name = '/'
                decision = 'No suggestions found for this ID.'
                response = jsonify(
                    decision = decision,
                    name = name
                )
=======
        if existing_decision:

            print('existing: ' f'{existing_decision}')
            #decision = existing_decision[0][1]
            #print(decision)
            decision = existing_decision[0][1]
            name = existing_decision[0][0]
            response = f"You should eat: {decision} <br>It was suggested by: {name}"
            remove_id_data(table_name='suggestions', id=id)
            
            #response = make_decision(id)

        else:
            print('no decision for this id yet')
            response = make_decision(id)
            print('This is the decision')
            print(response)
            
            if response == None:
                response = 'Sorry we there were no suggestions for this id yet'
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f
            
            else:
                decision=(response[0]['suggestion'])
                name = response[0]['name']
<<<<<<< HEAD
                response = jsonify(
                    decision = decision,
                    name = name
                )
=======
                response = f"You should eat: {decision} <br> It was suggested by: {name}"
                print(decision)
>>>>>>> 68cae05df7972285a4640eda6569e34f63a47a3f
                add_decision(name,decision,id)

                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                with conn:            
                    c.execute(f"DELETE FROM suggestions WHERE id='{id}'")
                              

        return response
#Get method on /wswe
    def get(self):
        link=id_generator()
        return link

        
#Make resource availabele through url 
api.add_resource(Suggestions, "/suggestions")
api.add_resource(WSWE, "/wswe")

#run server 
if __name__ == "__main__":
    app.run(debug=True) #debug mode only for testing env