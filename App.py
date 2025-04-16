from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Connect to local database
def get_db_connection():
    dsn = cx_Oracle.makedsn("localhost", 1521, sid='xe')
    connection = cx_Oracle.connect(user="ProjectDB", password="Fast123", dsn=dsn)
    return connection

@app.route('/')
def home():
    return render_template('main.html')  # Render the homepage

@app.route('/view')
def view_job_cards():
        return render_template('view_job_card.html')  # Render the "View Job Cards" page

@app.route('/view/<option>')
def what_is_selected(option):
    templates = {
        'show': 'view_job_card.html',
        'enter': 'Add_Job_Card.html',
        'goods': 'Selected_View_For_Goods.html',
        'country': 'Selected_View_For_Countries.html',
        'category': 'Selected_View_For_Category.html',
        'company': 'Selected_View_For_Company.html',
        'accounts': 'Selected_View_For_Accounts.html',
        'status': 'Selected_View_For_Status.html',
    }
    return render_template(templates.get(option, '404.html'))
    
    
    

@app.route('/Selected_View_For_Goods', methods=['GET', 'POST'])
def filter_goods():
    if request.method == 'POST':
        # Check if "Display All" button was clicked
        display_all = request.form.get('display_all')

        # If "Display All" is clicked, ignore filters
        if display_all:
            query = "SELECT * FROM GOODS_TABLE"
            params = []
        else:
            # Handle filtering logic
            filter1_column = request.form.get('filter1_column')
            filter1_value = request.form.get('filter1_value')
            filter2_column = request.form.get('filter2_column')
            filter2_value = request.form.get('filter2_value')

            # Start building the query
            query = "SELECT * FROM GOODS_TABLE WHERE 1=1"
            params = []

            # Add the first filter
            if filter1_value:
                query += f" AND {filter1_column} = :1"
                params.append(filter1_value)

            # Add the second filter if provided
            if filter2_value:
                query += f" AND {filter2_column} = :2"
                params.append(filter2_value)

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # If no rows are found
            if not rows:
                return render_template('Selected_View_For_Goods.html', error="No results found", rows=None, columns=None)

            # Convert rows to dictionaries
            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Goods.html', rows=dict_rows, columns=columns)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return render_template('Selected_View_For_Goods.html')
    
@app.route('/Selected_View_For_Countries', methods=['GET', 'POST'])
def filter_countries():
    if request.method == 'POST':
        display_all = request.form.get('display_all')
        
        if display_all:
            query = "SELECT * FROM COUNTRIES"
            params = []
        else:
            # Handle filtering logic
            filter1_column = request.form.get('filter1_column')
            filter1_value = request.form.get('filter1_value')

            # Start building the query
            query = "SELECT * FROM COUNTRIES WHERE 1=1"
            params = []

            # Add the first filter
            if filter1_value:
                query += f" AND {filter1_column} = :1"
                params.append(filter1_value)

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # If no rows are found
            if not rows:
                return render_template('Selected_View_For_Countries.html', error="No results found", rows=None, columns=None)

            # Convert rows to dictionaries
            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Countries.html', rows=dict_rows, columns=columns)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return render_template('Selected_View_For_Countries.html')

@app.route('/Selected_View_For_Category', methods=['GET', 'POST'])
def filter_categories():
    if request.method == 'POST':
        display_all = request.form.get('display_all')
        
        if display_all:
            query = "SELECT * FROM CATEGORY_TABLE"
            params = []
        else:
            filter1_column = request.form.get('filter1_column')
            filter1_value = request.form.get('filter1_value')

            query = "SELECT * FROM CATEGORY_TABLE WHERE 1=1"
            params = []

            if filter1_value:
                query += f" AND {filter1_column} = :1"
                params.append(filter1_value)

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            
            if not rows:
                return render_template('Selected_View_For_Category.html', error="No results found", rows=None, columns=None)

            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Category.html', rows=dict_rows, columns=columns)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return render_template('Selected_View_For_Category.html')

@app.route('/Selected_View_For_Company', methods=['GET', 'POST'])
def filter_companies():
    if request.method == 'POST':
        display_all = request.form.get('display_all')
        
        if display_all:
            query = "SELECT * FROM COMPANIES"
            params = []
        else:
            # Handle filtering logic
            filter1_column = request.form.get('filter1_column')
            filter1_value = request.form.get('filter1_value')

            # Start building the query
            query = "SELECT * FROM COMPANIES WHERE 1=1"
            params = []

            # Add the first filter
            if filter1_value:
                query += f" AND {filter1_column} = :1"
                params.append(filter1_value)

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # If no rows are found
            if not rows:
                return render_template('Selected_View_For_Company.html', error="No results found", rows=None, columns=None)

            # Convert rows to dictionaries
            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Company.html', rows=dict_rows, columns=columns)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return render_template('Selected_View_For_Company.html')

@app.route('/Selected_View_For_Accounts', methods=['GET', 'POST'])
def filter_accounts():
    if request.method == 'POST':
        display_all = request.form.get('display_all')
        
        if display_all:
            query = "SELECT * FROM ACCOUNTS_TABLE"
            params = []
        else:
            filter1_column = request.form.get('filter1_column')
            filter1_value = request.form.get('filter1_value')

            query = "SELECT * FROM ACCOUNTS_TABLE WHERE 1=1"
            params = []

            if filter1_value:
                query += f" AND {filter1_column} = :1"
                params.append(filter1_value)

        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            if not rows:
                return render_template('Selected_View_For_Accounts.html', error="No results found", rows=None, columns=None)

            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Accounts.html', rows=dict_rows, columns=columns)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return render_template('Selected_View_For_Accounts.html')

