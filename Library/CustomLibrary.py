from robot.libraries.BuiltIn import BuiltIn
from dateutil.relativedelta import *
from selenium import webdriver
import time
import calendar
from datetime import datetime, time, date, timedelta
from datetime import datetime
from datetime import date
import datetime
from robot.api.deco import keyword

import os
import time
import xlrd
import traceback
                
class CustomLibrary(object):

        def __init__(self):
                pass
        
        def get_future_date(self,datediff):
                date_month = date.today() + relativedelta(months=+datediff)
                return date_month.strftime("%d")
        
        def get_date_subtract_from_current_date(self,datediff):
                sub_date = date.today() -timedelta(datediff)
                return sub_date.strftime("%d-%b-%Y")
        
        def get_month_subtract_from_current_month(self,datediff):
                sub_month = date.today() + relativedelta(months=-datediff)
                return sub_month.strftime("%d-%b-%Y")
        
        def get_past_date(self,datediff):
                date_month = date.today() + relativedelta(months=-datediff)
                return date_month.strftime("%d")
        
        def get_month_last_date(self,year,month):
               lastdate = calendar.monthrange(year,month)
               return lastdate
        
        def do_get_current_date(self):
                date_month = datetime.datetime.now().day
                return date_month

        def get_ms_excel_row_values_into_dictionary_based_on_key(self,filepath,keyName,sheetName=None):
            """Returns the dictionary of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            dictVar={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return dictVar
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            dictVar={}
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                rowValues=worksheet.row_values(int(rowNo))
                if str(rowValues[0])!=str(keyName):
                    continue
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    cell_data=self.get_unique_test_data(cell_data)
                
                    dictVar[str(headersList[rowIndex])]=str(cell_data)
            return dictVar

        def get_all_ms_excel_row_values_into_dictionary(self,filepath,sheetName=None):
            """Returns the dictionary of values all row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            all_row_dict={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return all_row_dict
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                each_row_dict={}
                rowValues=worksheet.row_values(int(rowNo))
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    if(str(cell_data)=="" or str(cell_data)==None):
                        continue
                    cell_data=self.get_unique_test_data(cell_data)
                    each_row_dict[str(headersList[rowIndex])]=str(cell_data)
                all_row_dict[str(rowValues[0])]=each_row_dict
            return all_row_dict

        def get_unique_test_data(self,testdata):
            """Returns the unique if data contains unique word """
            faker = BuiltIn().get_library_instance('FakerLibrary')
            unique_string=faker.random_number(5,True)
            unique_string=str(unique_string)
            testdata=testdata.replace("UNIQUE",unique_string)
            testdata=testdata.replace("Unique",unique_string)
            testdata=testdata.replace("unique",unique_string)
            return testdata

        def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
            """Returns the True if the specified work sheets exist in the specifed MS Excel file else False"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            sStatus=False        
            if sheetName==None:
                return True
            else:
                for sname in snames:
                    if sname.lower()==sheetName.lower():
                        wsname=sname
                        sStatus=True
                        break
                if sStatus==False:
                    print ("Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: " +str(filepath))
            return sStatus

        def compare_time(self,actualhr,actualmins,expectedhr,expectedmins):
                datetime.fromtimestamp(actualhr).strftime('%I')
                datetime.fromtimestamp(actualmins).strftime('%M')
                datetime.fromtimestamp(expectedhr).strftime('%I')
                datetime.fromtimestamp(expectedmins).strftime('%M')
                t1 = datetime.time(actualhr, actualmins, 0)
                t2 = datetime.time(expectedhr, expectedmins, 0)
                if t1 > t2:
                  return True
                else:
                  return False

        def do_get_current_month_last_date(self):
               current_date = date.today()
               current_year= current_date.strftime("%Y")
               current_month = current_date.strftime("%m")
               lastdate = calendar.monthrange((int(current_year)),(int(current_month)))
               return lastdate[1]        

        def do_get_next_month_last_date(self):
               future_date = date.today() + timedelta(1)
               future_year= future_date.strftime("%Y")
               future_month = future_date.strftime("%m")
               lastdate = calendar.monthrange((int(future_year)),(int(future_month)))
               return lastdate[1]

        def get_next_month_no(self):
                date_month = date.today() + relativedelta(months=+1)
                month_no = int(date_month.strftime("%m"))
                return month_no
        
        def get_month_first_date(self,year,month):
               firstdate = calendar.monthrange(year,month)
               return firstdate

        def do_get_past_date_from_currentdate(self,datediff):
                """Returns the past date with format (01) """
                past_date = date.today() -timedelta(datediff)
                return past_date.strftime("%d")

        def do_get_past_date_from_previous_month(self,datediff):
                """Returns the past month date with format (01) """
                sub_month = date.today() + relativedelta(months=-datediff)
                past_date = sub_month -timedelta(1)
                return past_date.strftime("%d")

        def do_get_past_month_date(self,datediff):
                """Returns the past month with format (01/01/2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                return sub_month.strftime("%d")
        
        def do_get_past_month_lastdate(self,datediff):
                """Returns the past month with format (day=31) """
                sub_month = date.today() + relativedelta(months=-datediff)
                return sub_month.strftime("%d/%m")

        def do_get_previous_month_first_day(self,datediff):
                """Returns the first day of previous month with format (01/01/2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                first_day = sub_month.replace(day=1)
                return first_day.strftime("%d/%m/%Y")
        
        def do_get_previous_month(self):
                today = datetime.date.today()
                first = today.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                previous_month = lastMonth.strftime("%B")
                return previous_month
        
        def do_get_previous_short_month(self):
                today = datetime.date.today()
                first = today.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                previous_month = lastMonth.strftime("%b")
                return previous_month

        def do_get_current_month_date_now(self):
                date_month = date.today()
                date_monthnow = date_month.strftime("%d %b %Y")
                return date_monthnow
        
        def do_get_Previous_ShortMonth_currentYear(self):
                today = datetime.date.today()
                first = today.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                previous_month = lastMonth.strftime("%b %Y")
                return previous_month

        def do_get_first_monday_of_current_month(self):
                """Returns the first monday of current month with format (01) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.MONDAY - month_range[0]) % 7
                first_monday = date_corrected+datetime.timedelta(days = delta)
                return first_monday.strftime("%d")

        def do_get_first_monday_of_current_month(self):
                """Returns the first monday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.MONDAY - month_range[0]) % 7
                first_monday = date_corrected+datetime.timedelta(days = delta)
                return first_monday.strftime("%d/%m/%Y")
        
        def do_get_april_month_first_date(self):
                """Returns the first day of previous month with format (%d/%b/%Y) """
                sub_month = date.today() + relativedelta(months=+1)
                today = datetime.date.today()
                first = today.replace(day=1)
                sub_month = first + relativedelta(months=+1) + relativedelta(years=-1)
                return sub_month.strftime("%d %b %Y")

        def do_get_september_month_last_day(self,datediff):
                """Returns the last day of previous month with format (%d/%b/%Y) """
                sub_month = date.today() + relativedelta(months=-datediff)
                today = datetime.date.today()
                first = today.replace(day=28)
                sub_month = first + relativedelta(months=-datediff)
                final_sum_month=sub_month.replace(day=30)
                return final_sum_month.strftime("%d %b %Y")

        def do_get_current_year_future_month_last_day(self,datediff):
                """Returns the last day of future month with format (%d %b %Y) """
                today = datetime.date.today()
                current_date = date.today()
                current_year= current_date.strftime("%Y")
                sub_month = date.today() + relativedelta(months=-datediff)
                first = today.replace(day=31)
                sub_month = first + relativedelta(months=-datediff)
                return sub_month.strftime("%d %b %Y")

        def do_get_first_tuesday_of_current_month(self):
                """Returns the first tuesday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.TUESDAY - month_range[0]) % 7
                first_monday = date_corrected+datetime.timedelta(days = delta)
                return first_monday.strftime("%d/%m/%Y")

        def do_get_previous_month_last_day(self,datediff):
                """Returns the first day of previous month with format (01/01/2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                last_day = sub_month.replace(day=30)
                return last_day.strftime("%d")

        def do_get_first_sunday_of_current_month(self):
                """Returns the first sunday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.SUNDAY - month_range[0]) % 7
                first_sunday = date_corrected+datetime.timedelta(days = delta)
                return first_sunday.strftime("%d")

        def do_get_first_friday_of_current_month(self):
                """Returns the first friday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                month_number,month_days = month_range
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.FRIDAY - month_range[0]) % 7
                number = month_days - delta
                first_friday = date_corrected+datetime.timedelta(days = delta)
                return first_friday.strftime("%d")

        def do_get_current_month_first_day(self):
                """Returns the first day of previous month with format (01/01/2020) """
                sub_month = date.today()
                first_day = sub_month.replace(day=1)
                return first_day.strftime("%d/%m/%Y")

        def do_get_first_monday_of_next_month(self):
                """Returns the first tuesday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                month_number,month_days = month_range
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.MONDAY - month_range[0]) % 7
                number = month_days - delta
                first_monday = date_corrected+datetime.timedelta(days = delta)+datetime.timedelta(days = number+2)
                return first_monday.strftime("%d/%m/%Y")

        def do_get_next_month_first_monday(self,year,month,date):
                d = datetime.date(year,month,date)
                next_monday = self.next_weekday(d, 0)
                monday_date = next_monday.strftime("%d %b %Y")
                return monday_date

        def do_get_next_month_first_monday_d(self,year,month,date):
                d = datetime.date(year,month,date)
                next_monday = self.next_weekday(d, 0)
                monday_date = next_monday.strftime("%d")
                return monday_date

        def do_get_tuesday_following_friday_of_current_month(self):
                """Returns the tuesday following first friday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.FRIDAY - month_range[0]) % 7
                first_friday = date_corrected+datetime.timedelta(days = delta)
                tuesday = first_friday + timedelta(days=4)
                return tuesday.strftime("%d %m")

        def do_get_monday_following_friday_of_current_month(self):
                """Returns the first friday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.FRIDAY - month_range[0]) % 7
                first_friday = date_corrected+datetime.timedelta(days = delta)
                monday = first_friday + timedelta(days=3)
                return monday.strftime("%d")
        
        def do_get_all_monday_of_previous_month_base_on_weekdaylimt(self,weekday):
                """Returns the first monday of current month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                month_number,month_days = month_range
                date_corrected = datetime.date(int(year),int(month),1) 
                delta_range = (calendar.MONDAY - month_range[0]) % 7
                delta = (calendar.MONDAY - month_range[0]) % int(weekday)
                number = month_days + delta_range
                previous_month_first_monday = date_corrected+datetime.timedelta(days = delta) + datetime.timedelta(days = -number+4)
                return previous_month_first_monday.strftime("%d/%m/%Y")

        def next_weekday(self,d,weekday):
                days = weekday - d.weekday()
                if days <= 0:
                    days += 7
                return d + datetime.timedelta(days)

        def do_get_next_month_first_monday_date(self,year,month,date):
                d = datetime.date(year,month,date)
                next_monday = self.next_weekday(d, 0)
                monday_day = next_monday.strftime("%d/%m/%Y")
                return monday_day
                
        def do_get_next_month_first_monday(self,year,month,date):
                d = datetime.date(year,month,date) 
                next_monday = self.next_weekday(d, 0)
                monday_date = next_monday.strftime("%d %b %Y")
                return monday_date

        def do_get_next_month_first_monday_d(self,year,month,date):
                d = datetime.date(year,month,date)
                next_monday = self.next_weekday(d, 0)
                monday_date = next_monday.strftime("%d")
                return monday_date
        
        def do_get_current_year_dec_last_day(self):
                date_result=date(date.today().year, 12, 31)
                return date_result.strftime("%d %b %Y")

        def do_get_future_date_from_currentdate(self,datediff):
                """Returns the past date with format (01) """
                past_date = date.today() +timedelta(datediff)
                return past_date.strftime("%d/%m/%Y")
        
        def do_get_past_longdate_from_currentdate(self,datediff):
                """Returns the past date with format (01) """
                past_date = date.today() -timedelta(datediff)
                return past_date.strftime("%d/%m/%Y")

        def get_punch_in_out_time(self,intime):
                act_time = intime.split(':')
                min_list = act_time[1].split(' ') 
                design = min_list[1]
                hour = int(act_time[0])+1
                if int(act_time[0]) == 11 and min_list[1] == 'PM':
                    design = 'AM'
                    print(design)
                if int(act_time[0]) == 11 and min_list[1] == 'AM':
                    design = 'PM'
                    print(design)
                added_time =  str(hour)+":"+str(min_list[0])+" "+design
                return added_time

        def get_punch_in_minus_2hours_time(self,intime):
                act_time = intime.split(':')
                min_list = act_time[1].split(' ') 
                design = min_list[1]
                hour = int(act_time[0])-2
                if int(act_time[0]) == 12 and min_list[1] == 'PM':
                    design = 'AM'
                    print(design)
                if int(act_time[0]) == 12 and min_list[1] == 'AM':
                    design = 'PM'
                    print(design)
                minus_time =  str(hour)+":"+str(min_list[0])+" "+design
                return minus_time

        def open_chrome_browser(self,url,filepath):
            selenium = BuiltIn().get_library_instance('SeleniumLibrary')
            try:
                options = webdriver.ChromeOptions()
                chrome_options = webdriver.ChromeOptions()
                options.add_experimental_option('prefs', {
                    'download': {
                    'default_directory': filepath
                   },
                    'credentials_enable_service': False,
                    'profile': {
                    'password_manager_enabled': False,
                    'default_content_settings': {
                    'popups':0
                    }
                    }
                    })
                options.add_experimental_option("excludeSwitches",["enable-automation","load-extension"])
                selenium.create_webdriver('Chrome',chrome_options=options)
                selenium.go_to(url)
                return True
            except:
                return False
  
        def do_get_previous_month_date_with_year_from_currentdate(self):
                today = datetime.date.today()
                first = today.replace(day=1)
                lastMonth = first - datetime.timedelta(days=1)
                previous_month = lastMonth.strftime("%d/%m/%Y")
                return previous_month

        def do_get_deduct_days_from_current_date(self,datediff):
                """Returns the past date with format (01) """
                past_date = date.today() -timedelta(datediff)
                return past_date.strftime("%d/%B/%Y")

        def do_get_past_date_from_currentdate_date(self,datediff):
                """Returns the past date with format (Tue, 17-Mar-2020) """
                past_date = date.today() -timedelta(datediff - 1) 
                return past_date.strftime("%a, %d-%b-%Y")

        def do_get_past_date_from_previous_month_date(self,datediff):
                """Returns the past month date with format (Tue, 17-Mar-2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                past_date = sub_month -timedelta(1)
                return past_date.strftime("%a, %d-%b-%Y")

        def do_get_previous_month_full_date(self,datediff):
                """Returns the past month with format (01/01/2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                return sub_month.strftime("%d-%b-%y")

        def do_get_past_date_from_currentdate_date(self,datediff):
                """Returns the past date with format (Tue, 17-Mar-2020) """
                past_date = date.today() -timedelta(datediff - 1) 
                return past_date.strftime("%a, %d-%b-%Y")

        def do_get_past_month_last_day(self,datediff):
                """Returns the last day of future month with format (%d %b %Y) """
                today = datetime.date.today()
                current_date = date.today()
                current_year= current_date.strftime("%Y")
                sub_month = date.today() + relativedelta(months=-datediff)
                first = today.replace(day=31)
                sub_month = first + relativedelta(months=-datediff)
                return sub_month.strftime("%a, %d-%b-%Y")

        def do_get_past_month_first_day(self,datediff):
                """Returns the first day of previous month with format (01/01/2020) """
                sub_month = date.today() + relativedelta(months=-datediff)
                first_day = sub_month.replace(day=1)
                return first_day.strftime("%d-%b-%y")

        def do_get_past_date_from_current_date_minus_xdays(self,datediff):
                """Returns the past date with format (01-Feb-20) """
                past_date = date.today() -timedelta(datediff - 1) 
                return past_date.strftime("%d-%b-%y")

        def do_get_tuesday_following_monday_of_future_month(self):
                """Returns the tuesday following first monday of future month with format (01/01/2020) """
                current_date = date.today()
                year = current_date.strftime("%Y")
                month = current_date.strftime("%m")
                month_range = calendar.monthrange(int(year),int(month))
                month_number,month_days = month_range
                date_corrected = datetime.date(int(year),int(month),1)
                delta = (calendar.MONDAY - month_range[0]) % 7
                number = month_days - delta
                first_monday = date_corrected+datetime.timedelta(days = delta)+datetime.timedelta(days = number)
                tuesday = first_monday + timedelta(days=4)
                return tuesday.strftime("%d")

        def do_get_future_date_from_currentdate_Short(self,datediff):
                """Returns the past date with format (01) """
                past_date = date.today() +timedelta(datediff)
                return past_date.strftime("%d")


        
        
        



              




        
 
        




        

        
        

