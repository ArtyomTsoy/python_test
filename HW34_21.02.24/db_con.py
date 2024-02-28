import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

mycursor = mydb.cursor()


def show_contacts(cursor):
    sql_query = "SELECT * FROM contacts"
    cursor.execute(sql_query)
    contacts_all = cursor.fetchall()
    return contacts_all


def create_contact(user_data):
    global mycursor
    global mydb

    u_data = user_data.strip().split(' ')

    l_name = u_data[0]
    f_name = u_data[1]
    m_name = u_data[2] if len(u_data) >= 3 else ''

    sql_query = "INSERT INTO contacts (l_name, f_name, m_name) VALUES (%s, %s, %s)"
    contact_data = (l_name, f_name, m_name)

    mycursor.execute(sql_query, contact_data)
    mydb.commit()


def update_contact(contact_id, new_data):
    global mycursor
    global mydb

    u_data = new_data.strip().split(' ')
    l_name = u_data[0]
    f_name = u_data[1]
    m_name = u_data[2] if len(u_data) >= 3 else ''

    sql_query = "UPDATE contacts SET l_name = %s, f_name = %s, m_name = %s WHERE id = %s"
    contact_data = (l_name, f_name, m_name, contact_id)

    mycursor.execute(sql_query, contact_data)
    mydb.commit()


def delete_contact(contact_id):
    global mycursor
    global mydb

    sql_query = "DELETE FROM contacts WHERE id = %s"
    contact_data = (contact_id,)

    mycursor.execute(sql_query, contact_data)
    mydb.commit()