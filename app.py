
















# from flask import Flask, render_template, request, redirect, url_for, session,flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from werkzeug.utils import secure_filename
# import os
# import re
# import random
# # from codecarbon import EmissionsTracker
# from flask_caching import Cache
# from flask_bcrypt import Bcrypt


# app = Flask(__name__)
# bcrypt = Bcrypt(app)
# app.secret_key = 'your_secret_key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'sakshi#12345'
# app.config['MYSQL_DB']='geeklogin'
# app.config['PORT']='3306'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sakshi#12345@localhost:3306/geeklogin'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

# app.config['CACHE_TYPE'] = 'SimpleCache'  # Using in-memory cache
# app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache data for 5 minutes
# cache = Cache(app)

# mysql = MySQL(app)
# db=SQLAlchemy(app)

# app.app_context().push()
# # tracker = EmissionsTracker()
# class Products(db.Model):
#     sno=db.Column(db.Integer,primary_key=True)
#     fid=db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
#     product_name=db.Column(db.String(100),nullable=False)
#     price = db.Column(db.Float,nullable=False)
#     quantity = db.Column(db.Integer,nullable=False)
#     category = db.Column(db.String(50),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)

#     def _repr_(self)->str:
#          return f"{self.sno} - {self.product_name}"

# class Accounts(db.Model):
#     fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     Role = db.Column(db.String(255), nullable=True) 
#     # Other columns in the accounts table...

# def _repr_(self)->str:
#          return f"{self.fid} - {self.email}"

# class Earning(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
#     amount_earned = db.Column(db.Float, nullable=False)
#     order_date = db.Column(db.DateTime, default=datetime.utcnow)

# def _repr_(self)->str:
#     return f"{self.order_id} - {self.fid} - {self.amount_earned}"

# class Cart(db.Model):
#     ch_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     bill_id = db.Column(db.Integer, nullable=False)
#     sno=db.Column(db.Integer,db.ForeignKey('products.sno'),nullable=False)
#     product_name=db.Column(db.String(100),nullable=False)
#     price = db.Column(db.Float,nullable=False)
#     quantity = db.Column(db.Integer,nullable=False)

# def _repr_(self)->str:
#     return f"{self.bill_id}"

# def genbill():
#     bid = random.randint(1, 10000)
#     return bid



# # class Earning(db.Model):
# #     __tablename__ = 'earning'
# #     order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
# #     amount_earned = db.Column(db.Float, nullable=False)
# #     order_date = db.Column(db.DateTime, default=datetime.utcnow)

# #     def __repr__(self) -> str:
# #         return f"{self.order_id} - {self.fid} - {self.amount_earned}"


# @app.route('/term')
# def term():
#     # Your view function logic here
#     return render_template('terms.html')


# @app.route('/')
# @cache.cached(timeout=300)
# def index():
#     return render_template('index.html')

# @app.route('/signup')
# def signup():
#     return render_template('login.html')
#     # Your signup logic here


# @app.route('/payment_details')
# def paydet(bill_id):
#     prods = Cart.query.filter_by(bill_id=bill_id)


#     return render_template('addcart.html')
# # @app.route('/addfrmr', methods=['GET','POST'])
# # def addfrmr():
# #     if request.method=='POST':
# #         # fid=request.form['farmer_id']  removed because fid is auto-incremented

# #         # fid = session.get('fid')
# #         # if fid is None:
# #         if 'fid' not in session:
# #             flash('User not logged in!', 'error')
# #             return redirect(url_for('login'))
        
# #         fid=session['fid']
# #         email=session.get('email')

# #         account=Accounts.query.filter_by(email=email).first()
# #         if not account:
# #             flash('User Email not found!','error')
# #             return redirect(url_for('login'))
        
# #         if account.fid != fid:
# #             flash('Incorrect farmer ID for the logged-in user!', 'error')
# #             return redirect(url_for('login'))
        
        

# #         product_name=request.form['product_name']
# #         price=request.form['price']
# #         quantity=request.form['quantity']
# #         category=request.form['category']
# #         todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
# #         db.session.add(todo)
# #         db.session.commit()
# #         flash('Product added successfully!', 'success')
# #         return redirect('addfrmr')
    
