import base64
import requests


class BaseAPI:

    def __init__(self) -> None:
        self.url = ""

    def fetch_data(self, image: bytes) -> bytes | str | None:
        try:
            image_b64 = base64.b64encode(image).decode("utf-8")
            response = requests.post(self.url, json={"image": image_b64})
            if response.status_code != 200:
                raise Exception(f"{response.status_code} - {response.reason}")
            result = self.handle_data(response)
            return result
        except Exception as exception:
            print(f"ERROR: {exception}")

    def handle_data(self) -> None:
        raise Exception("ERROR: 'handle_data' not implemented")


class SegmentationAPI(BaseAPI):

    def __init__(self) -> None:
        super().__init__()
        self.url = "https://andres-alcala-gtz-brain-cancer-segmentation.hf.space/predict"

    def handle_data(self, response: requests.Response) -> bytes:
        data = response.json()
        prediction = data["prediction"]
        mask = base64.b64decode(prediction)
        return mask


class ClassificationAPI(BaseAPI):

    def __init__(self) -> None:
        super().__init__()
        self.url = "https://andres-alcala-gtz-brain-cancer-detection.hf.space/predict"

    def handle_data(self, response: requests.Response) -> str:
        data = response.json()
        prediction = data["prediction"]
        probability = "\n".join(f"{key}: {value}" for key, value in prediction.items())
        return probability
