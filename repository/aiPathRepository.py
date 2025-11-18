import pickle


class AIPathRepository:
    def __init__(self):
        self.file_path = "ai_model_path.pkl"
        self.model_path = ""
        self.type_model_path = ""

    def save_model_path(self, ai_path: str, ai_type_path: str):
        self.model_path = ai_path
        self.type_model_path = ai_type_path

        data = {"model_path": self.model_path, "type_model_path": self.type_model_path}
        with open(self.file_path, "wb") as f:
            pickle.dump(data, f)

    def load_model_path(self):
        try:
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
                self.model_path = data.get("model_path", "")
                self.type_model_path = data.get("type_model_path", "")
        except FileNotFoundError:
            self.model_path = ""
            self.type_model_path = ""