# #     alltodo=Products.query.all()
# #     return render_template('prodt_add_farmer.html',alltodo=alltodo)

# # @app.route('/ProductDelete/<int:sno>')
# # def Delete(sno):
# #     todo=Products.query.filter_by(sno=sno).first()
# #     fid=todo.fid
# #     db.session.delete(todo)
# #     db.session.commit()
# #     return redirect(url_for('addfrmr', fid=fid))


# @app.route('/ProductDelete/<int:sno>')
# def delete_product(sno):
#     product = Products.query.filter_by(sno=sno).first()
#     if product:
#         fid = product.fid
#         db.session.delete(product)
#         db.session.commit()
#         cache.delete('all_products')  # Clear cache after deletion
#         return redirect(url_for('addfrmr', fid=fid))
#     flash("Product not found!", "error")
#     return redirect(url_for('index'))


# @app.route('/ProductUpdate/<int:sno>', methods=['GET','POST'])
# def Update(sno):
#     if request.method=='POST':
#         product_name=request.form['product_name']
#         price=request.form['price']
#         quantity=request.form['quantity']
#         category=request.form['category']
#         todo=Products.query.filter_by(sno=sno).first()
#         fid = todo.fid
#         todo.product_name=product_name
#         todo.price=price
#         todo.quantity=quantity
#         todo.category=category
#         db.session.add(todo)
#         db.session.commit()
#         cache.delete('product_' + str(sno))
#         return redirect(url_for('addfrmr', fid=fid))


#     todo=Products.query.filter_by(sno=sno).first()
#     # fid=todo.fid
#     return render_template('ProductUpdate.html',todo=todo)

# # def get_prod(sno):
# #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# #     cursor.execute('SELECT * FROM products WHERE sno = %s', (sno,))
# #     prod = cursor.fetchone()
# #     return prod


# # @app.route('/ahtml', methods=['GET', 'POST'])
# # def addcart():
# #     alltodo = Products.query.all()

# #     # Initialize cart in session if not already present
# #     if 'cart' not in session:
# #         session['cart'] = []

# #     if request.method == 'POST':
# #         # Get product details
# #         qty = int(request.form['quantity'])
# #         todo_sno = request.form['todo_sno']
# #         prod = Products.query.filter_by(sno=todo_sno).first()

# #         if not prod:
# #             return 'Product not found', 404

# #         if prod.quantity < qty:
# #             return 'Insufficient stock', 400

# #         # Add item to session cart
# #         cart_item = {
# #             "sno": prod.sno,
# #             "product_name": prod.product_name,
# #             "price": prod.price,
# #             "quantity": qty,
# #         }

# #         # Check if item already in cart
# #         for item in session['cart']:
# #             if item['sno'] == prod.sno:
# #                 item['quantity'] += qty
# #                 break
# #         else:
# #             session['cart'].append(cart_item)

# #         # Save session changes
# #         session.modified = True
# #         return redirect(url_for('addcart'))

# #     return render_template('ahtml.html', alltodo=alltodo, cart=session['cart'])

# # @app.route('/viewcart', methods=['GET'])
# # def view_cart():
# #     # Retrieve the cart from the session
# #     cart = session.get('cart', [])
    
# #     # Calculate the total payable amount
# #     total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
# #     return render_template('addcart.html', cart=cart, total_amount=total_amount)

# # @app.route('/clearcart', methods=['POST'])
# # def clear_cart():
# #     if 'cart' in session:
# #         for item in session['cart']:
# #             product = Cart.query.filter_by(product_name=item['product_name']).first()
# #             if product:
# #                 product.quantity += item['quantity']  # Restore the quantity
# #         db.session.commit()
# #         session.pop('cart', None)
# #     flash('Cart cleared successfully!')
# #     return redirect(url_for('addcart'))












# @app.route('/ahtml', methods=['GET', 'POST'])
# def addcart():
#     alltodo = Products.query.all()

