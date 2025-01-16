from app import create_app
from main import main

# Run main.py when initialising the flask app
main()

app = create_app()


if __name__ == '__main__':
	#Run the flask app
	app.run(host='0.0.0.0',port=5000,debug=True)
