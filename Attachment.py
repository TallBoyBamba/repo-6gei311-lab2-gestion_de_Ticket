from abc import ABC, abstractmethod
import os


class Attachment(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def load(self) -> str:
        pass


class TextAttachment(Attachment):
    def load(self) -> str:
        return self.loadText()

    def loadText(self) -> str:
        if not os.path.exists(self.path):
            return f"Fichier introuvable : {self.path}"
        with open(self.path, "r", encoding="utf-8") as fichier:
            return fichier.read()


class ImageAttachment(Attachment):
    def load(self) -> str:
        return self.loadImage()

    def loadImage(self) -> str:
        if not os.path.exists(self.path):
            return f"Fichier introuvable : {self.path}"
        return self.path


class VideoAttachment(Attachment):
    def load(self) -> str:
        return self.loadVideo()

    def loadVideo(self) -> str:
        if not os.path.exists(self.path):
            return f"Fichier introuvable : {self.path}"
        return self.path  