#     # Initialize cart in session if not already present
#     if 'cart' not in session:
#         session['cart'] = []

#     if request.method == 'POST':
#         # Get product details
#         qty = int(request.form['quantity'])
#         todo_sno = request.form['todo_sno']
#         prod = Products.query.filter_by(sno=todo_sno).first()

#         if not prod:
#             return 'Product not found', 404

#         if prod.quantity < qty:
#             return 'Insufficient stock', 400

#         # Add item to session cart
#         cart_item = {
#             "sno": prod.sno,
#             "product_name": prod.product_name,
#             "price": prod.price,
#             "quantity": qty,
#         }

#         # Check if item already in cart
#         for item in session['cart']:
#             if item['sno'] == prod.sno:
#                 item['quantity'] += qty
#                 break
#         else:
#             session['cart'].append(cart_item)

#         # Reduce stock in the Products table
#         prod.quantity -= qty

#         # Save session changes and commit to database
#         db.session.commit()
#         session.modified = True
#         return redirect(url_for('addcart'))

#     return render_template('ahtml.html', alltodo=alltodo, cart=session['cart'])


# @app.route('/viewcart', methods=['GET'])
# def view_cart():
#     # Retrieve the cart from the session
#     cart = session.get('cart', [])
    
#     # Calculate the total payable amount
#     total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
#     return render_template('addcart.html', cart=cart, total_amount=total_amount)


# @app.route('/clearcart', methods=['POST'])
# def clear_cart():
#     if 'cart' in session:
#         for item in session['cart']:
#             product = Products.query.filter_by(sno=item['sno']).first()
#             if product:
#                 product.quantity += item['quantity']  # Restore the quantity
#         db.session.commit()
#         session.pop('cart', None)
#     flash('Cart cleared successfully!')
#     return redirect(url_for('addcart'))












# @app.route('/<int:fid>/earning')
# def earn(fid):
#     earnings = Earning.query.filter_by(fid=fid).all()
#     if not earnings:
#         return "Farmer not found", 404

#     total_amount = sum(earning.amount_earned for earning in earnings)
#     service_charge = total_amount * 0.05
#     return render_template('earning.html', earnings=earnings, totalamt=total_amount, servicech=service_charge)



# @app.route('/paynow', methods=['POST'])
# def pay_now():
#     cart = session.get('cart', [])
#     if not cart:
#         return "Your cart is empty!", 400
    
#     # Calculate the total amount
#     total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
#     # Update the farmer's earnings and reduce product stock
#     for item in cart:
#         # Fetch the product using its ID
#         product = Products.query.filter_by(sno=item['sno']).first()
        
#         if not product:
#             return f"Product with ID {item['sno']} not found!", 404
        
#         # Ensure sufficient stock
#         if product.quantity < item['quantity']:
#             return f"Insufficient stock for product {product.product_name}!", 400
        
#         # Reduce stock
#         product.quantity -= item['quantity']
        
#         # Update farmer's earnings
#         farmer = Accounts.query.filter_by(fid=product.fid).first()
#         if farmer:
#             # Add earnings
#             new_earning = Earning(
#                 fid=farmer.fid,
#                 amount_earned=item['price'] * item['quantity']
#             )
#             db.session.add(new_earning)
#         else:
#             return f"Farmer with ID {product.fid} not found!", 404
    
#     # Commit all changes
#     db.session.commit()
    
#     # Clear the cart after payment
#     session.pop('cart', None)
    
#     # Redirect to the Pay.html page with the total amount
#     return render_template('Pay.html', amount=total_amount)

# def del_prod(sno):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('DELETE FROM products WHERE sno = %s', (sno,))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     msg = ' '
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'fid' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         fid = request.form['fid']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s AND fid= %s', (email, password,fid))
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['fid'] = account['fid']
#             session['email'] = account['email']
#             msg = 'Logged in successfully!'
#             return redirect(url_for('frfid', fid=fid))
#         else:
#             msg = 'Incorrect email / password!'
#     return render_template('login.html', msg=msg)

