import os

machine1_fileID = "file-AXfn4QIUzV3KstQX80mHaolM"
machine2_fileID = "file-xyaCHnRJWNha4sa2pzF5khJC"
g7_fileID = "file-CJYm6QFXQ4CiXWD0wTwFbVZX"

gpt_examples_context_1 = '"Timestamp: 1577880000 (2020-01-01 12:00:00), Status: Online, Output: 0.428", "Timestamp: 1577898000 (2020-01-01 17:00:00), Status: Online-Warning, Output: 0.25", "Timestamp: 1577905200 (2020-01-01 19:00:00), Status: Online-Critical, Output: 0.216", "Timestamp: 1577908800 (2020-01-01 20:00:00), Status: Offline, Output: 0.196"'

st_examples_context_1 = 'Timestamp: 1577880000 (2020-01-01 12:00:00), Status: Online, Output: 0.428\nTimestamp: 1577898000 (2020-01-01 17:00:00), Status: Online-Warning, Output: 0.25\nTimestamp: 1577905200 (2020-01-01 19:00:00), Status: Online-Critical, Output: 0.216\nTimestamp: 1577908800 (2020-01-01 20:00:00), Status: Offline, Output: 0.196'

gpt_example_qa_1 = [["When did the machine go offline?", "At 20:00:00"], ["What was the machine's output at 07:00:00?", ".60"], ["What was the Machine's status at 17:30:00?", "Online-Warning"]]

st_example_qa_1 = "Q: When did the machine go offline?\nA: At 20:00:00\nQ:What was the machine's output at 07:00:00?\nA: .60\nQ: What was the Machine's status at 17:30:00?\nA: Online-Warning"

gpt_examples_context_2 = '"Timestamp: 1577880000 (2020-01-01 12:00:00), Status: Online, Output: 0.375", "Timestamp: 1577883600 (2020-01-01 13:00:00), Status: Online-Warning, Output: 0.25", "Timestamp: 1577890800 (2020-01-01 15:00:00), Status: Online-Critical, Output: 0.218", "Timestamp: 1577894400 (2020-01-01 16:00:00), Status: Offline, Output: 0.2"'
st_examples_context_2 = 'Timestamp: 1577880000 (2020-01-01 12:00:00), Status: Online, Output: 0.375\nTimestamp: 1577883600 (2020-01-01 13:00:00), Status: Online-Warning, Output: 0.25\nTimestamp: 1577890800 (2020-01-01 15:00:00), Status: Online-Critical, Output: 0.218\nTimestamp: 1577894400 (2020-01-01 16:00:00), Status: Offline, Output: 0.2'
gpt_example_qa_2 = [["When did the machine go offline?", "At 16:00:00"], ["What was the machine's output at 07:00:00?", ".583"], ["What was the Machine's status at 15:30:00?", "Online-Critical"]]
st_example_qa_2  = "Q: When did the machine go offline?\nA: At 16:00:00\nQ:What was the machine's output at 07:00:00?\nA: .583\nQ: What was the Machine's status at 15:30:00?\nA: Online-Critical"

gpt_examples_context_g7 = '"Country: Canada, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 1556.508, 2016: 1527.996, 2017: 1649.266, 2018: 1721.822, 2019: 1741.576, 2020: 1643.408", "Country: Japan, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 4444.931, 2016: 5003.678, 2017: 4930.837, 2018: 5036.892, 2019: 5148.781, 2020: 5048.688", "Country: United States, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 18238.3, 2016: 18745.1, 2017: 19542.975, 2018: 20611.875, 2019: 21433.225, 2020: 20932.75"'
st_examples_context_g7 = 'Country: Canada, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 1556.508, 2016: 1527.996, 2017: 1649.266, 2018: 1721.822, 2019: 1741.576, 2020: 1643.408\nCountry: Japan, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 4444.931, 2016: 5003.678, 2017: 4930.837, 2018: 5036.892, 2019: 5148.781, 2020: 5048.688\nCountry: United States, Subject Descriptor: Gross domestic product, current prices, Units: U.S. dollars, Scale: Billions, 2015: 18238.3, 2016: 18745.1, 2017: 19542.975, 2018: 20611.875, 2019: 21433.225, 2020: 20932.75'
gpt_example_qa_g7 = [["What was Canada's Gross Domestic Product for current prices in 2016?", "1528 Billion U.S. Dollars"], ["What was United States' Gross Domestic Product for current prices in 2017?", "19542.98 U.S. Dollars"], ["What was Japan's Gross Domestic Product for current prices in 2020?", "5048.69 Billlion U.S. Dollars"]]
st_example_qa_g7 = "Q: What was Canada's Gross Domestic Product for current prices in 2016?\nA: 1528 Billion U.S. Dollars\nWhat was United States' Gross Domestic Product for current prices in 2017?\nA: 19542.98 U.S. Dollars\nQ: What was Japan's Gross Domestic Product for current prices in 2020?\nA: 5048.69 Billlion U.S. Dollars"


# examples_context = '"text": "Timestamp: 1577880000 (2020-01-01 12:00:00), Status: Online, Output: 0.428", "text": "Timestamp: 1577898000 (2020-01-01 17:00:00), Status: Online-Warning, Output: 0.25", "text": "Timestamp: 1577905200 (2020-01-01 19:00:00), Status: Online-Critical, Output: 0.216", "text": "Timestamp: 1577908800 (2020-01-01 20:00:00), Status: Offline, Output: 0.196"'
#   examples = [["When did the machine go offline?", "At 8 p.m."], ["What was the machine's output at 7 a.m.?", "60%"], ["What was the Machine's status at 5:30 p.m.?", "Online-Warning"]]

