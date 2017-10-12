import matplotlib.pyplot as plt
import numpy as np
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas



def graphic(variableGrafica, dataArray, initTime, interval):
	
		#generate timeArray 
		timeArray = []
		for i in range(len(dataArray)):
			timeArray.append(initTime + interval*i)
		print timeArray

		#plot
   		plt.xlabel('Time')
		plt.ylabel(variableGrafica + ' samples')
		plt.title(variableGrafica)
		plt.plot(timeArray, dataArray, 'k')
		plt.savefig('/var/tmp/'+variableGrafica+'.png')
		plt.show()
		

		

def createPDF():
		#generate a PDF
		aux = canvas.Canvas("./pdf/LAG.pdf")

		aux.drawString(50,50,"RT4ALL logger")
		#include graphics

		aux.drawImage("/var/tmp/Temperature.png",100 , 350, 400,250)
		aux.drawImage("/var/tmp/Humidity.png",100, 80,400,250)
		

		aux.showPage()
		aux.save()

	


if __name__ == "__main__":

	#variableGrafica = input()
	dataArray = [23,54,36,78, 32,76,12]
	graphic('Temperature',dataArray, 1, 0.5)
	graphic('Humidity',dataArray, 1, 0.5)
	createPDF();
	
	
	