# @app.route('/<int:fid>', methods=['GET', 'POST'])
# def frfid(fid):
#     farmer = Accounts.query.get_or_404(fid)
#     return render_template('farmer_details.html', farmer=farmer)

# @app.route('/<int:fid>/products', methods=['GET', 'POST'])
# def addfrmr(fid):    
#     farmer=Products.query.filter_by(fid=fid).all()  
#     if request.method=='POST':    
#         # fid=request.form['farmer_id']  removed because fid is auto-incremented
   
#         #fid = session.get('fid')    
#         if fid is None:    
#             flash('User not logged in!', 'error')    
#             return redirect(url_for('login'))    
   
#         product_name=request.form['product_name']    
#         price=request.form['price']    
#         quantity=request.form['quantity']    
#         category=request.form['category']    
#         todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
#         db.session.add(todo)    
#         db.session.commit() 
#         # tracker.stop()   
#         flash('Product added successfully!', 'success')    
#         return redirect(url_for('addfrmr', fid=fid))    
#     return render_template('prodt_add_farmer.html',farmer=farmer) 



# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('email', None)
#     return redirect(url_for('login'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         Role=request.form['Role']

#          # Check if the email is already registered
#         existing_user = Accounts.query.filter_by(email=email).first()
#         if existing_user:
#             flash('Email address already exists!', 'error')
#             return redirect(url_for('login'))

#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
#         account = cursor.fetchone()
#         if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             flash('Invalid email address!', 'error')
#             return redirect(url_for('signup'))
        
#         if Role == 'Farmer':
#             cursor.execute('SELECT fid FROM accounts WHERE email = %s', (email,))
#             farmer = cursor.fetchone()
#             if farmer:
#                 farmer_id = farmer['fid']

       

#         # Create a new Accounts object and add it to the database
#         new_user = Accounts(username=username, password=password, email=email,Role=Role)
#         db.session.add(new_user)
#         db.session.commit()

#         flash('Registration successful! Please log in.', 'success')

        
#         if Role=="Buyer":
#             return redirect(url_for('display_products'))
#         elif Role=='Farmer':
#             return redirect(url_for('login'))
    
    


#     last_user = Accounts.query.order_by(Accounts.fid.desc()).first()
#     if last_user:
#         farmer_id = last_user.fid + 1  # Assuming fid is auto-incremented
#     else:
#         farmer_id = 1  # Initial value for farmer_id

    
#     return render_template('register.html',msg=msg , farmer_id=farmer_id)




# @app.route('/list')
# def list_products():
#     products = Products.query.all()
#     product_counts = {}
#     for product in products:
#         if product.product_name in product_counts:
#             product_counts[product.product_name] += 1
#         else:
#             product_counts[product.product_name] = 1
#     return render_template('List.html', product_counts=product_counts)





# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'product-image' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['product-image']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # Here you would typically save the filename to a database along with other product details
#             return 'File uploaded successfully'
#     return render_template('index.html')
  
# # if __name__ == "__main__":
# #     app.run(debug=True)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)













# @app.route('/ProductDelete/<int:sno>')
# def delete_product(sno):
#     product = Products.query.filter_by(sno=sno).first()
#     if product:
#         fid = product.fid
#         db.session.delete(product)
#         db.session.commit()
#         cache.delete('all_products')  # Clear cache after deletion
#         return redirect(url_for('addfrmr', fid=fid))
#     flash("Product not found!", "error")
#     return redirect(url_for('index'))


















from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import re
import random
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
app = Flask(__name__)

app.secret_key = 'your_secret_key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'sakshi#12345'
# app.config['MYSQL_DB']='geeklogin'
# app.config['PORT']='3306'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sakshi#12345@localhost:3306/geeklogin'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

# mysql = MySQL(app)
# db=SQLAlchemy(app)

# Configure MySQL using environment variables (Render will provide these)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'geeklogin')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))

# SQLAlchemy configuration (Recommended for production)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}"
    f"@{app.config['MYSQL_HOST']}:{app.config['MYSQL_PORT']}/{app.config['MYSQL_DB']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Initialize SQLAlchemy
