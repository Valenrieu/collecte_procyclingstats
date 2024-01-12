#!/bin/python3

import export_riders_data
from export_races_url import export_urls
from export_races_data import main
from clean_dataframe import clean_races_file

if __name__=="__main__":
    export_urls()
    main()
    clean_races_file()
