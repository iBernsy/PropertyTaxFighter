import selenium, time, os, pandas, csv, re, string
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

EXCEL_HEADERS = []
EXCEL_DATA = []

Homesite_Headers_Data_1 = ['-','-','-','-','-','-']
Homesite_Tables_Data_2 = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']

def fillSegments(fill, landHeaders, landData, tempLandHeaders, counter):
    for i in range (1, fill):
        for header in tempLandHeaders:
            landHeaders.append(str(counter) + ' - ' + header)
            landData.append('-')
        counter += 1

def addData(datalist, columnType):
    global EXCEL_DATA, EXCEL_HEADERS
    if(columnType == 0):
        for i in datalist:
            EXCEL_HEADERS.append(i)
    else:
        for i in datalist:
            EXCEL_DATA.append(i)

def concatenateImprovementHeader(df):
    improvementData = []
    improvementHeaders = []
    df = pandas.concat(df)
    for row in df.itertuples():        
        #print(row)
        for i in range(2, 7):
            if(row[0] == 0):
                improvementHeaders.append(row[i])
            else:
                improvementData.append(row[i])
    improvementHeaders.append('$ per Sq.ft')
    improvementData.append(int(re.sub(r'\D', "", improvementData[4])) / int(re.sub(r'\D', "", improvementData[3])))

    addData(improvementHeaders, 0)
    addData(improvementData, 1)

def concatenateLandSegments(df):
    df = pandas.concat(df)
    df = df.loc[~df.index.duplicated(keep='first')]
    df = df.iloc[2:]
    tempLandHeaders = []
    landHeaders=[]
    landData=[]
    segmentValue = ''
    for row in df.itertuples():
        for i in range(1, 7):
            if (row[0] == 2):
                tempLandHeaders.append(row[i])
            elif (row[1] == 'TOTALS'):
                if (i == 6):
                    segmentValue = str([row[i]])
            else:
                landData.append(row[i])
        if not (row[0] == 2 or row[1] == 'TOTALS'):
            for header in tempLandHeaders:
                landHeaders.append(str(row[1]) + ' - ' + header)  
                #print(str(row))     
    if (len(landHeaders) < 24 and len(landData) < 24):
        if (len(landHeaders) < 6 and len(landData) < 6): # Add 4
            counter = 1
            fillSegments(5, landHeaders, landData, tempLandHeaders, counter)
        elif (len(landHeaders) < 12 and len(landData) < 12): # Add 3
            counter = 2
            fillSegments(4, landHeaders, landData, tempLandHeaders, counter)
        elif (len(landHeaders) < 18 and len(landData) < 18): # Add 2
            counter = 3
            fillSegments(3, landHeaders, landData, tempLandHeaders, counter)
        elif (len(landHeaders) < 24 and len(landData) < 24): # Add 1
            counter = 4
            fillSegments(2, landHeaders, landData, tempLandHeaders, counter)
        else:
            print("Error in Records... ")


        landHeaders.append('Land Segments Totals') 
        landData.append(segmentValue)   
        addData(landHeaders, 0)
        addData(landData, 1)

def concatenateTable(df):
    columnHeaders = []
    columnValues = []
    df = pandas.concat(df)
    for row in df.itertuples():
        if not (pandas.isnull(row[1])) or (row[1] == row[2]):
            columnHeaders.append(row[1])
            columnValues.append(row[2])
    
    addData(columnHeaders, 0)
    addData(columnValues, 1)

def firstImprovement(df):
    df = pandas.concat(df)
    tempHeader = ['Record', 'Type', 'Year Built', 'Sq. Ft', 'Value']
    tempData = []
    for row in df.itertuples():
        if not(pandas.isnull(row[1])):
            for i in range(1,7):
                if (row[1] == 1):
                    if not (row[i] == 'Details'):
                        tempData.append(row[i])
                else:
                    if (i % 2 == 1):
                        tempHeader.append(row[i])
                    else:
                        tempData.append(row[i])
    tempHeader.append('$ per Sq. Ft')
    tempData.append(int(re.sub(r'\D', "", tempData[4])) / tempData[3])
    addData(tempHeader, 0)
    addData(tempData, 1)

def concatenateValueHistory(df):
    df = pandas.concat(df)
    df = df.loc[~df.index.duplicated(keep='first')]
    df = df.iloc[2:]
    tempValueHeaders = []
    valueHeaders = []
    valueData = []
    for row in df.itertuples():
        for i in range(2, 10):
            if row[0] == 2:
                tempValueHeaders.append(str(row[i]) + ' - ')
            else:
                valueData.append(row[i])
        if not(row[0] == 2):
            for header in tempValueHeaders:
                        valueHeaders.append(header + str(row[1]))
    addData(valueHeaders, 0)
    addData(valueData, 1)
            

