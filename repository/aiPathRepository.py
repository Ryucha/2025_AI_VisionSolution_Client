import pickle


class AIPathRepository:
    def __init__(self):
        self.file_path = "ai_model_path.pkl"
        self.model_path = ""

    def save_model_path(self, path: str):
        self.model_path = path
        with open(self.file_path, "wb") as f:
            pickle.dump(self.model_path, f)

    def load_model_path(self) -> str:
        try:
            with open(self.file_path, "rb") as f:
                self.model_path = pickle.load(f)
        except FileNotFoundError:
            self.model_path = ""