@app.route('/Selected_View_For_Status', methods=['GET', 'POST'])
def filter_view():
    if request.method == 'POST':
        # Get user-selected table or join option
        display_option = request.form.get('display_option')

        # Get filter inputs
        filter1_column = request.form.get('filter1_column')
        filter1_value = request.form.get('filter1_value')
        filter2_column = request.form.get('filter2_column')
        filter2_value = request.form.get('filter2_value')

        # Build the base query
        query = ""
        params = []

        if display_option == "status":
            # Status table query
            query = "SELECT * FROM Status_table"

        elif display_option == "accounts":
            # Accounts table query
            query = "SELECT * FROM Accounts_table WHERE 1=1"

        elif display_option == "join":
            # Join query
            query = """
                SELECT 
                    s_t.Status_ID, 
                    s_t.Status, 
                    s_t.Payment_Status, 
                    s_t.Bill_No, 
                    a_t.Item_Cost, 
                    a_t.Duties, 
                    a_t.Taxes, 
                    a_t.Total_Cost
                FROM 
                    Status_table s_t
                JOIN 
                    Accounts_table a_t
                ON 
                    s_t.Bill_No = a_t.Bill_No
                WHERE 1=1
            """

        # Add filters dynamically
        if filter1_value:
            query += f" AND {filter1_column} = :1"
            params.append(filter1_value)

        if filter2_value:
            query += f" AND {filter2_column} = :2"
            params.append(filter2_value)

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # Handle no results
            if not rows:
                return render_template('Selected_View_For_Status.html', error="No results found", rows=None, columns=None, display_option=display_option)

            # Convert rows to dictionaries
            dict_rows = [dict(zip(columns, row)) for row in rows]
            return render_template('Selected_View_For_Status.html', rows=dict_rows, columns=columns, display_option=display_option)
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()

    else:
        # Render the filter form for a GET request
        return render_template('Selected_View_For_Status.html')
    
def generate_next_id(table, column, prefix):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Query to get the highest existing ID from the table
        query = f"""
            SELECT {column} 
            FROM {table} 
            WHERE {column} LIKE '{prefix}%' 
            ORDER BY TO_NUMBER(SUBSTR({column}, LENGTH('{prefix}') + 1)) DESC
            FETCH FIRST 1 ROWS ONLY
        """
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            # Extract the numeric part, increment it, and create the next ID
            last_id = result[0]
            num = int(last_id[len(prefix):]) + 1
            return f"{prefix}{num:03}"  # Zero-pad to 3 digits
        else:
            # If no existing IDs, start with 001
            return f"{prefix}001"
    except Exception as e:
        raise RuntimeError(f"Error generating ID: {e}")
    finally:
        cursor.close()
        connection.close()



# Add Account
@app.route('/add_account', methods=['GET', 'POST'])
def add_account():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        if request.method == 'POST':
            # Get data from the form
            bill_no = request.form['bill_no']
            item_cost = request.form['item_cost']
            duties = request.form['duties']
            taxes = request.form['taxes']
            total_cost = request.form['total_cost']

            # Insert into the database
            insert_query = """
                INSERT INTO ACCOUNTS_TABLE (BILL_NO, ITEM_COST, DUTIES, TAXES, TOTAL_COST)
                VALUES (:bill_no, :item_cost, :duties, :taxes, :total_cost)
            """
            cursor.execute(insert_query, {
                'bill_no': bill_no,
                'item_cost': item_cost,
                'duties': duties,
                'taxes': taxes,
                'total_cost': total_cost
            })
            connection.commit()
            return redirect('/add_status')  # Redirect to another route or page

    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

    return render_template('Bill_No_Entry.html')


# Add Status
@app.route('/add_status', methods=['GET', 'POST'])
def add_status():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        if request.method == 'POST':
            # Get data from the form
            status_id = request.form['status_id']
            status = request.form['status']
            payment_status = request.form['payment_status']
            bill_no = request.form['bill_no']

            # Insert into the database
            insert_query = """
                INSERT INTO STATUS_TABLE (STATUS_ID, STATUS, PAYMENT_STATUS, BILL_NO)
                VALUES (:status_id, :status, :payment_status, :bill_no)
            """
            cursor.execute(insert_query, {
                'status_id': status_id,
                'status': status,
                'payment_status': payment_status
            })
            connection.commit()
            return redirect('/add_job_card')  # Redirect to another route or page

    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()

    return render_template('Add_Status.html')

# Add Job Card
@app.route('/add_job_card/<bill_no>/<status_id>', methods=['GET', 'POST'])
def add_job_card(bill_no, status_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        if request.method == 'POST':
            # Get data from the form
            job_id = request.form['job_id']
            country_name = request.form['country_name']
            company_name = request.form['company_name']
            company_id = request.form['company_id']
            dated = request.form['dated']
            good_name = request.form['good_name']
            good_id = request.form['good_id']
            bill_no = request.form['bill_no']
            status_id = request.form['status_id']
            category_id = request.form['category_id']

            # Insert into the database
            insert_query = """
                INSERT INTO JOB_CARD_TABLE (JOB_ID, BILL_NO, COMPANY_ID, DATED, CATEGORY_ID, STATUS_ID, COUNTRY_ID, GOOD_ID)
                VALUES (:job_id, :bill_no, :company_id, :dated, :cetegory_id, :status_id, :country_id, :good_id)
            """
            cursor.execute(insert_query, {
                'job_id': job_id,
                'country_name': country_name,
                'company_name': company_name,
                'company_id': company_id,
                'dated': dated,
                'good_name': good_name,
                'good_id': good_id
            })
            connection.commit()
            return redirect('/Add_Job_Card')  # Redirect to another route or page

    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        connection.close()
    return render_template('Add_Job_Card.html')




if __name__ == '__main__':
    app.run(debug=True)