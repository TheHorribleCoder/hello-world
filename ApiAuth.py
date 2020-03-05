from __future__ import print_function
import os

import requests
import matplotlib as plt
from bs4 import BeautifulSoup

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class ApiAuth:

    def __init__(self, scopes, client_secret_file, application_name):
        self.scopes = scopes
        self.client_secret_file = client_secret_file
        self.application_name = application_name

    def getCredentials(self):

        """Gets valid user credentials from storage.
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        :return:
            Credentials, the obtained credential.
        """

        current_dir = os.getcwd()
        credentials_dir = os.path.join(current_dir, '.credentials')

        if not os.path.exists(credentials_dir):
            os.makedirs(credentials_dir)
        credential_path = os.path.join(credentials_dir, 'google-drive-credentials.json')
        store = Storage(credential_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.client_secret_file, self.scopes)
            flow.user_agent = self.application_name
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials


class Stocks:

    def __init__(self, stocks, stock_symbols):
        self.stocks = stocks
        self.stock_symbols = stock_symbols


    def scrap(self, stocks=None, stock_symbols=None):
        """
        Scrap the stock prices by inputting stock names or stock symbols and save them pd DataFrame.

        Parameters
        ----------
        stocks : list
                List of stocks

        stock_symbols : list
                List of stock symbols (Reuters Instrument Code)

        Returns
        ----------
        stock_frame : df
                Pandas DataFrame with scrapped stock prices
        """
        pass

    def write_cloud(self, stock_frame):
        """
        Upload the scrapped data to google docks spreadsheet.

        Parameters
        ----------
        stock_frame : Pandas DataFrame
                DataFrame with stock tickers and prices

        """
        pass

    def plot(self):
        """
        Plot the graph of stock price changes - to be implemented.
        """
        pass

    def set_limit(self, stock_limit, stock_frame):
        """
        Change colors according to price fluctuations

        Parameters
        ----------
        stock_limit : list of tuples
                List of the uppest and lowest prices

        stock_frame : Pandas DataFrame
                DataFrame with stock tickers and prices

        Returns
        ----------
        stock_frame : df
            Pandas DataFrame modified according to set alerts

        """
        pass