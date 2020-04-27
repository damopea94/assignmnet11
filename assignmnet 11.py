import matplotlib.pyplot as plt
import mysql.connector


def get_connection():
	connection = mysql.connector.connect(host='localhost', user='root',passwd='',db='world')
	return connection


def get_countries():
	connection = get_connection()
	cursor = connection.cursor()
	cursor.execute("SELECT c.name,LifeExpectancy FROM country d INNER JOIN city c ON c.countrycode=d.code WHERE Continent='Oceania'")
	result = cursor.fetchall()
	return result


def set_data():
	result=get_countries()
	index=0;
	names = []
	data = []
	for row in result:
		names.append(row[0])
		data.append(row[1])
		index=index+1

	return names ,data


def main():
	print('Showing data for Oceania')
	names,data=set_data()
	print("name=",len(names))
	fig = plt.figure()
	ax = fig.add_axes([0, 0, 1, 1])
	ax.bar(names, data)
	plt.show()


main()