mysql = MySQL(app)    # If using Flask-MySQL

app.app_context().push()

class Products(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    fid=db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
    product_name=db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    

    def _repr_(self)->str:
         return f"{self.sno} - {self.product_name}"

class Accounts(db.Model):
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    Role = db.Column(db.String(255), nullable=True)
    products = db.relationship('Products', backref='owner', lazy='dynamic') 
    # Other columns in the accounts table...

def _repr_(self)->str:
         return f"{self.fid} - {self.email}"

class Earning(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
    amount_earned = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    account = db.relationship('Accounts', backref='earnings', lazy='joined')


def _repr_(self)->str:
    return f"{self.order_id} - {self.fid} - {self.amount_earned}"

class Cart(db.Model):
    ch_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    bill_id = db.Column(db.Integer, nullable=False)
    sno=db.Column(db.Integer,db.ForeignKey('products.sno'),nullable=False)
    product_name=db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)

def _repr_(self)->str:
    return f"{self.bill_id}"

def genbill():
    bid = random.randint(1, 10000)
    return bid



# class Earning(db.Model):
#     __tablename__ = 'earning'
#     order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     fid = db.Column(db.Integer, db.ForeignKey('accounts.fid'), nullable=False)
#     amount_earned = db.Column(db.Float, nullable=False)
#     order_date = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.order_id} - {self.fid} - {self.amount_earned}"


@app.route('/term')
def term():
    # Your view function logic here
    return render_template('terms.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('login.html')
    # Your signup logic here


@app.route('/payment_details')
def paydet(bill_id):
    prods = Cart.query.filter_by(bill_id=bill_id)


    return render_template('addcart.html')
# @app.route('/addfrmr', methods=['GET','POST'])
# def addfrmr():
#     if request.method=='POST':
#         # fid=request.form['farmer_id']  removed because fid is auto-incremented

#         # fid = session.get('fid')
#         # if fid is None:
#         if 'fid' not in session:
#             flash('User not logged in!', 'error')
#             return redirect(url_for('login'))
        
#         fid=session['fid']
#         email=session.get('email')

#         account=Accounts.query.filter_by(email=email).first()
#         if not account:
#             flash('User Email not found!','error')
#             return redirect(url_for('login'))
        
#         if account.fid != fid:
#             flash('Incorrect farmer ID for the logged-in user!', 'error')
#             return redirect(url_for('login'))
        
        

#         product_name=request.form['product_name']
#         price=request.form['price']
#         quantity=request.form['quantity']
#         category=request.form['category']
#         todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
#         db.session.add(todo)
#         db.session.commit()
#         flash('Product added successfully!', 'success')
#         return redirect('addfrmr')
    
#     alltodo=Products.query.all()
#     return render_template('prodt_add_farmer.html',alltodo=alltodo)

@app.route('/ProductDelete/<int:sno>')
def Delete(sno):
    todo=Products.query.filter_by(sno=sno).first()
    fid=todo.fid
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('addfrmr', fid=fid))

@app.route('/ProductUpdate/<int:sno>', methods=['GET','POST'])
def Update(sno):
    if request.method=='POST':
        product_name=request.form['product_name']
        price=request.form['price']
        quantity=request.form['quantity']
        category=request.form['category']
        todo=Products.query.filter_by(sno=sno).first()
        fid = todo.fid
        todo.product_name=product_name
        todo.price=price
        todo.quantity=quantity
        todo.category=category
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('addfrmr', fid=fid))


    todo=Products.query.filter_by(sno=sno).first()
    # fid=todo.fid
    return render_template('ProductUpdate.html',todo=todo)

# def get_prod(sno):
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT * FROM products WHERE sno = %s', (sno,))
#     prod = cursor.fetchone()
#     return prod


# @app.route('/ahtml', methods=['GET', 'POST'])
# def addcart():
#     alltodo = Products.query.all()

#     # Initialize cart in session if not already present
#     if 'cart' not in session:
#         session['cart'] = []

