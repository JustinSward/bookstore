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
def clearCart():
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

# Adds new user to the SQLite database
@app.route('/addnewuser', methods=['POST', 'GET'])
def addnewuser():
    if request.method == 'POST':
 #       newUser = ("pw","fname","lname","tel","email",False,"country")
 #       newUser[0] = request.form['n_pw']
 #       newUser[1] = request.form['n_fname']
 #       newUser[2] = request.form['n_lname']
 #       newUser[3] = request.form['n_tel']
 #       newUser[4] = request.form['n_email']
 #       newUser[5] = request.form['n_accttype']
 #       newUser[6] = request.form['n_country']
        c.execute("""INSERT INTO useraccounts (u_pw,u_fname,u_lname,u_telephone,u_email,u_accttype,u_country) VALUES
                  (?,?,?,?,?,False,?)""",
                  (request.form['pw'],
                  request.form['fname'],
                  request.form['lname'],
                  request.form['tel'],
                  request.form['email'],
                  request.form['country']))
        conn.commit()
        
    return render_template('useradded.html')

# Adds book to the SQLite database
@app.route('/createnewbook', methods=['POST', 'GET'])
def createnewbook():
    if request.method == 'POST':
        c.execute("""INSERT INTO book (isbn,title,genre_id,publisher_id,publishyear,numpages,currentprice,qtyavail,qtyonorder)
                  VALUES (?,?,?,?,?,?,?,?,?)""",
                  (request.form['isbn'],
                  request.form['title'],
                  request.form['genre_id'],
                  request.form['publisher_id'],
                  request.form['publishyear'],
                  request.form['numpages'],
                  request.form['currentprice'],
                  request.form['qtyavail'],
                  request.form['qtyonorder']))
        conn.commit()
        
    return render_template('bookadded.html')

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

# Renders the Cart web page
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Renders the Checkout web page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Renders the View Orders web page
@app.route('/orders')
def orders():
    c.execute('SELECT * FROM orders')
    allOrders = c.fetchall()
    return render_template('orders.html', orders = allOrders)

# Renders the Account web page
@app.route('/account')
def account():
    return render_template('account.html')

# Renders the Admin web page
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Renders the Add New User web page
@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

# Renders the View Users web page
@app.route('/viewusers')
def viewusers():
    c.execute('SELECT * FROM useraccounts')
    users = c.fetchall()
    return render_template('viewusers.html', users = users)

# Renders the Add New User web page
@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

# Renders the Modify User web page
@app.route('/modifyuser')
def modifyuser():
    return render_template('modifyuser.html')

# Renders the View Commissions web page
@app.route('/viewcommissions')
def viewcommissions():
    c.execute('SELECT * FROM commissions')
    commissions = c.fetchall()
    return render_template('viewcommissions.html', commissions = commissions)

# Renders the View Publishers web page
@app.route('/viewpublishers')
def viewpublishers():
    c.execute('SELECT * FROM publisher')
    commissions = c.fetchall()
    return render_template('viewcommissions.html', commissions = commissions)

# Renders the View Sales web page
@app.route('/viewsales')
def viewsales():
    c.execute('SELECT * FROM order_manifest')
    sales = c.fetchall()
    return render_template('viewsales.html', sales = sales)


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