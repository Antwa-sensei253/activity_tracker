import json
import pandas as pd
data = {
    "activities": [
        {
            "name": "Administrator: cmd - py  activity_tracker.py ",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:30:20",
                    "hours": 0,
                    "minutes": 0,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:49",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 47,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:28",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 26,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:09",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "github.com",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:30:21",
                    "hours": 0,
                    "minutes": 0,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Task View",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:30:23",
                    "hours": 0,
                    "minutes": 0,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:52",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:27:14",
                    "hours": 0,
                    "minutes": 57,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:43",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 41,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:47",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:51",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:19",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:23",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:26",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:27",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:30",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:03",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:05",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:18",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:28",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 26,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:30",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:34",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 32,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:51",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:56",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:23:16",
                    "hours": 3,
                    "minutes": 53,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:30:29",
                    "hours": 0,
                    "minutes": 0,
                    "seconds": 27,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:07",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:06:50",
                    "hours": 0,
                    "minutes": 36,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:06:52",
                    "hours": 0,
                    "minutes": 36,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:24:30",
                    "hours": 0,
                    "minutes": 54,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:31",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:41",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 39,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:50",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:52",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:25",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:21",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:25",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:27",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 26,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:29",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 27,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:04",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 2,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:17",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:20",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:08",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:15:53",
                    "hours": 1,
                    "minutes": 45,
                    "seconds": 52,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:15:59",
                    "hours": 1,
                    "minutes": 45,
                    "seconds": 58,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:12",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:27",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 26,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:31",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:20",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:24",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:47",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:51",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:55",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 54,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:57",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:44:26",
                    "hours": 2,
                    "minutes": 14,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:31",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:30:58",
                    "hours": 4,
                    "minutes": 0,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Introduction - Foxit PDF Reader",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:35:59",
                    "hours": 0,
                    "minutes": 5,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:41:27",
                    "hours": 0,
                    "minutes": 11,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:50",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:55",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 53,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:04:38",
                    "hours": 0,
                    "minutes": 34,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:06:49",
                    "hours": 0,
                    "minutes": 36,
                    "seconds": 47,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:24:26",
                    "hours": 0,
                    "minutes": 54,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:27:05",
                    "hours": 0,
                    "minutes": 57,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:04",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 2,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:13",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:17",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:14:23",
                    "hours": 1,
                    "minutes": 44,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:15:52",
                    "hours": 1,
                    "minutes": 45,
                    "seconds": 51,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:15:54",
                    "hours": 1,
                    "minutes": 45,
                    "seconds": 53,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:19",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 17,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:32",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "9 Things I Wish I Knew When I Started Programming - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:39",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:41:22",
                    "hours": 0,
                    "minutes": 11,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:48",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:37",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 35,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "New Tab - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:41",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 39,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:41:24",
                    "hours": 0,
                    "minutes": 11,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:38",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:09:01",
                    "hours": 1,
                    "minutes": 38,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:11:57",
                    "hours": 1,
                    "minutes": 41,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:41",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 39,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:48",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:44",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 42,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:02",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:30",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "(1) Feed | LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:57",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:56",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 54,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:25",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:37",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 35,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "(1) Notifications | LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:58",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:38",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Notifications | LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:36:59",
                    "hours": 0,
                    "minutes": 6,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:01",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:29",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:40",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 38,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:23:32",
                    "hours": 3,
                    "minutes": 53,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Feed | LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:37:51",
                    "hours": 0,
                    "minutes": 7,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:10",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:44",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 42,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:41:21",
                    "hours": 0,
                    "minutes": 11,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:10",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:35",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 34,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:37",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:11:00",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:11:09",
                    "hours": 2,
                    "minutes": 41,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Post | Feed | LinkedIn - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:38:12",
                    "hours": 0,
                    "minutes": 8,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:08",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Search",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:11",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 9,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:45",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:06:51",
                    "hours": 0,
                    "minutes": 36,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:06:53",
                    "hours": 0,
                    "minutes": 36,
                    "seconds": 51,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:24:29",
                    "hours": 0,
                    "minutes": 54,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:30",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:21",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:09",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:14",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:18",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 17,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:14:24",
                    "hours": 1,
                    "minutes": 44,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:50",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:11:02",
                    "hours": 2,
                    "minutes": 41,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:30:59",
                    "hours": 4,
                    "minutes": 0,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "WhatsApp",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:15",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:40:59",
                    "hours": 0,
                    "minutes": 10,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:07:58",
                    "hours": 0,
                    "minutes": 37,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:39",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:42",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 40,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:48",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:14",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:21",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:14:26",
                    "hours": 1,
                    "minutes": 44,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:11:08",
                    "hours": 2,
                    "minutes": 41,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Home - Chess.com - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 00:41:30",
                    "hours": 0,
                    "minutes": 11,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Play Chess Online for Free with Friends & Family - Chess.com - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:44",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 42,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Windows Shell Experience Host",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:02:57",
                    "hours": 0,
                    "minutes": 32,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Notification Center",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:04:39",
                    "hours": 0,
                    "minutes": 34,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:13:06",
                    "hours": 1,
                    "minutes": 43,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:45",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:48",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Albion Online Launcher",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:24:35",
                    "hours": 0,
                    "minutes": 54,
                    "seconds": 34,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "BattlEye Launcher",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:24:43",
                    "hours": 0,
                    "minutes": 54,
                    "seconds": 42,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Albion Online Client",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:27:04",
                    "hours": 0,
                    "minutes": 57,
                    "seconds": 2,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:27:09",
                    "hours": 0,
                    "minutes": 57,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:29",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 27,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:51",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:59",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:08",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:10",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:12",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:19",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 17,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:44",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 42,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:36:09",
                    "hours": 1,
                    "minutes": 6,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:21",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:24",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:29",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 27,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:38:58",
                    "hours": 1,
                    "minutes": 8,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:39:23",
                    "hours": 1,
                    "minutes": 9,
                    "seconds": 21,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:14",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:29",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:35",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 34,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:39",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 38,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:53:49",
                    "hours": 1,
                    "minutes": 23,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:53:56",
                    "hours": 1,
                    "minutes": 23,
                    "seconds": 54,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:24",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:55:49",
                    "hours": 1,
                    "minutes": 25,
                    "seconds": 47,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:03",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:16",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 14,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:59:06",
                    "hours": 1,
                    "minutes": 29,
                    "seconds": 4,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:08:58",
                    "hours": 1,
                    "minutes": 38,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:11:54",
                    "hours": 1,
                    "minutes": 41,
                    "seconds": 52,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Task Switching",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:27:07",
                    "hours": 0,
                    "minutes": 57,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:20",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:40",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 38,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:45",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:53",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 51,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:22",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:15",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 14,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:53:50",
                    "hours": 1,
                    "minutes": 23,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:54:25",
                    "hours": 1,
                    "minutes": 24,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:55:50",
                    "hours": 1,
                    "minutes": 25,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:18",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:59:07",
                    "hours": 1,
                    "minutes": 29,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:08",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:28:15",
                    "hours": 1,
                    "minutes": 58,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:29:52",
                    "hours": 1,
                    "minutes": 59,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:34:07",
                    "hours": 2,
                    "minutes": 4,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:45:18",
                    "hours": 2,
                    "minutes": 15,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:26",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:38",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:32",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:48",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:05",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:09",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:58",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:09:03",
                    "hours": 3,
                    "minutes": 39,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:15:11",
                    "hours": 3,
                    "minutes": 45,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:28:57",
                    "hours": 0,
                    "minutes": 58,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:03",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:36:18",
                    "hours": 1,
                    "minutes": 6,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:23",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 21,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:37:33",
                    "hours": 1,
                    "minutes": 7,
                    "seconds": 31,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:39:01",
                    "hours": 1,
                    "minutes": 8,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:39:28",
                    "hours": 1,
                    "minutes": 9,
                    "seconds": 26,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:18",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 17,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:31",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:37",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:53:54",
                    "hours": 1,
                    "minutes": 23,
                    "seconds": 52,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:53:59",
                    "hours": 1,
                    "minutes": 23,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:55:58",
                    "hours": 1,
                    "minutes": 25,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:56:27",
                    "hours": 1,
                    "minutes": 26,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:07",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:23",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:36",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 34,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:47",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:45",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:22",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 21,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:30:56",
                    "hours": 4,
                    "minutes": 0,
                    "seconds": 54,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Screen Snipping",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:09",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:11",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 9,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:29:13",
                    "hours": 0,
                    "minutes": 59,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "demons - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:39:04",
                    "hours": 1,
                    "minutes": 9,
                    "seconds": 2,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:39:26",
                    "hours": 1,
                    "minutes": 9,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Japanese Student Who Thinks \"Thank You\" In English Is \"F--- You\" - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:45:41",
                    "hours": 1,
                    "minutes": 15,
                    "seconds": 40,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:55:59",
                    "hours": 1,
                    "minutes": 25,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "HAPPY SOULS - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:56:21",
                    "hours": 1,
                    "minutes": 26,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Father warns Daughter about the Internet (1998) - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:14",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:57:17",
                    "hours": 1,
                    "minutes": 27,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 01:59:12",
                    "hours": 1,
                    "minutes": 29,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:09:00",
                    "hours": 1,
                    "minutes": 38,
                    "seconds": 58,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:01",
                    "hours": 1,
                    "minutes": 41,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:39",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:12",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "C:\\Users\\kingm\\Documents\\Rainmeter\\Skins\\Music Player\\Player.ini",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:02",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:35",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 33,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:30:57",
                    "hours": 4,
                    "minutes": 0,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "@M7MD - Discord",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:15",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Home",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:22",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:01",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Music",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:24",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:54",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 53,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "2 A.M Study Session -- - [lofi hip hop_chill beats](MP3_320K).mp3",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:12:25",
                    "hours": 1,
                    "minutes": 42,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Downloads",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:08",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "C:\\Users\\kingm\\Documents\\Rainmeter\\Skins\\Date\\Date skin.ini",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:16:22",
                    "hours": 1,
                    "minutes": 46,
                    "seconds": 21,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "System tray overflow window.",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:24:21",
                    "hours": 1,
                    "minutes": 54,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "so I spent 100\u20ac on my new weapon ... and went blackzone || Stream Highlights#262 || Albion Online - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:55",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 53,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:03",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:07",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:11",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 9,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:26",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:59",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:27:45",
                    "hours": 1,
                    "minutes": 57,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:28:14",
                    "hours": 1,
                    "minutes": 58,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:29:22",
                    "hours": 1,
                    "minutes": 59,
                    "seconds": 20,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:29:51",
                    "hours": 1,
                    "minutes": 59,
                    "seconds": 49,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:31:12",
                    "hours": 2,
                    "minutes": 1,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Sign in to Steam",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:57",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Steam",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:58",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 56,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:02",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:10",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 8,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:17",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Special Offers",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:25:59",
                    "hours": 1,
                    "minutes": 55,
                    "seconds": 57,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Getting Started - Scars of Honor - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:05",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Counter-Strike 2",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:26:27",
                    "hours": 1,
                    "minutes": 56,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:27:03",
                    "hours": 1,
                    "minutes": 57,
                    "seconds": 1,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:27:46",
                    "hours": 1,
                    "minutes": 57,
                    "seconds": 44,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:29:23",
                    "hours": 1,
                    "minutes": 59,
                    "seconds": 21,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:31:05",
                    "hours": 2,
                    "minutes": 1,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:31:15",
                    "hours": 2,
                    "minutes": 1,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:12",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:59",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 58,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:44:25",
                    "hours": 2,
                    "minutes": 14,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:45:17",
                    "hours": 2,
                    "minutes": 15,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:53:31",
                    "hours": 2,
                    "minutes": 23,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:08:57",
                    "hours": 2,
                    "minutes": 38,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:06",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:13",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:36",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 35,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:28:31",
                    "hours": 2,
                    "minutes": 58,
                    "seconds": 29,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:34:40",
                    "hours": 3,
                    "minutes": 4,
                    "seconds": 38,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:14",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:33",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 31,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:36:09",
                    "hours": 3,
                    "minutes": 6,
                    "seconds": 7,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:41:14",
                    "hours": 3,
                    "minutes": 11,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:07",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:47",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:50",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:20",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:37",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 35,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:48",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 46,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:06",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 4,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:17",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 15,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:00:54",
                    "hours": 3,
                    "minutes": 30,
                    "seconds": 52,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:02",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:15",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 13,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:26",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:57",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 55,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:02:19",
                    "hours": 3,
                    "minutes": 32,
                    "seconds": 17,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:09:02",
                    "hours": 3,
                    "minutes": 39,
                    "seconds": 0,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:09:41",
                    "hours": 3,
                    "minutes": 39,
                    "seconds": 39,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:15:00",
                    "hours": 3,
                    "minutes": 44,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:15:12",
                    "hours": 3,
                    "minutes": 45,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:23:12",
                    "hours": 3,
                    "minutes": 53,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Witch's Tea Party | Re:ZERO -Starting Life in Another World- Season 2 - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:31:13",
                    "hours": 2,
                    "minutes": 1,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:31:25",
                    "hours": 2,
                    "minutes": 1,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:33:49",
                    "hours": 2,
                    "minutes": 3,
                    "seconds": 48,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:34:06",
                    "hours": 2,
                    "minutes": 4,
                    "seconds": 5,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:44:38",
                    "hours": 2,
                    "minutes": 14,
                    "seconds": 36,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "ALBION ONLINE 5.4 DOUBLE BLADED VS 7.3 PRIMAL STAFF! - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:44:52",
                    "hours": 2,
                    "minutes": 14,
                    "seconds": 50,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:46:00",
                    "hours": 2,
                    "minutes": 15,
                    "seconds": 58,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Albion| 24m Profit 4.1 Fire vs 6.4 Awaken BloodMoon #shorts #albiononline #mmorpg #albiononlinepvp - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:46:27",
                    "hours": 2,
                    "minutes": 16,
                    "seconds": 25,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:53:34",
                    "hours": 2,
                    "minutes": 23,
                    "seconds": 32,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "memes from the internet 16 - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 02:53:39",
                    "hours": 2,
                    "minutes": 23,
                    "seconds": 37,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:09:01",
                    "hours": 2,
                    "minutes": 38,
                    "seconds": 59,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Who let my bro cook?!! \ud83d\ude2e\ud83d\udd25 #animeedits #shorts - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:09:26",
                    "hours": 2,
                    "minutes": 39,
                    "seconds": 24,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Massive McDonalds Menu Lights Up NYC || ViralHog - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:09:45",
                    "hours": 2,
                    "minutes": 39,
                    "seconds": 43,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "This dog plays like a true Brazilian \ud83d\ude02 - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:05",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:11",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "How Many Moons Could Earth Handle? #kurzgesagt #shorts - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:12",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:10:24",
                    "hours": 2,
                    "minutes": 40,
                    "seconds": 23,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "ALBION ONLINE | 8.3 GREAT NATURE GAMEPLAY | ONLY OUTNUMBERED I NEVER LOOSE ONLY WIN | INSANE PROFIT - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:30:32",
                    "hours": 3,
                    "minutes": 0,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:13",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 11,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:30",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:35:32",
                    "hours": 3,
                    "minutes": 5,
                    "seconds": 30,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:36:05",
                    "hours": 3,
                    "minutes": 6,
                    "seconds": 3,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:36:11",
                    "hours": 3,
                    "minutes": 6,
                    "seconds": 9,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:41:20",
                    "hours": 3,
                    "minutes": 11,
                    "seconds": 18,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:20",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 19,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:24",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 22,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Explaining Reinhard's Power to Someone Who Hasn't Seen Re:Zero - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:57:46",
                    "hours": 3,
                    "minutes": 27,
                    "seconds": 44,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:12",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:36",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 34,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:58:47",
                    "hours": 3,
                    "minutes": 28,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:04",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 2,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:08",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 03:59:18",
                    "hours": 3,
                    "minutes": 29,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:00",
                    "hours": 3,
                    "minutes": 30,
                    "seconds": 58,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:12",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 10,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:16",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 14,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:01:56",
                    "hours": 3,
                    "minutes": 31,
                    "seconds": 54,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:02:18",
                    "hours": 3,
                    "minutes": 32,
                    "seconds": 16,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:02:33",
                    "hours": 3,
                    "minutes": 32,
                    "seconds": 31,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:09:08",
                    "hours": 3,
                    "minutes": 39,
                    "seconds": 6,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:09:47",
                    "hours": 3,
                    "minutes": 39,
                    "seconds": 45,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:15:10",
                    "hours": 3,
                    "minutes": 45,
                    "seconds": 9,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:15:13",
                    "hours": 3,
                    "minutes": 45,
                    "seconds": 12,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:23:30",
                    "hours": 3,
                    "minutes": 53,
                    "seconds": 28,
                    "start_time": "2023-10-29 00:30:01"
                },
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:23:42",
                    "hours": 3,
                    "minutes": 53,
                    "seconds": 40,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        },
        {
            "name": "Top 10 Most Satisfying Reflect KOs | Albion Seneca7 - YouTube - Brave",
            "time_entries": [
                {
                    "days": 0,
                    "end_time": "2023-10-29 04:30:54",
                    "hours": 4,
                    "minutes": 0,
                    "seconds": 52,
                    "start_time": "2023-10-29 00:30:01"
                }
            ]
        }
    ]
}
df = pd.DataFrame(d['activities'])

df.plot()
