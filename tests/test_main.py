import io
import json
import unittest
from unittest.mock import patch
from main import classify_email, validate_result, SCHEMA


EXAMPLE = {
    "category": "訂單查詢",
    "priority": "中",
    "summary": "顧客詢問未到貨包裹。",
    "suggested_reply": "您好，請提供訂單編號，以便協助查詢物流。",
}


class FakeResponse:
    def __enter__(self):
        return self
    def __exit__(self, *_):
        return False
    def read(self, *args):
        return self._content.read(*args)
    def __init__(self, payload):
        self._content = io.BytesIO(json.dumps(payload, ensure_ascii=False).encode())
        

class ClassifierTests(unittest.TestCase):
    def test_schema_has_four_required_fields(self):
        self.assertEqual(len(SCHEMA["required"]), 4)

    def test_valid_output(self):
        self.assertEqual(validate_result(EXAMPLE), EXAMPLE)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_result({**EXAMPLE, "category": "未定義"})

    def test_missing_field(self):
        with self.assertRaises(ValueError):
            validate_result({"category": "訂單查詢"})

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            classify_email(" ")

    def test_remote_url_rejected(self):
        with self.assertRaises(ValueError):
            classify_email("測試", url="https://example.com")

    @patch("urllib.request.urlopen")
    def test_request_and_parse(self, mock_open):
        mock_open.return_value = FakeResponse({"message": {"content": json.dumps(EXAMPLE, ensure_ascii=False)}})
        result = classify_email("請幫我查詢包裹")
        self.assertEqual(result, EXAMPLE)
        request = mock_open.call_args.args[0]
        payload = json.loads(request.data)
        self.assertFalse(payload["stream"])
        self.assertEqual(payload["format"], SCHEMA)
        self.assertEqual(payload["messages"][1]["role"], "user")


if __name__ == "__main__":
    unittest.main()
