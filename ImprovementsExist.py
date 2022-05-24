#try:
                 #########################
                 # WITHOUT IMPROVEMENTS
                # //tbody/tr/td[contains(text(), 'IMPROVEMENTS')]
                # Improvement Table Part 1
            if 'IMPROVEMENTS' in self.driver.page_source:
                improvementTable = self.driver.find_element(by=By.XPATH, value="//table[@class='improvementTable']").get_attribute('outerHTML')
                df5 = pandas.read_html(improvementTable)     
                concatenateImprovementHeader(df5)

                improvementTableRecords = self.driver.find_element(by=By.XPATH, value="//div[@id='dnn_ctr377_View_divCamaInfo']/ul/li/div/table").get_attribute('outerHTML')
                df6 = pandas.read_html(improvementTableRecords)
                df = pandas.concat(df6)

                tableHeaders = self.driver.find_element(by=By.XPATH, value="//div[@id='dnn_ctr377_View_divCamaInfo']/ul/li/div/table/tbody/tr/td/table").get_attribute('outerHTML')
                df7 = pandas.read_html(tableHeaders)
                firstImprovement(df7)
            else:
                tempHeader = ['Improvement #1', 'State Code', 'Homesite', 'Total Main Area (Exterior Measured)', 'Market Value', 'Record', 'Type', 'Year Built', 'Sq. Ft', 'Value', 'Class', 'Bedrooms', 'Flooring', 'Eff. Year Built',
                    'Baths (Full, ½, ¾)', 'Foundation', 'Adjustment %', 'Heat and AC', 'Int. Finish', 'Roof Style', 'Fireplaces', 'Ext. Finish']
                tempData = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                addData(tempHeader, 0)
                addData(tempData, 1)
            #except NoSuchElementException:
                # fill data
                #addData(Homesite_Headers_Data_1, 1)
                #addData(Homesite_Tables_Data_2, 1)
                #return 


#With IMprovements
########################################
# Check if improvement table exists then exit if not
            # "//table[@class='improvementTable']"
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


#######################
# ORIGINAL
df.drop(['2022 GENERAL INFORMATION', 'Property Status', 'Property Type', 'Neighborhood', 'Account', 'Map Number', '2022 OWNER INFORMATION', 'Owner Name', 'Owner ID',
'Exemptions', 'Percent Ownership', 'Mailing Address', 'Agent', 'Agricultural Use', 'Timber Use', 'State Code', 'Homesite', 'Type', 'Bedrooms', 'Flooring', 'Baths (Full, ½, ¾)', 'Int. Finish',
'IMPROVEMENT - 2021', 'LAND - 2021', 'MARKET - 2021', 'AG MARKET - 2021', 'AG USE - 2021', 'APPRAISED - 2021', 'HS CAP LOSS - 2021', 'ASSESSED - 2021', 'IMPROVEMENT - 2020',
 'LAND - 2020', 'MARKET - 2020', 'AG MARKET - 2020', 'AG USE - 2020', 'APPRAISED - 2020', 'HS CAP LOSS - 2020', 'ASSESSED - 2020', 'IMPROVEMENT - 2019',
 'LAND - 2019', 'MARKET - 2019', 'AG MARKET - 2019', 'AG USE - 2019', 'APPRAISED - 2019', 'HS CAP LOSS - 2019', 'ASSESSED - 2019', 'IMPROVEMENT - 2018',
 'LAND - 2018', 'MARKET - 2018', 'AG MARKET - 2018', 'AG USE - 2018', 'APPRAISED - 2018', 'HS CAP LOSS - 2018', 'ASSESSED - 2018', 'IMPROVEMENT - 2017',
 'LAND - 2017', 'MARKET - 2017', 'AG MARKET - 2017', 'AG USE - 2017', 'APPRAISED - 2017', 'HS CAP LOSS - 2017', 'ASSESSED - 2017', '1 - Front Acreage - LAND SEGMENT TYPE',
  '1 - Front Acreage - STATE CODE', '1 - Front Acreage - HOMESITE', '1 - Front Acreage - MARKET VALUE', '1 - Front Acreage - AG USE', '1 - Front Acreage - TIM USE',
   '2 - Secondary Acreage - LAND SEGMENT TYPE', '2 - Secondary Acreage - STATE CODE', '2 - Secondary Acreage - HOMESITE', '2 - Secondary Acreage - MARKET VALUE', '2 - Secondary Acreage - AG USE',
    '2 - Secondary Acreage - TIM USE', '3 - LAND SEGMENT TYPE', '3 - STATE CODE', '3 - HOMESITE', '3 - MARKET VALUE', '3 - AG USE', '3 - TIM USE', '4 - LAND SEGMENT TYPE',
     '4 - STATE CODE', '4 - HOMESITE', '4 - MARKET VALUE', '4 - AG USE', '4 - TIM USE', 'Land Segments Totals'], axis=1, inplace=True)



     #####################
     # FOR PROPERTIES WITH OFFSET
     df.drop(['2022 GENERAL INFORMATION', 'Property Status', 'Property Type', 'Neighborhood', 'Account', 'Map Number', '2022 OWNER INFORMATION', 'Owner Name', 'Owner ID',
'Exemptions', 'Percent Ownership', 'Mailing Address', 'Agent', 'Agricultural Use', 'Timber Use', 'State Code', 'Homesite', 'Type', 'Bedrooms', 'Flooring', 'Baths (Full, ½, ¾)', 'Int. Finish',
'IMPROVEMENT - 2021', 'LAND - 2021', 'MARKET - 2021', 'AG MARKET - 2021', 'AG USE - 2021', 'APPRAISED - 2021', 'HS CAP LOSS - 2021', 'ASSESSED - 2021', 'IMPROVEMENT - 2020',
 'LAND - 2020', 'MARKET - 2020', 'AG MARKET - 2020', 'AG USE - 2020', 'APPRAISED - 2020', 'HS CAP LOSS - 2020', 'ASSESSED - 2020', 'IMPROVEMENT - 2019',
 'LAND - 2019', 'MARKET - 2019', 'AG MARKET - 2019', 'AG USE - 2019', 'APPRAISED - 2019', 'HS CAP LOSS - 2019', 'ASSESSED - 2019', 'IMPROVEMENT - 2018',
 'LAND - 2018', 'MARKET - 2018', 'AG MARKET - 2018', 'AG USE - 2018', 'APPRAISED - 2018', 'HS CAP LOSS - 2018', 'ASSESSED - 2018', 'IMPROVEMENT - 2017',
 'LAND - 2017', 'MARKET - 2017', 'AG MARKET - 2017', 'AG USE - 2017', 'APPRAISED - 2017', 'HS CAP LOSS - 2017', 'ASSESSED - 2017', '1 - Front Acreage - LAND SEGMENT TYPE',
  '1 - Front Acreage - STATE CODE', '1 - Front Acreage - HOMESITE', '1 - Front Acreage - MARKET VALUE', '1 - Front Acreage - AG USE', '1 - Front Acreage - TIM USE',
     '2 - LAND SEGMENT TYPE', '2 - STATE CODE', '2 - HOMESITE', '2 - MARKET VALUE', '2 - AG USE', '2 - TIM USE', '3 - LAND SEGMENT TYPE', '3 - STATE CODE', '3 - HOMESITE', '3 - MARKET VALUE', '3 - AG USE', '3 - TIM USE', '4 - LAND SEGMENT TYPE',
     '4 - STATE CODE', '4 - HOMESITE', '4 - MARKET VALUE', '4 - AG USE', '4 - TIM USE'], axis=1, inplace=True)
