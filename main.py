# PROGRAMMED BY JUSTIN SWARD, 100683372
import os
import sqlite3
from flask import Flask, flash, render_template, url_for, request, redirect, Response, send_file
from datetime import datetime
from operator import itemgetter, attrgetter

app = Flask(__name__)       # Use the flask Python web framework
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    ## Don't think this will be implemented in the bookstore app

# Establish connection with the SQLite database for this project, bookstore.db  (located in same parent directory)
conn = sqlite3.connect('bookstore.db', check_same_thread=False)
c = conn.cursor()



# Definition of the Cart class (holds cart items)
class Cart:
    cart_userid = 0 # User id of the cart owner (0 by default)
 #   num_cartitems = 0 # Keeps track of the number of items in the shopping cart (MAYBE JUST USE cart_items.len()???)
    cart_items = []


        

# Definition of the CartItem class (belonging to a Cart)
class Cart_Item:

    def __init__(self, itemNum, itemISBN, itemQty):
        self.itemnum = itemNum              # Numerate which cart item it is in the array
        self.itemISBN = int(itemISBN)       # ISBN of book item in cart
        self.itemQty = int(itemQty)         # Quantity in cart

    def getItemISBN(self):
        return self.itemISBN
    
    def getId(self):
        return self.itemQty
    






# Removes all items from the shopping cart
@app.route('/clear')
def clearCist():
    Cart.cart_array.clear()
    Cart.num_cartitems = 0
    return redirect('/')




# Renders the Home web page
@app.route('/', methods=['POST', 'GET'])
def about():
    global logged_in
    if request.method == 'POST':
        ulogin_username = request.form['username']
        ulogin_password = request.form['password']

        c.execute("SELECT u_id FROM useraccounts WHERE u_email=? AND u_pw=?", (ulogin_username, ulogin_password))
        
        temp = c.fetchall() #returns a list/tuple format -- need only the user id value
        for item in temp:
            print(temp)
            logged_in = temp[0]
        
    return render_template('home.html', logged_in_HTML = logged_in)

# Logs the user out and returns home
@app.route('/logout')
def logout():
    logged_in = 0
    return render_template('home.html', logged_in_HTML = logged_in)

# Renders the Admin web page
@app.route('/search')
def search():
    c.execute('SELECT * FROM book')
    books = c.fetchall()
    return render_template('search.html', books = books)

# Renders the Admin web page
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Renders the Admin web page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Renders the Admin web page
@app.route('/orders')
def orders():
    return render_template('orders.html')

# Renders the Account web page
@app.route('/account')
def account():
    return render_template('account.html')

# Renders the Admin web page
@app.route('/admin')
def admin():
    return render_template('admin.html')



#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   

# Run the main program
if __name__ == "__main__":
    logged_in = int(0)       # By default, not logged in
    admin_access = 0    # By default, no admin access
    sessionCart = Cart # Creates a shopping cart object for the current session
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    app.run(debug=True) # Add Port 8080 to run virtualenv on the Google Cloud App platform