#     if request.method == 'POST':
#         # Get product details
#         qty = int(request.form['quantity'])
#         todo_sno = request.form['todo_sno']
#         prod = Products.query.filter_by(sno=todo_sno).first()

#         if not prod:
#             return 'Product not found', 404

#         if prod.quantity < qty:
#             return 'Insufficient stock', 400

#         # Add item to session cart
#         cart_item = {
#             "sno": prod.sno,
#             "product_name": prod.product_name,
#             "price": prod.price,
#             "quantity": qty,
#         }

#         # Check if item already in cart
#         for item in session['cart']:
#             if item['sno'] == prod.sno:
#                 item['quantity'] += qty
#                 break
#         else:
#             session['cart'].append(cart_item)

#         # Save session changes
#         session.modified = True
#         return redirect(url_for('addcart'))

#     return render_template('ahtml.html', alltodo=alltodo, cart=session['cart'])

# @app.route('/viewcart', methods=['GET'])
# def view_cart():
#     # Retrieve the cart from the session
#     cart = session.get('cart', [])
    
#     # Calculate the total payable amount
#     total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
#     return render_template('addcart.html', cart=cart, total_amount=total_amount)

# @app.route('/clearcart', methods=['POST'])
# def clear_cart():
#     if 'cart' in session:
#         for item in session['cart']:
#             product = Cart.query.filter_by(product_name=item['product_name']).first()
#             if product:
#                 product.quantity += item['quantity']  # Restore the quantity
#         db.session.commit()
#         session.pop('cart', None)
#     flash('Cart cleared successfully!')
#     return redirect(url_for('addcart'))












@app.route('/ahtml', methods=['GET', 'POST'])
def addcart():
    alltodo = Products.query.all()

    # Initialize cart in session if not already present
    if 'cart' not in session:
        session['cart'] = []

    if request.method == 'POST':
        # Get product details
        qty = int(request.form['quantity'])
        todo_sno = request.form['todo_sno']
        prod = Products.query.filter_by(sno=todo_sno).first()

        if not prod:
            return 'Product not found', 404

        if prod.quantity < qty:
            return 'Insufficient stock', 400

        # Add item to session cart
        cart_item = {
            "sno": prod.sno,
            "product_name": prod.product_name,
            "price": prod.price,
            "quantity": qty,
        }

        # Check if item already in cart
        for item in session['cart']:
            if item['sno'] == prod.sno:
                item['quantity'] += qty
                break
        else:
            session['cart'].append(cart_item)

        # Reduce stock in the Products table
        prod.quantity -= qty

        # Save session changes and commit to database
        db.session.commit()
        session.modified = True
        return redirect(url_for('addcart'))

    return render_template('ahtml.html', alltodo=alltodo, cart=session['cart'])


@app.route('/viewcart', methods=['GET'])
def view_cart():
    # Retrieve the cart from the session
    cart = session.get('cart', [])
    
    # Calculate the total payable amount
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    
    return render_template('addcart.html', cart=cart, total_amount=total_amount)


@app.route('/clearcart', methods=['POST'])
def clear_cart():
    if 'cart' in session:
        for item in session['cart']:
            product = Products.query.filter_by(sno=item['sno']).first()
            if product:
                product.quantity += item['quantity']  # Restore the quantity
        db.session.commit()
        session.pop('cart', None)
    flash('Cart cleared successfully!')
    return redirect(url_for('addcart'))












@app.route('/<int:fid>/earning')
def earn(fid):
    earnings = Earning.query.filter_by(fid=fid).all()
    if not earnings:
        return "Farmer not found", 404

    total_amount = sum(earning.amount_earned for earning in earnings)
    service_charge = total_amount * 0.05
    return render_template('earning.html', earnings=earnings, totalamt=total_amount, servicech=service_charge)