class WebDriver(webdriver.Chrome):
    def __init__(self, headless):
        options = Options()
        if (headless == False):
            options.add_argument("--start-maximized")
        else:
            options.headless = headless
        self.driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=options)
        self.driver.implicitly_wait(1)
    
    def quit(self):
        self.driver.quit()
        print ("Driver exited successfully.\n")
    
    def loadWebsite(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            self.quit()
            print("Error loading website {}.. \n".format(url) + str(e))

    def loadProperty(self, propertyNumber):
        try:
            elem = self.driver.find_element_by_xpath("//div/input[@name='searchTerms']")
            elem.click()
            elem.send_keys(propertyNumber)
            self.driver.find_element_by_xpath("//span/button[@id='searchsubmit']").click()
            self.driver.find_element_by_xpath("//td[contains(text(), '{}')]".format(propertyNumber)).click()
        except Exception as e:
            self.quit()
            print("Error loading property {}.. \n".format(property) + str(e))

    def grabPropertyHeader(self, propertyNumber):
        try:
            propertyOwner = self.driver.find_element(by=By.XPATH, value="//div[@class='divOwnersLabel']").text
            propertyAddress = self.driver.find_element(by=By.XPATH, value="//tr/td[contains(@id, 'PropertyAddress')]").text
            propertyAssessedValue = self.driver.find_element(by=By.XPATH, value="//tr/td[contains(@id, 'TotalAssessedValue')]").text
            addData(['Property Number','Owner','Address','Assessed Value'], 0)
            addData([propertyNumber, propertyOwner, propertyAddress, propertyAssessedValue], 1)
        except Exception as e:
            self.quit()
            print("Error grabbing property header.. \n" + str(e))

    def grabTableInformation(self, propertyNumber):
        try:
            # General Information
            try:
                generalInformationTable = self.driver.find_element(by=By.XPATH, value="//table[@id='tblGeneralInformation']").get_attribute('outerHTML')
                df = pandas.read_html(generalInformationTable)
                concatenateTable(df)
            except Exception as ee:
                self.quit()
                print("Error grabbing general information.. \n" + str(ee))
            # Owner Information
            ownerInformation = self.driver.find_element(by=By.XPATH, value="//table[@id='tblOwnerInformation']").get_attribute('outerHTML')
            df1 = pandas.read_html(ownerInformation)
            concatenateTable(df1)
            # Value Information
            valueInformation = self.driver.find_element(by=By.XPATH, value="//table[@id='dnn_ctr377_View_tblValueInfoRP']").get_attribute('outerHTML')
            df2 = pandas.read_html(valueInformation)
            concatenateTable(df2)
            try: 
                # //tbody/tr/td[contains(text(), 'IMPROVEMENTS')]
                # Improvement Table Part 1
                improvementTable = self.driver.find_element(by=By.XPATH, value="//table[@class='improvementTable']").get_attribute('outerHTML')
                df5 = pandas.read_html(improvementTable)     
                concatenateImprovementHeader(df5)

                improvementTableRecords = self.driver.find_element(by=By.XPATH, value="//div[@id='dnn_ctr377_View_divCamaInfo']/ul/li/div/table").get_attribute('outerHTML')
                df6 = pandas.read_html(improvementTableRecords)
                df = pandas.concat(df6)

                tableHeaders = self.driver.find_element(by=By.XPATH, value="//div[@id='dnn_ctr377_View_divCamaInfo']/ul/li/div/table/tbody/tr/td/table").get_attribute('outerHTML')
                df7 = pandas.read_html(tableHeaders)
                firstImprovement(df7)
            except NoSuchElementException:
                # fill data
                addData(Homesite_Headers_Data_1, 1)
                addData(Homesite_Tables_Data_2, 1)
                return 
            # Value History
            valueHistory = self.driver.find_element(by=By.XPATH, value="//table[@id='dnn_ctr377_View_tblValueHistoryRP']").get_attribute('outerHTML')
            df3 = pandas.read_html(valueHistory)
            concatenateValueHistory(df3)
            # Grab Total Acreage
            totalAcreage = self.driver.find_element(by=By.XPATH, value="//tr/td[contains(text(),'Sq. ft /')]").get_attribute('innerHTML')
            addData(['Total Acreage'], 0) 
            addData([totalAcreage], 1)
            #print(totalAcreage)
            # Land Segments
            landSegments = self.driver.find_element(by=By.XPATH, value="//table[@id='dnn_ctr377_View_tblLandSegments']").get_attribute('outerHTML')
            df4 = pandas.read_html(landSegments)
            concatenateLandSegments(df4)
            
        except Exception as e:
            self.quit()
            f = open("Error.txt", "a")
            f.write("Error grabbing property header.. {} .. \n".format(propertyNumber) + str(e) + '\n')
            f.close()

headless = True
counter = 0
propertyCounter = 1
def scrapeProperties(propertyNumber):
    global EXCEL_DATA, EXCEL_HEADERS, counter
    EXCEL_HEADERS = []
    EXCEL_DATA = []
    wd = WebDriver(headless)
    url = "https://esearch.mcad-tx.org/Property-Detail?PropertyQuickRefID={}".format(propertyNumber)
    wd.loadWebsite(url)
    #wd.loadProperty(propertyNumber)
    wd.grabPropertyHeader(propertyNumber)
    wd.grabTableInformation(propertyNumber)
    wd.quit()
    with open("OffsetProperty.csv", "a") as infile:
        writer = csv.writer(infile)
        if(counter == 0):
            writer.writerow(EXCEL_HEADERS)    #Write Header
            counter +=1
        writer.writerow(EXCEL_DATA)       #Write Content

with open("OffsetProps.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        scrapeProperties(line)
        print("Property Counter: " + str(propertyCounter))
        propertyCounter += 1


#propertyNumber = 'R260241'
    

#print(len(EXCEL_HEADERS))
#print(len(EXCEL_DATA))
# print((EXCEL_HEADERS))
# print((EXCEL_DATA))