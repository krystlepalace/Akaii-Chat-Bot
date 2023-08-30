from nudenet import NudeClassifier


classifier = NudeClassifier()
async def check(image: str) -> bool:
    return (classifier.classify(image)[image]["unsafe"] >= 0.4)

