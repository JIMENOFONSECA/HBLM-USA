'''
MIT License

Copyright (c) 2020 Jimeno A. Fonseca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os

METADATA_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "metadata.xlsx")
INTERMEDIATE_RESULT_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results", "intermediate_result.csv")
FINAL_RESULT_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results", "final_result.csv")
WEATHER_DATA_FOLDER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "weather_data")
BUILDING_PERFORMANCE_FOLDER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "building_data")
PREDICTION_DATA_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "training_prediction_data", "prediction_dataset.csv")
TRAINING_DATA_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "training_prediction_data", "training_dataset.csv")
MODEL_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results", "model.pkl")