import json
from database import handle_indoor_data

b='''
{
	"1": {
		"1": {
			"temperature": "11.0",
			"humidity": "11.8",
			"radiation": "11",
			"co2": "11",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "12.0",
			"humidity": "12.8",
			"radiation": "12",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "13.0",
			"humidity": "13.8",
			"radiation": "13",
			"co2": "13",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"2": {
		"1": {
			"temperature": "21.0",
			"humidity": "21.8",
			"radiation": "21",
			"co2": "21",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "22.0",
			"humidity": "22.8",
			"radiation": "22",
			"co2": "22",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "23.0",
			"humidity": "23.8",
			"radiation": "23",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"3": {
		"1": {
			"temperature": "31.0",
			"humidity": "31.8",
			"radiation": "31",
			"co2": "31",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "32.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"4": {
		"1": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"5": {
		"1": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"6": {
		"1": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"7": {
		"1": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	},
	"8": {
		"1": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"2": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		},
		"3": {
			"temperature": "27.0",
			"humidity": "62.8",
			"radiation": "105",
			"co2": "519",
			"update_time": "2016-09-09 21:09:34"
		}
	}
}'''

# def handle_indoor_data(request_data):
#     obj = json.loads(request_data)
#     keys = obj.keys()
#     print obj
#     print keys
#     for key in keys:
#         value = obj[key]
#         for key2 in value.keys():
#             value2=value[key2]
#             print  key, value2['update_time'], value2['temperature'], value2['humidity'],value2['radiation'], value2['co2']
#     print 'indoor data save success'+get_current_time()

obj = json.loads(b)
keys=obj.keys()
# print obj
print keys
for key in keys:
    value=obj[key]
#     print value
    for key2 in value.keys():
        print key2
        print value[key2]
# handle_indoor_data(b)