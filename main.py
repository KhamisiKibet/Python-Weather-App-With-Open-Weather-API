#####
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
import platform
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback

from datetime import datetime
import json
import requests
import urllib
from urllib.parse import urlencode
########################################################################
## 
########################################################################

# #########################
# IMPORT GUI FILE
from ui_mainwindow import *
# ##########################

# #########################
# GLOBAL VALUES
FINAL_WEATHER_ERROR = "none" #used to hold a variable that helps the app determine where an error occured while loading the app



########################################################################
## WORKER SIGNAL CLASS
########################################################################
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

########################################################################
## 
########################################################################


########################################################################
## WORKER  CLASS
########################################################################
class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


########################################################################
## 
########################################################################




########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # HIDE PROGRESSBAR AND MESSAGES CONTAINER BY DEFAULT
        self.ui.progressBar.setVisible(False)
        self.ui.message_frame.hide()


        #######################################################################
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## == ##


        # START THREAD
        self.threadpool = QThreadPool()


        ########################################################################
        ## UPDATE COUNTRIES ON CONTINENT CHANGE
        ########################################################################
        self.ui.continents_list.currentTextChanged.connect(lambda: self.weather_thread("countries"))


        ########################################################################
        ## UPDATE CITIES ON COUNTRIES CHANGE
        ########################################################################
        self.ui.countries_list.currentTextChanged.connect(lambda: self.weather_thread("cities"))

        ########################################################################
        ## UPDATE WEATHER ON CITY CHANGE
        ########################################################################
        self.ui.cities_list.currentTextChanged.connect(lambda: self.weather_thread("weather"))


        ########################################################################
        ## RELOAD WEATHER
        ########################################################################
        # self.ui.retryButton.clicked.connect(lambda: self.reload_weather)
        self.ui.retryButton.pressed.connect(self.reload_weather)








        self.weather_thread("weather")





    ########################################################################
    ## CREATE WEATHER THREAD FUNCTION 
    ########################################################################
    def weather_thread(self, request):
        print("Requested", request)
        # DISABLE LIST ITEMS TO AVOID MULTIPLE REQUESTS
        self.ui.continents_list.setEnabled(False)
        self.ui.countries_list.setEnabled(False)
        self.ui.cities_list.setEnabled(False)
        #
        # DISPLAY PROGRESS BAR
        self.ui.progressBar.show()
        # 
        # Hide messsage container
        self.ui.message_frame.hide()
        
        global FINAL_WEATHER_ERROR;
        # Pass the function to execute
        if request == "continents":
            # Update final error
            FINAL_WEATHER_ERROR = "continents"
            # UPDATE CONTINENTS
            worker = Worker(self.update_continents)
        elif request == "countries":
            # Update final error
            FINAL_WEATHER_ERROR = "countries"
            # UPDATE COUNRIES
            worker = Worker(self.update_countries)
        elif request == "cities":
            # Update final error
            FINAL_WEATHER_ERROR = "cities"
            # UPDATE CITIES
            worker = Worker(self.upadate_cities)
        elif request == "weather":
            # Update final error
            FINAL_WEATHER_ERROR = "weather"
            # UPDATE WEATHER
            worker = Worker(self.get_weather)
        else:
            # DISABLE LIST ITEMS (Invalid request)
            self.ui.continents_list.setEnabled(True)
            self.ui.countries_list.setEnabled(True)
            self.ui.cities_list.setEnabled(True)
            self.ui.progressBar.hide()
            return


        # START WORKER
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    ########################################################################
    ## 
    ########################################################################

    ########################################################################
    ## WORKER PRINT OUT
    ########################################################################
    def print_output(self, s):
        print(s)
    ########################################################################
    ## 
    ########################################################################

    ########################################################################
    ## WORKER THREAD COMPLETE FUNCTION
    ########################################################################
    def thread_complete(self):
        print("THREAD COMPLETE!")
    ########################################################################
    ## 
    ########################################################################



    ########################################################################
    ## WORKER THREAD PROGRESS FUNCTION
    ########################################################################
    def progress_fn(self, n):
        # n = progress value
        print("%d%% done" % n)
        # set progress value to progress bar
        self.ui.progressBar.setValue(n)

        if n < 100:
            # disable list items and show progressbar while progress is less than 100
            self.ui.continents_list.setEnabled(False)
            self.ui.countries_list.setEnabled(False)
            self.ui.cities_list.setEnabled(False)
            self.ui.progressBar.show()
        else:
            # enable list items and hide progressbar  if progress is 100
            self.ui.continents_list.setEnabled(True)
            self.ui.countries_list.setEnabled(True)
            self.ui.cities_list.setEnabled(True)
            self.ui.progressBar.hide()
    ########################################################################
    ## 
    ########################################################################






    ########################################################################
    ## A FUNCTION TO UPDATE CONTINENTS
    ########################################################################
    def update_continents(self, progress_callback):
        # Update location label
        self.ui.weather_location.setText("Fetching continents list...")
        # GET GLOBAL VARIABLE
        global FINAL_WEATHER_ERROR
        FINAL_WEATHER_ERROR = "continents" #if an error occurs when loading continents, resume from this function

        # CATCH NETWORK ERROR USING TRY CATCH METHOD
        try:
            url = 'https://parseapi.back4app.com/classes/Continent?order=name'
            headers = {
                'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja', # This is the fake app's application id
                'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH' # This is the fake app's readonly master key
            }
            data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
            # print(json.dumps(data, indent=2))

            ########################################################################
            ## CLEAR CONTINENTS LIST BEFORE UPDATING
            ########################################################################
            self.ui.continents_list.clear()

            #######################################################################
            # ADD CONTIENTS TO LIST
            #######################################################################
            for continents in data['results']:

                self.ui.continents_list.addItem(continents['name'], continents['objectId'])
                print(continents['name'], continents['objectId']) 


            else:
                # Select first list item after list update
                self.ui.countries_list.setCurrentIndex(0)
                # UPDATE WORKER PROGRESS
                WEATHER_WORKER_PROGRESS_VALUE = 1
                progress_callback.emit(WEATHER_WORKER_PROGRESS_VALUE*25)

        except Exception as e:
            print(e)
            self.alert(e)

    ########################################################################
    ## 
    ########################################################################



    ########################################################################
    ## A FUNCTION TO UPDATE COUNTRIES USING CONTINENT ID
    ########################################################################
    def update_countries(self, progress_callback):
        # Update location label
        self.ui.weather_location.setText("Fetching countries list...")
        # GET GLOBAL VARIABLE
        global FINAL_WEATHER_ERROR
        FINAL_WEATHER_ERROR = "countries" #if an error occurs when loading continents, resume from this function

        ########################################################################
        ## GET CONTINENT ID FROM LIST
        ########################################################################
        continent_id = self.ui.continents_list.currentData() #id will be used to fetch countries

        # print(continent_id)

        try:
            where = urllib.parse.quote_plus("""
            {
                "continent": {
                    "__type": "Pointer",
                    "className": "Continent",
                    "objectId": "%s"
                }
            }
            """ % (continent_id) )
            url = 'https://parseapi.back4app.com/classes/Country?order=name&where=%s' % where
            headers = {
                'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja', # This is the fake app's application id
                'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH' # This is the fake app's readonly master key
            }
            data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
            # print(json.dumps(data, indent=2))

            ########################################################################
            ## CLEAR COUNTRIES LIST BEFORE UPDATING
            ########################################################################
            self.ui.countries_list.clear()

            ########################################################################
            ## UPDATE COUNTRIES LIST
            ########################################################################
            for countries in data['results']:
                self.ui.countries_list.addItem(countries['name'], countries['objectId'])
            else:
                # Select first list item after list update
                self.ui.countries_list.setCurrentIndex(0)
                # UPDATE WORKER PROGRESS
                WEATHER_WORKER_PROGRESS_VALUE = 2
                progress_callback.emit(WEATHER_WORKER_PROGRESS_VALUE*25)

        except Exception as e:
            print(e)
            self.alert(e)


    ########################################################################
    ## 
    ########################################################################


    ########################################################################
    ## A FUNCTION TO UPDATE COUNTRY CITIES
    ########################################################################
    def upadate_cities(self, progress_callback):
        # Update location label
        self.ui.weather_location.setText("Fetching cities list...")
        # GET GLOBAL VARIABLE
        global FINAL_WEATHER_ERROR
        FINAL_WEATHER_ERROR = "cities" #if an error occurs when loading continents, resume from this function

        ########################################################################
        ## GET COUNTRY ID
        ########################################################################
        country_id = self.ui.countries_list.currentData() 
        # print(country_id)

        try:
            where = urllib.parse.quote_plus("""
            {
                "country": {
                    "__type": "Pointer",
                    "className": "Country",
                    "objectId": "%s"
                }
            }
            """ % (country_id))

            url = 'https://parseapi.back4app.com/classes/City?order=name&where=%s' % where
            headers = {
                'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja', # This is the fake app's application id
                'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH' # This is the fake app's readonly master key
            }
            data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
            # print(json.dumps(data, indent=2))

            ########################################################################
            ## CLEAR CITIES LIST BEFORE UPDATING
            ########################################################################
            self.ui.cities_list.clear()

            ########################################################################
            ## UPDATE CITIES LIST
            ########################################################################        
            for cities in data['results']:
                self.ui.cities_list.addItem(cities['name'], cities['objectId'])
            else:
                # Select first list item after list update
                self.ui.cities_list.setCurrentIndex(0)
                # UPDATE WORKER PROGRESS
                WEATHER_WORKER_PROGRESS_VALUE = 3
                progress_callback.emit(WEATHER_WORKER_PROGRESS_VALUE*25)

        except Exception as e:
            print(e)
            self.alert(e)


    ########################################################################
    ## 
    ########################################################################

    ########################################################################
    ## GET WEATHER INFORMATION OF SELECTED CITY LOCATION
    ########################################################################
    def get_weather(self, progress_callback):
        # GET GLOBAL VARIABLE
        global FINAL_WEATHER_ERROR
        FINAL_WEATHER_ERROR = "weather" #if an error occurs when loading continents, resume from this function


        ########################################################################
        ## CHECK IF THE CITIES AND COUNTRIES LISTS ARE EMPTY
        ########################################################################
        if not self.ui.cities_list.currentText() or not self.ui.countries_list.currentText():
            print("No location")
            # GET LOCATION INFORMATION
            if not self.ui.continents_list.currentText():
                self.weather_thread("continents")
            elif not self.ui.countries_list.currentText():
                self.weather_thread("countries")
            elif not self.ui.cities_list.currentText():
                self.weather_thread("cities")

            return

        ########################################################################
        ## GET LOCATION NAME
        ########################################################################
        weather_location = self.ui.cities_list.currentText()+', '+self.ui.countries_list.currentText()
        # print(weather_location)

        ########################################################################
        ## UPDATE UI LOCATION LABEL
        ########################################################################
        self.ui.weather_location.setText("Loading weather information for "+weather_location+'('+self.ui.continents_list.currentText()+')')

        try:
            url = "https://community-open-weather-map.p.rapidapi.com/weather"

            querystring = {"q":weather_location,"lat":"0","lon":"0","lang":"null","units":"metric","mode":"xml, html"}

            headers = {
                'x-rapidapi-key': "API_KEY", #Paste your api key here-----Get api key from https://rapidapi.com/community/api/open-weather-map/endpoints
                'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
                }

            weather = requests.request("GET", url, headers=headers, params=querystring)

            # UPDATE WORKER PROGRESS
            WEATHER_WORKER_PROGRESS_VALUE = 3.5
            progress_callback.emit(WEATHER_WORKER_PROGRESS_VALUE*25)

            # print(weather.text)
            ########################################################################
            ## GET LOCATION  WEATHER FORECAST
            ########################################################################
            try:
                url = "https://community-open-weather-map.p.rapidapi.com/forecast"

                forecasts = requests.request("GET", url, headers=headers, params=querystring)

                # print(forecasts.text)

                # UPDATE WORKER PROGRESS
                WEATHER_WORKER_PROGRESS_VALUE = 4
                progress_callback.emit(WEATHER_WORKER_PROGRESS_VALUE*25)

                # UPDATE WEATHER UI
                self.weather_result(weather.json(), forecasts.json())

                # WEATHER LOCATION LABLE
                self.ui.weather_location.setText(weather_location+'('+self.ui.continents_list.currentText()+')')

            except Exception as e:
                # Catch network errors.
                print(e)
                self.alert(e)


        except Exception as e:
            # Catch network errors.
            print(e)
            self.alert(e)

    ########################################################################
    ## 
    ########################################################################


    ########################################################################
    ## FUNCTION TO UPDATE UI WEATHER INFORMATION
    ########################################################################
    # View the weather response code(200 means everything is ok)
    def weather_result(self, weather, forecasts):
        if weather['cod'] != 200: 
            print(weather['message'])
            self.alert(weather['cod']+", "+weather['message'])
            return

        # UPDATE UI
        self.ui.latitude_label.setText("%.2f °" % weather['coord']['lat'])
        self.ui.longitude_label.setText("%.2f °" % weather['coord']['lon'])

        self.ui.wind_speed_label.setText("%.2f m/s" % weather['wind']['speed'])

        self.ui.temperature_label.setText("%.1f °C" % weather['main']['temp'])
        self.ui.pressure_label.setText("%d" % weather['main']['pressure'])

        self.ui.sunrise_label.setText(from_ts_to_time_of_day(weather['sys']['sunrise']))

        self.ui.current_weather_label.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        ))

        self.set_weather_icon(self.ui.current_weather_icon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self.ui, 'forecast_time%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(getattr(self.ui, 'forecast_icon%d' % n), forecast['weather'])
            getattr(self.ui, 'forecast_temp%d' % n).setText("%.1f °C" % forecast['main']['temp'])


    ########################################################################
    ## FUNCTION TO UPDATE WEATHER ICONS
    ########################################################################
    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 weather[0]['icon']
                                )))
    ########################################################################
    ## 
    ########################################################################


     ########################################################################
    ## ALERT FUNCTION TO DISPLAY ERRORS
    ########################################################################
    def alert(self, message):
        self.ui.message_frame.show()
        self.ui.message_label.setText(str(message))
    ########################################################################
    ## 
    ########################################################################

    ########################################################################
    ## RELOAD WEATHER AFTER AN ERROR
    ########################################################################
    def reload_weather(self):
        # Hide message box
        self.ui.message_frame.hide()
        # Get global variable
        global FINAL_WEATHER_ERROR;
        # Reload weather if an error occured
        print("Final error", FINAL_WEATHER_ERROR)
        self.weather_thread(FINAL_WEATHER_ERROR)





########################################################################
## DATE FROM TIME STAMP FUNCTION
########################################################################
def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")
########################################################################
## 
########################################################################











########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################       