@app.route('/paynow', methods=['POST'])
def pay_now():
    cart = session.get('cart', [])
    if not cart:
        return "Your cart is empty!", 400
    
    # Calculate the total amount
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    products_to_delete = []
    # Update the farmer's earnings and reduce product stock
    for item in cart:
        # Fetch the product using its ID
        product = Products.query.filter_by(sno=item['sno']).first()
        if product.quantity == 0:
            products_to_delete.append(product)     
        if not product:
            return f"Product with ID {item['sno']} not found!", 404
        # if product.quantity < item['quantity']:
        #     return f"Insufficient stock for product {product.product_name}!", 400
        # Ensure sufficient stock
        if product.quantity <= 0:
            db.session.delete(product)
        
        # Reduce stock
        # product.quantity -= item['quantity']
        
        # Update farmer's earnings
        farmer = Accounts.query.filter_by(fid=product.fid).first()
        if farmer:
            # Add earnings
            new_earning = Earning(
                fid=farmer.fid,
                amount_earned=item['price'] * item['quantity']
            )
            db.session.add(new_earning)
        else:
            return f"Farmer with ID {product.fid} not found!", 404
    
    # Commit all changes
    db.session.commit()
    
    # Clear the cart after payment
    session.pop('cart', None)
    
    # Redirect to the Pay.html page with the total amount
    return render_template('Pay.html', amount=total_amount)











def del_prod(sno):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM products WHERE sno = %s', (sno,))





@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ' '
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'fid' in request.form:
        email = request.form['email']
        password = request.form['password']
        fid = request.form['fid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s AND fid= %s', (email, password,fid))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['fid'] = account['fid']
            session['email'] = account['email']
            msg = 'Logged in successfully!'
            return redirect(url_for('frfid', fid=fid))
        else:
            msg = 'Incorrect email / password!'
    return render_template('login.html', msg=msg)



@app.route('/<int:fid>', methods=['GET', 'POST'])
def frfid(fid):
    farmer = Accounts.query.get_or_404(fid)
    return render_template('farmer_details.html', farmer=farmer)

@app.route('/<int:fid>/products', methods=['GET', 'POST'])
def addfrmr(fid):    
    farmer=Products.query.filter_by(fid=fid).all()  
    if request.method=='POST':    
        # fid=request.form['farmer_id']  removed because fid is auto-incremented
   
        #fid = session.get('fid')    
        if fid is None:    
            flash('User not logged in!', 'error')    
            return redirect(url_for('login'))    
   
        product_name=request.form['product_name']    
        price=request.form['price']    
        quantity=request.form['quantity']    
        category=request.form['category']    
        todo=Products(fid=fid,product_name=product_name,price=price,quantity=quantity,category=category)
        db.session.add(todo)    
        db.session.commit()    
        flash('Product added successfully!', 'success')    
        return redirect(url_for('addfrmr', fid=fid))    
    return render_template('prodt_add_farmer.html',farmer=farmer) 



@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        Role=request.form['Role']

         # Check if the email is already registered
        existing_user = Accounts.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already exists!', 'error')
            return redirect(url_for('login'))

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'error')
            return redirect(url_for('signup'))
        
        if Role == 'Farmer':
            cursor.execute('SELECT fid FROM accounts WHERE email = %s', (email,))
            farmer = cursor.fetchone()
            if farmer:
                farmer_id = farmer['fid']

       

        # Create a new Accounts object and add it to the database
        new_user = Accounts(username=username, password=password, email=email,Role=Role)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')

        
        if Role=="Buyer":
            return redirect(url_for('display_products'))
        elif Role=='Farmer':
            return redirect(url_for('login'))
    
    


    last_user = Accounts.query.order_by(Accounts.fid.desc()).first()
    if last_user:
        farmer_id = last_user.fid + 1  # Assuming fid is auto-incremented
    else:
        farmer_id = 1  # Initial value for farmer_id

    
    return render_template('register.html',msg=msg , farmer_id=farmer_id)




@app.route('/list')
def list_products():
    products = Products.query.all()
    product_counts = {}
    for product in products:
        if product.product_name in product_counts:
            product_counts[product.product_name] += 1
        else:
            product_counts[product.product_name] = 1
    return render_template('List.html', product_counts=product_counts)





@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'product-image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['product-image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Here you would typically save the filename to a database along with other product details
            return 'File uploaded successfully'
    return render_template('index.html')

tracker.stop()
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)













