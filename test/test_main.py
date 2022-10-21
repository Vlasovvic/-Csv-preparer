import json
import main

import pytest


class TestMain:

    def test_job_succsed(self):
        with open('test/docs/main_correct_21.10.2022.json') as test_obj:
            expected = json.load(test_obj)
            #expected = json.load(correct_file)
        with open('test/docs/test_config_21.10.2022.json') as raw_json:
            config = json.load(raw_json)
            actual = main.job(config)
        assert actual == expected

    def test_job_more_then_expected(self):
        headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4",
            "Series_title_5"
        ]
        actual_headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4",
            "Series_title_5",
            "Series_title_6"
        ]
        with pytest.raises(main.MoreColumnsThenExpected) as e:
            actual = main.check_exceptions(headers, actual_headers)
            assert actual == e

    def test_job_less_then_expected(self):
        headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4",
            "Series_title_5"
        ]
        actual_headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4"
        ]
        with pytest.raises(main.LessColumnsThenExpected) as e:
            actual = main.check_exceptions(headers, actual_headers)
            assert actual == e

    def test_job_HeadersError(self):
        headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4",
            "Series_title_5"
        ]
        actual_headers = [
            "Series_reference",
            "Period",
            "Data_value",
            "Suppressed",
            "STATUS",
            "UNITS",
            "Magnitude",
            "Subject",
            "Group",
            "Series_title_1",
            "Series_title_2",
            "Series_title_3",
            "Series_title_4",
            "Series_title_6"
        ]
        with pytest.raises(main.HeadersError) as e:
            actual = main.check_exceptions(headers, actual_headers)
            assert actual == e
