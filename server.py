from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
@app.route('/<int:num_w>/<int:num_h>')
@app.route('/<int:num_w>/<int:num_h>')
@app.route('/<int:num_w>/<int:num_h>')
@app.route('/<int:num_w>/<int:num_h>/<string:colorOne>/<string:colorTwo>')
@app.route('/<int:num_w>/<int:num_h>/<string:colorOne>/<string:colorTwo>')

def default_checker(num_w=8, num_h=8,colorOne='colorOne', colorTwo='colorTwo'):
    return render_template('index.html', num_w=num_w, num_h=num_h,colorOne=colorOne, colorTwo=colorTwo)  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
