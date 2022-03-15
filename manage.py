from app import create_up

from flask_bootstrap import Bootstrap


app = create_up()
bootstrap = Bootstrap(app)





def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
   
    
if __name__== '__main__':
    app.run(debug=True)
